from __future__ import annotations

from functools import lru_cache

from app.config import RuntimeConfig, build_runtime_config
from app.secrets import SecretSettings
from app.services.adapter_registry import AdapterRegistry
from app.services.journal_service import JournalService
from app.services.setup_service import SetupService
from app.services.status_service import StatusService


@lru_cache(maxsize=1)
def get_runtime_config() -> RuntimeConfig:
    return build_runtime_config()


@lru_cache(maxsize=1)
def get_secrets() -> SecretSettings:
    runtime = get_runtime_config()
    return SecretSettings(_env_file=runtime.env_file, _env_file_encoding="utf-8")


@lru_cache(maxsize=1)
def get_adapter_registry() -> AdapterRegistry:
    secrets = get_secrets()
    nocodb_token = (
        secrets.nocodb_api_token.get_secret_value().strip()
        if secrets.nocodb_api_token is not None
        else None
    )
    n8n_api_key = (
        secrets.n8n_api_key.get_secret_value().strip()
        if secrets.n8n_api_key is not None
        else None
    )
    perplexica_api_key = (
        secrets.perplexica_api_key.get_secret_value().strip()
        if secrets.perplexica_api_key is not None
        else None
    )
    openwebui_api_key = (
        secrets.openwebui_api_key.get_secret_value().strip()
        if secrets.openwebui_api_key is not None
        else None
    )
    return AdapterRegistry(
        get_runtime_config(),
        nocodb_api_token=nocodb_token or None,
        n8n_api_key=n8n_api_key or None,
        perplexica_api_key=perplexica_api_key or None,
        openwebui_api_key=openwebui_api_key or None,
    )


@lru_cache(maxsize=1)
def get_journal_service() -> JournalService:
    return JournalService(max_recent_actions=get_runtime_config().max_recent_actions)


@lru_cache(maxsize=1)
def get_status_service() -> StatusService:
    runtime = get_runtime_config()
    return StatusService(
        environment=runtime.app_env,
        adapters=get_adapter_registry(),
        journal=get_journal_service(),
    )


def clear_runtime_caches() -> None:
    get_setup_service.cache_clear()
    get_status_service.cache_clear()
    get_journal_service.cache_clear()
    get_adapter_registry.cache_clear()
    get_secrets.cache_clear()
    get_runtime_config.cache_clear()


@lru_cache(maxsize=1)
def get_setup_service() -> SetupService:
    runtime = get_runtime_config()
    return SetupService(config_file=runtime.config_file, env_file=runtime.env_file)
