from __future__ import annotations

from app.adapters.n8n import N8nAdapter
from app.adapters.nocodb import NocoDBAdapter
from app.adapters.obsidian import ObsidianAdapter
from app.adapters.openwebui import OpenWebUIAdapter
from app.adapters.perplexica import PerplexicaAdapter
from app.config import RuntimeConfig


class AdapterRegistry:
    def __init__(self, config: RuntimeConfig, nocodb_api_token: str | None = None) -> None:
        self.obsidian = ObsidianAdapter(
            vault_path=config.obsidian_vault_path,
            allowed_roots=config.obsidian_allowed_roots,
        )
        self.nocodb = NocoDBAdapter(
            base_url=config.nocodb_base_url,
            api_token=nocodb_api_token,
        )
        self.n8n = N8nAdapter(base_url=config.n8n_base_url)
        self.perplexica = PerplexicaAdapter(base_url=config.perplexica_base_url)
        self.openwebui = OpenWebUIAdapter(base_url=config.openwebui_base_url)
