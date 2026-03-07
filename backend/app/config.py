from __future__ import annotations

from pathlib import Path
from typing import Any
import json

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


ROOT_DIR = Path(__file__).resolve().parents[2]


class FileOperatorConfig(BaseModel):
    workspace_name: str = "Cockpit OS DSI Transverse"
    default_page: str = "home"


class FileRuntimeConfig(BaseModel):
    app_name: str = "Cockpit OS DSI Transverse"
    app_env: str = "development"
    app_host: str = "0.0.0.0"
    app_port: int = 8000
    log_dir: str = "./logs"


class FileObsidianConfig(BaseModel):
    vault_path: str = "D:/Yannick"
    allowed_roots: list[str] = Field(default_factory=lambda: ["D:/Yannick"])


class FileToolConfig(BaseModel):
    base_url: str


class FileNocoDBToolConfig(FileToolConfig):
    writable_tables: list[str] = Field(default_factory=list)


class FileToolsConfig(BaseModel):
    nocodb: FileNocoDBToolConfig = FileNocoDBToolConfig(base_url="http://localhost:8080")
    n8n: FileToolConfig = FileToolConfig(base_url="http://localhost:5678")
    perplexica: FileToolConfig = FileToolConfig(base_url="http://localhost:3001")
    openwebui: FileToolConfig = FileToolConfig(base_url="http://localhost:3000")


class FileLoggingConfig(BaseModel):
    level: str = "INFO"
    max_recent_actions: int = 20


class FileConfig(BaseModel):
    runtime: FileRuntimeConfig = FileRuntimeConfig()
    operator: FileOperatorConfig = FileOperatorConfig()
    obsidian: FileObsidianConfig = FileObsidianConfig()
    tools: FileToolsConfig = FileToolsConfig()
    logging: FileLoggingConfig = FileLoggingConfig()


class EnvironmentSettings(BaseSettings):
    app_name: str | None = None
    app_env: str | None = None
    app_host: str | None = None
    app_port: int | None = None

    obsidian_vault_path: str | None = None
    obsidian_allowed_roots: str | None = None

    nocodb_base_url: str | None = None
    nocodb_writable_tables: str | None = None
    n8n_base_url: str | None = None
    perplexica_base_url: str | None = None
    openwebui_base_url: str | None = None

    cockpit_config_file: str = "./config/app.json"
    cockpit_log_dir: str | None = None
    cockpit_env_file: str | None = None

    model_config = SettingsConfigDict(
        env_file=ROOT_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


def _load_file_config(path: Path) -> FileConfig:
    if not path.exists():
        return FileConfig()

    with path.open("r", encoding="utf-8") as handle:
        data: dict[str, Any] = json.load(handle)
    return FileConfig.model_validate(data)


class RuntimeConfig(BaseModel):
    app_name: str
    app_env: str
    app_host: str
    app_port: int
    config_file: str
    env_file: str
    log_dir: str

    obsidian_vault_path: str
    obsidian_allowed_roots: list[str]

    nocodb_base_url: str
    nocodb_writable_tables: list[str]
    n8n_base_url: str
    perplexica_base_url: str
    openwebui_base_url: str

    max_recent_actions: int


def _pick_str(*values: str | None, default: str) -> str:
    for value in values:
        if value is None:
            continue
        candidate = value.strip()
        if candidate:
            return candidate
    return default


def _pick_int(*values: int | None, default: int) -> int:
    for value in values:
        if value is not None:
            return value
    return default


def build_runtime_config() -> RuntimeConfig:
    env = EnvironmentSettings()
    config_file = Path(env.cockpit_config_file)
    if not config_file.is_absolute():
        config_file = (ROOT_DIR / config_file).resolve()

    file_config = _load_file_config(config_file)

    env_file = Path(_pick_str(env.cockpit_env_file, default="./.env"))
    if not env_file.is_absolute():
        env_file = (ROOT_DIR / env_file).resolve()

    log_dir = Path(
        _pick_str(
            env.cockpit_log_dir,
            file_config.runtime.log_dir,
            default="./logs",
        )
    )
    if not log_dir.is_absolute():
        log_dir = (ROOT_DIR / log_dir).resolve()

    allowed_roots_env = [
        item.strip() for item in (env.obsidian_allowed_roots or "").split(",") if item.strip()
    ]
    allowed_roots = allowed_roots_env or file_config.obsidian.allowed_roots
    nocodb_writable_tables_env = [
        item.strip() for item in (env.nocodb_writable_tables or "").split(",") if item.strip()
    ]
    nocodb_writable_tables = nocodb_writable_tables_env or file_config.tools.nocodb.writable_tables

    return RuntimeConfig(
        app_name=_pick_str(env.app_name, file_config.runtime.app_name, default="Cockpit OS DSI Transverse"),
        app_env=_pick_str(env.app_env, file_config.runtime.app_env, default="development"),
        app_host=_pick_str(env.app_host, file_config.runtime.app_host, default="0.0.0.0"),
        app_port=_pick_int(env.app_port, file_config.runtime.app_port, default=8000),
        config_file=str(config_file),
        env_file=str(env_file),
        log_dir=str(log_dir),
        obsidian_vault_path=_pick_str(env.obsidian_vault_path, file_config.obsidian.vault_path, default="D:/Yannick"),
        obsidian_allowed_roots=allowed_roots,
        nocodb_base_url=_pick_str(env.nocodb_base_url, file_config.tools.nocodb.base_url, default="http://localhost:8080"),
        nocodb_writable_tables=nocodb_writable_tables,
        n8n_base_url=_pick_str(env.n8n_base_url, file_config.tools.n8n.base_url, default="http://localhost:5678"),
        perplexica_base_url=_pick_str(env.perplexica_base_url, file_config.tools.perplexica.base_url, default="http://localhost:3001"),
        openwebui_base_url=_pick_str(env.openwebui_base_url, file_config.tools.openwebui.base_url, default="http://localhost:3000"),
        max_recent_actions=file_config.logging.max_recent_actions,
    )
