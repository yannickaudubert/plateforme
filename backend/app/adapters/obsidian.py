from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import shutil

from app.models.obsidian import ObsidianNoteContent, ObsidianWriteResponse
from app.models.system import ToolHealth


class ObsidianAdapterError(Exception):
    """Base class for adapter-level Obsidian errors."""


class ObsidianPathError(ObsidianAdapterError):
    """Raised when a user-supplied note path violates guardrails."""


class ObsidianNotFoundError(ObsidianAdapterError):
    """Raised when a note cannot be found in the vault."""


class ObsidianConflictError(ObsidianAdapterError):
    """Raised when an operation conflicts with existing data."""


class ObsidianPreconditionError(ObsidianAdapterError):
    """Raised when optimistic locking precondition fails."""


class ObsidianAdapter:
    def __init__(self, vault_path: str, allowed_roots: list[str]) -> None:
        self.vault_path = Path(vault_path).resolve()
        self.allowed_roots = [Path(path) for path in allowed_roots]
        self.backup_dir_name = ".cockpit-backups"

    def _is_allowed_path(self, candidate: Path) -> bool:
        resolved = candidate.resolve()
        for root in self.allowed_roots:
            try:
                resolved.relative_to(root.resolve())
                return True
            except ValueError:
                continue
        return False

    def _validate_relative_markdown_path(self, note_path: str) -> Path:
        candidate_text = note_path.strip().replace("\\", "/")
        if not candidate_text:
            raise ObsidianPathError("Path cannot be empty")

        candidate = Path(candidate_text)
        if candidate.is_absolute():
            raise ObsidianPathError("Path must be relative to vault root")
        if candidate.suffix.lower() != ".md":
            raise ObsidianPathError("Only Markdown files (.md) are allowed")

        parts = list(candidate.parts)
        for part in parts:
            if part in {".", ".."}:
                raise ObsidianPathError("Relative traversal is not allowed")
            if part.lower() in {".obsidian", self.backup_dir_name.lower()}:
                raise ObsidianPathError("Access to internal directories is forbidden")

        resolved = (self.vault_path / candidate).resolve()
        try:
            resolved.relative_to(self.vault_path)
        except ValueError as exc:
            raise ObsidianPathError("Path escapes vault root") from exc

        if not self._is_allowed_path(resolved):
            raise ObsidianPathError("Path is outside allowed roots")
        return resolved

    def _to_relative_path(self, resolved: Path) -> str:
        return str(resolved.relative_to(self.vault_path)).replace("\\", "/")

    @staticmethod
    def _modified_iso(path: Path) -> str:
        return datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).isoformat()

    def _atomic_write(self, path: Path, content: str) -> None:
        temp_path = path.with_name(f"{path.name}.tmp-cockpit")
        temp_path.write_text(content, encoding="utf-8")
        temp_path.replace(path)

    def _write_backup(self, resolved_path: Path) -> None:
        relative = resolved_path.relative_to(self.vault_path)
        backup_dir = self.vault_path / self.backup_dir_name / relative.parent
        backup_dir.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        backup_name = f"{relative.stem}.{stamp}.bak{relative.suffix}"
        backup_path = backup_dir / backup_name
        shutil.copy2(resolved_path, backup_path)

    @staticmethod
    def _extract_frontmatter(content: str) -> dict[str, str]:
        lines = content.splitlines()
        if not lines or lines[0].strip() != "---":
            return {}

        end_index = None
        for index, line in enumerate(lines[1:], start=1):
            if line.strip() == "---":
                end_index = index
                break

        if end_index is None:
            return {}

        parsed: dict[str, str] = {}
        for line in lines[1:end_index]:
            if not line.strip() or ":" not in line:
                continue
            key, value = line.split(":", 1)
            parsed[key.strip()] = value.strip()
        return parsed

    def health(self) -> ToolHealth:
        if not self.vault_path.exists():
            return ToolHealth(
                tool="obsidian",
                status="degraded",
                message=f"Vault path not found: {self.vault_path}",
                checked_at=datetime.now(timezone.utc).isoformat(),
            )
        return ToolHealth(
            tool="obsidian",
            status="ok",
            message="Vault path is reachable",
            checked_at=datetime.now(timezone.utc).isoformat(),
        )

    def list_markdown_files(self, limit: int = 20) -> list[str]:
        if not self.vault_path.exists() or not self._is_allowed_path(self.vault_path):
            return []

        markdown_files: list[str] = []
        for file_path in sorted(self.vault_path.rglob("*.md")):
            # Guardrail: never surface .obsidian internal files as business content.
            if any(
                part.lower() in {".obsidian", self.backup_dir_name.lower()}
                for part in file_path.parts
            ):
                continue
            relative = file_path.relative_to(self.vault_path)
            markdown_files.append(str(relative).replace("\\", "/"))
            if len(markdown_files) >= limit:
                break
        return markdown_files

    def read_note(self, note_path: str) -> ObsidianNoteContent:
        resolved_path = self._validate_relative_markdown_path(note_path)
        if not resolved_path.exists():
            raise ObsidianNotFoundError(f"Note not found: {note_path}")

        content = resolved_path.read_text(encoding="utf-8")
        frontmatter = self._extract_frontmatter(content)
        relative_path = self._to_relative_path(resolved_path)
        return ObsidianNoteContent(
            path=relative_path,
            content=content,
            frontmatter=frontmatter,
            bytes_size=len(content.encode("utf-8")),
            modified_at=self._modified_iso(resolved_path),
        )

    def create_note(
        self,
        note_path: str,
        content: str,
        create_parents: bool = True,
    ) -> ObsidianWriteResponse:
        resolved_path = self._validate_relative_markdown_path(note_path)
        if resolved_path.exists():
            raise ObsidianConflictError(f"Note already exists: {note_path}")

        if create_parents:
            resolved_path.parent.mkdir(parents=True, exist_ok=True)
        elif not resolved_path.parent.exists():
            raise ObsidianPathError("Parent directory does not exist")

        self._atomic_write(resolved_path, content)
        relative_path = self._to_relative_path(resolved_path)
        return ObsidianWriteResponse(
            path=relative_path,
            status="created",
            bytes_written=len(content.encode("utf-8")),
            modified_at=self._modified_iso(resolved_path),
        )

    def update_note(
        self,
        note_path: str,
        content: str,
        expected_modified_at: str | None = None,
        create_backup: bool = True,
    ) -> ObsidianWriteResponse:
        resolved_path = self._validate_relative_markdown_path(note_path)
        if not resolved_path.exists():
            raise ObsidianNotFoundError(f"Note not found: {note_path}")

        current_modified_at = self._modified_iso(resolved_path)
        if expected_modified_at and expected_modified_at != current_modified_at:
            raise ObsidianPreconditionError(
                "Note has changed since last read. Refresh and retry."
            )

        if create_backup:
            self._write_backup(resolved_path)

        self._atomic_write(resolved_path, content)
        relative_path = self._to_relative_path(resolved_path)
        return ObsidianWriteResponse(
            path=relative_path,
            status="updated",
            bytes_written=len(content.encode("utf-8")),
            modified_at=self._modified_iso(resolved_path),
        )
