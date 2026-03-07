from __future__ import annotations

from functools import lru_cache

from app.config import RuntimeConfig, build_runtime_config
from app.secrets import SecretSettings
from app.services.adapter_registry import AdapterRegistry
from app.services.journal_service import JournalService
from app.services.status_service import StatusService


@lru_cache(maxsize=1)
def get_runtime_config() -> RuntimeConfig:
    return build_runtime_config()


@lru_cache(maxsize=1)
def get_secrets() -> SecretSettings:
    return SecretSettings()


@lru_cache(maxsize=1)
def get_adapter_registry() -> AdapterRegistry:
    secrets = get_secrets()
    nocodb_token = (
        secrets.nocodb_api_token.get_secret_value().strip()
        if secrets.nocodb_api_token is not None
        else None
    )
    return AdapterRegistry(get_runtime_config(), nocodb_api_token=nocodb_token or None)


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
