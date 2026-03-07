from __future__ import annotations

import json
from pathlib import Path

from app.config import build_runtime_config


def _write_config(path: Path) -> None:
    data = {
        "runtime": {
            "app_name": "File Runtime Name",
            "app_env": "staging",
            "app_host": "127.0.0.1",
            "app_port": 9001,
            "log_dir": "./file-logs",
        },
        "obsidian": {
            "vault_path": "D:/FileVault",
            "allowed_roots": ["D:/FileVault", "D:/FileShared"],
        },
        "tools": {
            "nocodb": {
                "base_url": "http://file-nocodb:8080",
                "writable_tables": ["tbl_file_a", "tbl_file_b"],
            },
            "n8n": {"base_url": "http://file-n8n:5678"},
            "perplexica": {"base_url": "http://file-perplexica:3001"},
            "openwebui": {"base_url": "http://file-openwebui:3000"},
        },
        "logging": {"level": "INFO", "max_recent_actions": 42},
    }
    path.write_text(json.dumps(data), encoding="utf-8")


def test_build_runtime_config_uses_file_values_when_env_is_blank(tmp_path: Path, monkeypatch) -> None:
    config_file = tmp_path / "app.json"
    _write_config(config_file)

    monkeypatch.setenv("COCKPIT_CONFIG_FILE", str(config_file))
    monkeypatch.setenv("APP_NAME", " ")
    monkeypatch.setenv("APP_ENV", " ")
    monkeypatch.setenv("APP_HOST", " ")
    monkeypatch.setenv("APP_PORT", "9001")
    monkeypatch.setenv("OBSIDIAN_VAULT_PATH", " ")
    monkeypatch.setenv("OBSIDIAN_ALLOWED_ROOTS", " ")
    monkeypatch.setenv("NOCODB_BASE_URL", " ")
    monkeypatch.setenv("NOCODB_WRITABLE_TABLES", " ")
    monkeypatch.setenv("N8N_BASE_URL", " ")
    monkeypatch.setenv("PERPLEXICA_BASE_URL", " ")
    monkeypatch.setenv("OPENWEBUI_BASE_URL", " ")
    monkeypatch.setenv("COCKPIT_LOG_DIR", " ")

    runtime = build_runtime_config()

    assert runtime.app_name == "File Runtime Name"
    assert runtime.app_env == "staging"
    assert runtime.app_host == "127.0.0.1"
    assert runtime.app_port == 9001
    assert runtime.obsidian_vault_path == "D:/FileVault"
    assert runtime.obsidian_allowed_roots == ["D:/FileVault", "D:/FileShared"]
    assert runtime.nocodb_base_url == "http://file-nocodb:8080"
    assert runtime.nocodb_writable_tables == ["tbl_file_a", "tbl_file_b"]
    assert runtime.n8n_base_url == "http://file-n8n:5678"
    assert runtime.perplexica_base_url == "http://file-perplexica:3001"
    assert runtime.openwebui_base_url == "http://file-openwebui:3000"
    assert runtime.max_recent_actions == 42
    assert runtime.log_dir.endswith("file-logs")


def test_build_runtime_config_env_overrides_file(tmp_path: Path, monkeypatch) -> None:
    config_file = tmp_path / "app.json"
    _write_config(config_file)

    monkeypatch.setenv("COCKPIT_CONFIG_FILE", str(config_file))
    monkeypatch.setenv("APP_NAME", "Env Runtime Name")
    monkeypatch.setenv("APP_ENV", "production")
    monkeypatch.setenv("APP_HOST", "0.0.0.0")
    monkeypatch.setenv("APP_PORT", "7777")
    monkeypatch.setenv("OBSIDIAN_VAULT_PATH", "D:/EnvVault")
    monkeypatch.setenv("OBSIDIAN_ALLOWED_ROOTS", "D:/EnvVault,D:/Other")
    monkeypatch.setenv("NOCODB_BASE_URL", "http://env-nocodb:8080")
    monkeypatch.setenv("NOCODB_WRITABLE_TABLES", "tbl_env_a,tbl_env_b")
    monkeypatch.setenv("N8N_BASE_URL", "http://env-n8n:5678")
    monkeypatch.setenv("PERPLEXICA_BASE_URL", "http://env-perplexica:3001")
    monkeypatch.setenv("OPENWEBUI_BASE_URL", "http://env-openwebui:3000")
    monkeypatch.setenv("COCKPIT_LOG_DIR", "./env-logs")

    runtime = build_runtime_config()

    assert runtime.app_name == "Env Runtime Name"
    assert runtime.app_env == "production"
    assert runtime.app_host == "0.0.0.0"
    assert runtime.app_port == 7777
    assert runtime.obsidian_vault_path == "D:/EnvVault"
    assert runtime.obsidian_allowed_roots == ["D:/EnvVault", "D:/Other"]
    assert runtime.nocodb_base_url == "http://env-nocodb:8080"
    assert runtime.nocodb_writable_tables == ["tbl_env_a", "tbl_env_b"]
    assert runtime.n8n_base_url == "http://env-n8n:5678"
    assert runtime.perplexica_base_url == "http://env-perplexica:3001"
    assert runtime.openwebui_base_url == "http://env-openwebui:3000"
    assert runtime.max_recent_actions == 42
    assert runtime.log_dir.endswith("env-logs")
