from __future__ import annotations

from app.logging import get_journal
from app.models.system import ActionLogEntry


class JournalService:
    def __init__(self, max_recent_actions: int) -> None:
        self._max_recent_actions = max_recent_actions

    def recent_actions(self) -> list[ActionLogEntry]:
        entries = get_journal().read_recent(limit=self._max_recent_actions)
        return [
            ActionLogEntry(
                timestamp=entry.timestamp,
                tool=entry.tool,
                action=entry.action,
                status=entry.status,
                details=entry.details,
            )
            for entry in entries
        ]
