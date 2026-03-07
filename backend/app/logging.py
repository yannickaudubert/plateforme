from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
import json
import logging
import sqlite3
import threading

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
        self._db_file = self._log_dir / "actions.sqlite3"
        self._lock = threading.Lock()
        self._initialize_db()

    @property
    def log_dir(self) -> Path:
        return self._log_dir

    def _connection(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self._db_file, timeout=5.0)
        connection.row_factory = sqlite3.Row
        return connection

    def _initialize_db(self) -> None:
        with self._lock:
            with self._connection() as connection:
                connection.execute(
                    """
                    CREATE TABLE IF NOT EXISTS action_journal (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        timestamp TEXT NOT NULL,
                        tool TEXT NOT NULL,
                        action TEXT NOT NULL,
                        status TEXT NOT NULL,
                        details_json TEXT NOT NULL
                    )
                    """
                )
                connection.execute(
                    """
                    CREATE INDEX IF NOT EXISTS idx_action_journal_timestamp
                    ON action_journal(timestamp DESC)
                    """
                )
                connection.commit()

    def write(self, entry: JournalEntry) -> None:
        with self._lock:
            with self._connection() as connection:
                connection.execute(
                    """
                    INSERT INTO action_journal (timestamp, tool, action, status, details_json)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        entry.timestamp,
                        entry.tool,
                        entry.action,
                        entry.status,
                        json.dumps(entry.details, ensure_ascii=True),
                    ),
                )
                connection.commit()

    def read_recent(self, limit: int = 20) -> list[JournalEntry]:
        normalized_limit = max(1, min(limit, 200))
        with self._lock:
            with self._connection() as connection:
                rows = connection.execute(
                    """
                    SELECT timestamp, tool, action, status, details_json
                    FROM action_journal
                    ORDER BY id DESC
                    LIMIT ?
                    """,
                    (normalized_limit,),
                ).fetchall()

        entries: list[JournalEntry] = []
        for row in reversed(rows):
            details_value: dict[str, object] = {}
            raw_details = row["details_json"]
            if isinstance(raw_details, str) and raw_details.strip():
                try:
                    parsed = json.loads(raw_details)
                    if isinstance(parsed, dict):
                        details_value = parsed
                except ValueError:
                    details_value = {}
            entries.append(
                JournalEntry(
                    timestamp=str(row["timestamp"]),
                    tool=str(row["tool"]),
                    action=str(row["action"]),
                    status=str(row["status"]),
                    details=details_value,
                )
            )
        return entries


_journal_lock = threading.Lock()
_journal: ActionJournal | None = None


def get_journal() -> ActionJournal:
    global _journal
    runtime = build_runtime_config()
    expected_log_dir = Path(runtime.log_dir).resolve()
    with _journal_lock:
        if _journal is None or _journal.log_dir.resolve() != expected_log_dir:
            _journal = ActionJournal(str(expected_log_dir))
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
    get_journal().write(entry)
