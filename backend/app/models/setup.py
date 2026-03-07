from __future__ import annotations

from pydantic import BaseModel, Field


class SetupRuntimeInput(BaseModel):
    app_name: str = Field(min_length=1, max_length=200)
    app_env: str = Field(min_length=1, max_length=100)
    app_host: str = Field(min_length=1, max_length=200)
    app_port: int = Field(ge=1, le=65535)
    log_dir: str = Field(min_length=1, max_length=500)


class SetupObsidianInput(BaseModel):
    vault_path: str = Field(min_length=1, max_length=500)
    allowed_roots: list[str] = Field(default_factory=list)


class SetupToolsInput(BaseModel):
    nocodb_base_url: str = Field(min_length=1, max_length=500)
    nocodb_writable_tables: list[str] = Field(default_factory=list)
    n8n_base_url: str = Field(min_length=1, max_length=500)
    perplexica_base_url: str = Field(min_length=1, max_length=500)
    openwebui_base_url: str = Field(min_length=1, max_length=500)


class SetupSecretsInput(BaseModel):
    nocodb_api_token: str | None = None
    n8n_api_key: str | None = None
    perplexica_api_key: str | None = None
    openwebui_api_key: str | None = None


class SetupConfigurationState(BaseModel):
    config_file: str
    env_file: str
    runtime: SetupRuntimeInput
    obsidian: SetupObsidianInput
    tools: SetupToolsInput
    secret_flags: dict[str, bool]


class SetupApplyRequest(BaseModel):
    runtime: SetupRuntimeInput
    obsidian: SetupObsidianInput
    tools: SetupToolsInput
    secrets: SetupSecretsInput = Field(default_factory=SetupSecretsInput)
    update_secrets: bool = True


class SetupApplyResponse(BaseModel):
    status: str
    config_file: str
    env_file: str
    updated_env_keys: list[str]
    updated_secret_keys: list[str]
    warnings: list[str]
