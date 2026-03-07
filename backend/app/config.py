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


class FileObsidianConfig(BaseModel):
    vault_path: str = "D:/Yannick"
    allowed_roots: list[str] = Field(default_factory=lambda: ["D:/Yannick"])


class FileToolConfig(BaseModel):
    base_url: str


class FileToolsConfig(BaseModel):
    nocodb: FileToolConfig = FileToolConfig(base_url="http://localhost:8080")
    n8n: FileToolConfig = FileToolConfig(base_url="http://localhost:5678")
    perplexica: FileToolConfig = FileToolConfig(base_url="http://localhost:3001")
    openwebui: FileToolConfig = FileToolConfig(base_url="http://localhost:3000")


class FileLoggingConfig(BaseModel):
    level: str = "INFO"
    max_recent_actions: int = 20


class FileConfig(BaseModel):
    operator: FileOperatorConfig = FileOperatorConfig()
    obsidian: FileObsidianConfig = FileObsidianConfig()
    tools: FileToolsConfig = FileToolsConfig()
    logging: FileLoggingConfig = FileLoggingConfig()


class EnvironmentSettings(BaseSettings):
    app_name: str = "Cockpit OS DSI Transverse"
    app_env: str = "development"
    app_host: str = "0.0.0.0"
    app_port: int = 8000

    obsidian_vault_path: str = "D:/Yannick"
    obsidian_allowed_roots: str = "D:/Yannick"

    nocodb_base_url: str = "http://localhost:8080"
    n8n_base_url: str = "http://localhost:5678"
    perplexica_base_url: str = "http://localhost:3001"
    openwebui_base_url: str = "http://localhost:3000"

    cockpit_config_file: str = "./config/app.json"
    cockpit_log_dir: str = "./logs"

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
    log_dir: str

    obsidian_vault_path: str
    obsidian_allowed_roots: list[str]

    nocodb_base_url: str
    n8n_base_url: str
    perplexica_base_url: str
    openwebui_base_url: str

    max_recent_actions: int


def build_runtime_config() -> RuntimeConfig:
    env = EnvironmentSettings()
    config_file = Path(env.cockpit_config_file)
    if not config_file.is_absolute():
        config_file = (ROOT_DIR / config_file).resolve()

    file_config = _load_file_config(config_file)

    log_dir = Path(env.cockpit_log_dir)
    if not log_dir.is_absolute():
        log_dir = (ROOT_DIR / log_dir).resolve()

    allowed_roots_env = [
        item.strip() for item in env.obsidian_allowed_roots.split(",") if item.strip()
    ]
    allowed_roots = allowed_roots_env or file_config.obsidian.allowed_roots

    return RuntimeConfig(
        app_name=env.app_name,
        app_env=env.app_env,
        app_host=env.app_host,
        app_port=env.app_port,
        config_file=str(config_file),
        log_dir=str(log_dir),
        obsidian_vault_path=env.obsidian_vault_path or file_config.obsidian.vault_path,
        obsidian_allowed_roots=allowed_roots,
        nocodb_base_url=env.nocodb_base_url or file_config.tools.nocodb.base_url,
        n8n_base_url=env.n8n_base_url or file_config.tools.n8n.base_url,
        perplexica_base_url=env.perplexica_base_url or file_config.tools.perplexica.base_url,
        openwebui_base_url=env.openwebui_base_url or file_config.tools.openwebui.base_url,
        max_recent_actions=file_config.logging.max_recent_actions,
    )
