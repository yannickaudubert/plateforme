from __future__ import annotations

from typing import Any

import httpx

from app.adapters.http_probe import probe_http_tool
from app.models.openwebui import OpenWebUIModelSummary
from app.models.system import ToolHealth


class OpenWebUIAdapterError(Exception):
    """Base class for Open WebUI adapter errors."""


class OpenWebUIAuthenticationError(OpenWebUIAdapterError):
    """Raised when Open WebUI authentication fails."""


class OpenWebUIRequestError(OpenWebUIAdapterError):
    """Raised for Open WebUI upstream errors."""


class OpenWebUIAdapter:
    def __init__(self, base_url: str, api_key: str | None = None) -> None:
        self.base_url = base_url.rstrip("/")
        self.api_key = (api_key or "").strip()

    def _headers(self) -> dict[str, str]:
        headers: dict[str, str] = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        return headers

    @staticmethod
    def _extract_error_message(response: httpx.Response) -> str:
        try:
            payload = response.json()
        except ValueError:
            return (response.text or "Open WebUI request failed").strip()
        if isinstance(payload, dict):
            for key in ("message", "error", "detail"):
                value = payload.get(key)
                if isinstance(value, str) and value.strip():
                    return value.strip()
        return "Open WebUI request failed"

    def _request(
        self,
        method: str,
        path: str,
        payload: dict[str, Any] | None = None,
    ) -> Any:
        if not self.base_url:
            raise OpenWebUIRequestError("Open WebUI base URL is not configured")
        try:
            response = httpx.request(
                method=method,
                url=f"{self.base_url}{path}",
                headers=self._headers(),
                json=payload,
                timeout=12.0,
                follow_redirects=True,
            )
        except httpx.RequestError as exc:
            raise OpenWebUIRequestError(
                f"Open WebUI request failed: {exc.__class__.__name__}"
            ) from exc

        if response.status_code == 401:
            raise OpenWebUIAuthenticationError("Open WebUI authentication failed")
        if response.status_code == 404:
            raise OpenWebUIRequestError("Open WebUI endpoint not found")
        if response.status_code >= 400:
            raise OpenWebUIRequestError(self._extract_error_message(response))
        if not response.text.strip():
            return {}
        try:
            return response.json()
        except ValueError as exc:
            raise OpenWebUIRequestError("Open WebUI returned a non-JSON response") from exc

    def health(self) -> ToolHealth:
        return probe_http_tool(tool="openwebui", base_url=self.base_url)

    def list_models(self) -> list[OpenWebUIModelSummary]:
        payload = self._request(method="GET", path="/api/models")
        if isinstance(payload, dict):
            items = payload.get("data")
            if not isinstance(items, list):
                items = payload.get("models")
        else:
            items = payload
        if not isinstance(items, list):
            return []

        models: list[OpenWebUIModelSummary] = []
        for item in items:
            if not isinstance(item, dict):
                continue
            model_id = str(item.get("id") or "").strip()
            if not model_id:
                continue
            name = item.get("name")
            models.append(
                OpenWebUIModelSummary(
                    id=model_id,
                    name=str(name) if isinstance(name, str) else None,
                )
            )
        return models

    def chat(
        self,
        model: str,
        prompt: str,
        system_prompt: str | None = None,
        temperature: float | None = None,
        max_tokens: int | None = None,
    ) -> dict[str, Any]:
        messages: list[dict[str, str]] = []
        if system_prompt and system_prompt.strip():
            messages.append({"role": "system", "content": system_prompt.strip()})
        messages.append({"role": "user", "content": prompt})

        payload: dict[str, Any] = {
            "model": model,
            "messages": messages,
            "stream": False,
        }
        if temperature is not None:
            payload["temperature"] = temperature
        if max_tokens is not None:
            payload["max_tokens"] = max_tokens

        raw = self._request(method="POST", path="/api/chat/completions", payload=payload)
        answer = ""
        usage: dict[str, Any] | None = None
        if isinstance(raw, dict):
            choices = raw.get("choices")
            if isinstance(choices, list) and choices and isinstance(choices[0], dict):
                message = choices[0].get("message")
                if isinstance(message, dict):
                    content = message.get("content")
                    if isinstance(content, str):
                        answer = content
            usage_raw = raw.get("usage")
            if isinstance(usage_raw, dict):
                usage = usage_raw
        return {"model": model, "answer": answer, "usage": usage, "raw": raw}
