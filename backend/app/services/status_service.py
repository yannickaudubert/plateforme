from __future__ import annotations

from app.models.system import SystemStatusResponse
from app.services.adapter_registry import AdapterRegistry
from app.services.journal_service import JournalService


class StatusService:
    def __init__(self, environment: str, adapters: AdapterRegistry, journal: JournalService) -> None:
        self._environment = environment
        self._adapters = adapters
        self._journal = journal

    def system_status(self) -> SystemStatusResponse:
        tools = [
            self._adapters.obsidian.health(),
            self._adapters.nocodb.health(),
            self._adapters.n8n.health(),
            self._adapters.perplexica.health(),
            self._adapters.openwebui.health(),
        ]
        actions = self._journal.recent_actions()
        return SystemStatusResponse(
            environment=self._environment,
            tools=tools,
            recent_actions=actions,
        )
