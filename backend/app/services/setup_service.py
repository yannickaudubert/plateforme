from __future__ import annotations

from pathlib import Path
import json
import re
from typing import Any

from app.models.setup import SetupApplyRequest, SetupApplyResponse, SetupConfigurationState


class SetupValidationError(Exception):
    """Raised when setup payload is invalid."""


class SetupService:
    _ENV_LINE_PATTERN = re.compile(r"^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.*)$")

    def __init__(self, config_file: str, env_file: str) -> None:
        self.config_file = Path(config_file)
        self.env_file = Path(env_file)

    def get_state(self, runtime: dict[str, Any], secret_flags: dict[str, bool]) -> SetupConfigurationState:
        return SetupConfigurationState(
            config_file=str(self.config_file),
            env_file=str(self.env_file),
            runtime=runtime["runtime"],
            obsidian=runtime["obsidian"],
            tools=runtime["tools"],
            secret_flags=secret_flags,
        )

    def apply(self, payload: SetupApplyRequest) -> SetupApplyResponse:
        if not payload.obsidian.allowed_roots:
            raise SetupValidationError("obsidian.allowed_roots must contain at least one path")

        cleaned_roots = [item.strip() for item in payload.obsidian.allowed_roots if item.strip()]
        if not cleaned_roots:
            raise SetupValidationError("obsidian.allowed_roots cannot be blank")

        config_data = self._read_config_data()
        config_data.setdefault("runtime", {})
        config_data.setdefault("obsidian", {})
        config_data.setdefault("tools", {})
        config_data["tools"].setdefault("nocodb", {})
        config_data["tools"].setdefault("n8n", {})
        config_data["tools"].setdefault("perplexica", {})
        config_data["tools"].setdefault("openwebui", {})

        config_data["runtime"]["app_name"] = payload.runtime.app_name
        config_data["runtime"]["app_env"] = payload.runtime.app_env
        config_data["runtime"]["app_host"] = payload.runtime.app_host
        config_data["runtime"]["app_port"] = payload.runtime.app_port
        config_data["runtime"]["log_dir"] = payload.runtime.log_dir

        config_data["obsidian"]["vault_path"] = payload.obsidian.vault_path
        config_data["obsidian"]["allowed_roots"] = cleaned_roots

        config_data["tools"]["nocodb"]["base_url"] = payload.tools.nocodb_base_url
        config_data["tools"]["n8n"]["base_url"] = payload.tools.n8n_base_url
        config_data["tools"]["perplexica"]["base_url"] = payload.tools.perplexica_base_url
        config_data["tools"]["openwebui"]["base_url"] = payload.tools.openwebui_base_url

        self._write_config_data(config_data)

        env_updates = {
            "APP_NAME": payload.runtime.app_name,
            "APP_ENV": payload.runtime.app_env,
            "APP_HOST": payload.runtime.app_host,
            "APP_PORT": str(payload.runtime.app_port),
            "COCKPIT_LOG_DIR": payload.runtime.log_dir,
            "OBSIDIAN_VAULT_PATH": payload.obsidian.vault_path,
            "OBSIDIAN_ALLOWED_ROOTS": ",".join(cleaned_roots),
            "NOCODB_BASE_URL": payload.tools.nocodb_base_url,
            "N8N_BASE_URL": payload.tools.n8n_base_url,
            "PERPLEXICA_BASE_URL": payload.tools.perplexica_base_url,
            "OPENWEBUI_BASE_URL": payload.tools.openwebui_base_url,
        }

        updated_secret_keys: list[str] = []
        if payload.update_secrets:
            secrets_map = {
                "NOCODB_API_TOKEN": payload.secrets.nocodb_api_token,
                "N8N_API_KEY": payload.secrets.n8n_api_key,
                "PERPLEXICA_API_KEY": payload.secrets.perplexica_api_key,
                "OPENWEBUI_API_KEY": payload.secrets.openwebui_api_key,
            }
            for key, value in secrets_map.items():
                if value is None:
                    continue
                trimmed = value.strip()
                if not trimmed:
                    continue
                env_updates[key] = trimmed
                updated_secret_keys.append(key)

        updated_env_keys = self._upsert_env_values(env_updates)

        warnings: list[str] = []
        if not updated_secret_keys:
            warnings.append("No secret values were updated.")

        return SetupApplyResponse(
            status="applied",
            config_file=str(self.config_file),
            env_file=str(self.env_file),
            updated_env_keys=updated_env_keys,
            updated_secret_keys=updated_secret_keys,
            warnings=warnings,
        )

    def _read_config_data(self) -> dict[str, Any]:
        if not self.config_file.exists():
            return {}
        with self.config_file.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
        if not isinstance(data, dict):
            return {}
        return data

    def _write_config_data(self, data: dict[str, Any]) -> None:
        self.config_file.parent.mkdir(parents=True, exist_ok=True)
        with self.config_file.open("w", encoding="utf-8") as handle:
            json.dump(data, handle, indent=2, ensure_ascii=True)
            handle.write("\n")

    @staticmethod
    def _format_env_value(value: str) -> str:
        if any(token in value for token in (" ", "#", '"')):
            escaped = value.replace('"', '\\"')
            return f'"{escaped}"'
        return value

    def _upsert_env_values(self, updates: dict[str, str]) -> list[str]:
        self.env_file.parent.mkdir(parents=True, exist_ok=True)
        if self.env_file.exists():
            lines = self.env_file.read_text(encoding="utf-8").splitlines()
        else:
            lines = []

        line_by_key: dict[str, int] = {}
        for index, line in enumerate(lines):
            match = self._ENV_LINE_PATTERN.match(line)
            if not match:
                continue
            line_by_key[match.group(1)] = index

        updated_keys: list[str] = []
        for key, raw_value in updates.items():
            formatted = f"{key}={self._format_env_value(raw_value)}"
            if key in line_by_key:
                lines[line_by_key[key]] = formatted
            else:
                lines.append(formatted)
            updated_keys.append(key)

        self.env_file.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")
        return updated_keys
