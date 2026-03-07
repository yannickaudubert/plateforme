from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from app.models.system import ToolHealth


class ObsidianAdapter:
    def __init__(self, vault_path: str, allowed_roots: list[str]) -> None:
        self.vault_path = Path(vault_path)
        self.allowed_roots = [Path(path) for path in allowed_roots]

    def _is_allowed_path(self, candidate: Path) -> bool:
        resolved = candidate.resolve()
        for root in self.allowed_roots:
            try:
                resolved.relative_to(root.resolve())
                return True
            except ValueError:
                continue
        return False

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
        for file_path in self.vault_path.rglob("*.md"):
            # Guardrail: never surface .obsidian internal files as business content.
            if ".obsidian" in file_path.parts:
                continue
            relative = file_path.relative_to(self.vault_path)
            markdown_files.append(str(relative).replace("\\", "/"))
            if len(markdown_files) >= limit:
                break
        return markdown_files
