from __future__ import annotations

import json
from pathlib import Path

import pytest

from app.models.setup import SetupApplyRequest, SetupObsidianInput, SetupRuntimeInput, SetupToolsInput
from app.services.setup_service import SetupService, SetupValidationError


def _request() -> SetupApplyRequest:
    return SetupApplyRequest(
        runtime=SetupRuntimeInput(
            app_name="Cockpit Test",
            app_env="development",
            app_host="0.0.0.0",
            app_port=8000,
            log_dir="./logs",
        ),
        obsidian=SetupObsidianInput(
            vault_path="D:/Vault",
            allowed_roots=["D:/Vault", "D:/Shared"],
        ),
        tools=SetupToolsInput(
            nocodb_base_url="http://localhost:8080",
            nocodb_writable_tables=["tbl_projects", "tbl_actions"],
            n8n_base_url="http://localhost:5678",
            perplexica_base_url="http://localhost:3001",
            openwebui_base_url="http://localhost:3000",
        ),
    )


def test_apply_writes_config_and_env(tmp_path: Path) -> None:
    config_file = tmp_path / "app.json"
    env_file = tmp_path / ".env"
    env_file.write_text("APP_NAME=Old\n", encoding="utf-8")

    service = SetupService(config_file=str(config_file), env_file=str(env_file))
    payload = _request()
    payload.secrets.nocodb_api_token = "token-123"

    result = service.apply(payload)
    assert result.status == "applied"
    assert "APP_NAME" in result.updated_env_keys
    assert "NOCODB_API_TOKEN" in result.updated_secret_keys

    config_data = json.loads(config_file.read_text(encoding="utf-8"))
    assert config_data["runtime"]["app_name"] == "Cockpit Test"
    assert config_data["obsidian"]["allowed_roots"] == ["D:/Vault", "D:/Shared"]
    assert config_data["tools"]["nocodb"]["base_url"] == "http://localhost:8080"
    assert config_data["tools"]["nocodb"]["writable_tables"] == ["tbl_projects", "tbl_actions"]

    env_text = env_file.read_text(encoding="utf-8")
    assert 'APP_NAME="Cockpit Test"' in env_text
    assert "NOCODB_API_TOKEN=token-123" in env_text
    assert "NOCODB_WRITABLE_TABLES=tbl_projects,tbl_actions" in env_text
    assert "OBSIDIAN_ALLOWED_ROOTS=D:/Vault,D:/Shared" in env_text


def test_apply_rejects_empty_allowed_roots(tmp_path: Path) -> None:
    service = SetupService(
        config_file=str(tmp_path / "app.json"),
        env_file=str(tmp_path / ".env"),
    )
    payload = _request()
    payload.obsidian.allowed_roots = []

    with pytest.raises(SetupValidationError):
        service.apply(payload)
