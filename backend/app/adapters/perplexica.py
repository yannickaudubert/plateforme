from __future__ import annotations

from app.adapters.http_probe import probe_http_tool
from app.models.system import ToolHealth


class PerplexicaAdapter:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def health(self) -> ToolHealth:
        return probe_http_tool(tool="perplexica", base_url=self.base_url)
