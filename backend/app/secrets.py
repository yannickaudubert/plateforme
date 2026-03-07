from __future__ import annotations

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

from app.config import ROOT_DIR


class SecretSettings(BaseSettings):
    nocodb_api_token: SecretStr | None = None
    n8n_api_key: SecretStr | None = None
    perplexica_api_key: SecretStr | None = None
    openwebui_api_key: SecretStr | None = None

    model_config = SettingsConfigDict(
        env_file=ROOT_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


def secret_is_set(secret: SecretStr | None) -> bool:
    if secret is None:
        return False
    return bool(secret.get_secret_value().strip())


def get_secret_flags() -> dict[str, bool]:
    secrets = SecretSettings()
    return {
        "nocodb_token_set": secret_is_set(secrets.nocodb_api_token),
        "n8n_api_key_set": secret_is_set(secrets.n8n_api_key),
        "perplexica_api_key_set": secret_is_set(secrets.perplexica_api_key),
        "openwebui_api_key_set": secret_is_set(secrets.openwebui_api_key),
    }
