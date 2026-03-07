from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
import json
import logging

from app.config import build_runtime_config


def _sanitize_details(details: dict[str, object]) -> dict[str, object]:
    sanitized: dict[str, object] = {}
    for key, value in details.items():
        lowered = key.lower()
        if "secret" in lowered or "token" in lowered or "key" in lowered:
            sanitized[key] = "***"
        else:
            sanitized[key] = value
    return sanitized


@dataclass
class JournalEntry:
    timestamp: str
    tool: str
    action: str
    status: str
    details: dict[str, object]


class ActionJournal:
    def __init__(self, log_dir: str) -> None:
        self._log_dir = Path(log_dir)
        self._log_dir.mkdir(parents=True, exist_ok=True)
        self._log_file = self._log_dir / "actions.log"

    def write(self, entry: JournalEntry) -> None:
        line = json.dumps(entry.__dict__, ensure_ascii=True)
        with self._log_file.open("a", encoding="utf-8") as handle:
            handle.write(line + "\n")

    def read_recent(self, limit: int = 20) -> list[JournalEntry]:
        if not self._log_file.exists():
            return []

        with self._log_file.open("r", encoding="utf-8") as handle:
            rows = [row.strip() for row in handle.readlines() if row.strip()]

        selected = rows[-limit:]
        entries: list[JournalEntry] = []
        for row in selected:
            data = json.loads(row)
            entries.append(
                JournalEntry(
                    timestamp=data.get("timestamp", ""),
                    tool=data.get("tool", ""),
                    action=data.get("action", ""),
                    status=data.get("status", ""),
                    details=data.get("details", {}),
                )
            )
        return entries


_config = build_runtime_config()
_journal = ActionJournal(_config.log_dir)


def get_journal() -> ActionJournal:
    return _journal


def setup_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )


def log_action(tool: str, action: str, status: str, details: dict[str, object] | None = None) -> None:
    payload = _sanitize_details(details or {})
    entry = JournalEntry(
        timestamp=datetime.now(timezone.utc).isoformat(),
        tool=tool,
        action=action,
        status=status,
        details=payload,
    )
    _journal.write(entry)
