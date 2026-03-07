from __future__ import annotations

from typing import Any

import httpx

from app.adapters.http_probe import probe_http_tool
from app.models.system import ToolHealth


class PerplexicaAdapterError(Exception):
    """Base class for Perplexica adapter errors."""


class PerplexicaAuthenticationError(PerplexicaAdapterError):
    """Raised when Perplexica authentication fails."""


class PerplexicaRequestError(PerplexicaAdapterError):
    """Raised for Perplexica upstream request failures."""


class PerplexicaAdapter:
    def __init__(self, base_url: str, api_key: str | None = None) -> None:
        self.base_url = base_url.rstrip("/")
        self.api_key = (api_key or "").strip()

    def _headers(self) -> dict[str, str]:
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        return headers

    @staticmethod
    def _extract_error_message(response: httpx.Response) -> str:
        try:
            payload = response.json()
        except ValueError:
            return (response.text or "Perplexica request failed").strip()
        if isinstance(payload, dict):
            for key in ("message", "error"):
                value = payload.get(key)
                if isinstance(value, str) and value.strip():
                    return value.strip()
        return "Perplexica request failed"

    def _search_request(self, path: str, payload: dict[str, Any]) -> dict[str, Any]:
        if not self.base_url:
            raise PerplexicaRequestError("Perplexica base URL is not configured")
        try:
            response = httpx.post(
                url=f"{self.base_url}{path}",
                headers=self._headers(),
                json=payload,
                timeout=12.0,
                follow_redirects=True,
            )
        except httpx.RequestError as exc:
            raise PerplexicaRequestError(
                f"Perplexica request failed: {exc.__class__.__name__}"
            ) from exc

        if response.status_code == 401:
            raise PerplexicaAuthenticationError("Perplexica authentication failed")
        if response.status_code == 404:
            raise PerplexicaRequestError("Perplexica search endpoint not found")
        if response.status_code >= 400:
            raise PerplexicaRequestError(self._extract_error_message(response))
        try:
            parsed = response.json()
        except ValueError as exc:
            raise PerplexicaRequestError("Perplexica returned a non-JSON response") from exc
        if not isinstance(parsed, dict):
            raise PerplexicaRequestError("Perplexica returned an unexpected payload shape")
        return parsed

    @staticmethod
    def _extract_answer(payload: dict[str, Any]) -> str:
        for key in ("answer", "message", "response"):
            value = payload.get(key)
            if isinstance(value, str) and value.strip():
                return value.strip()
        data = payload.get("data")
        if isinstance(data, dict):
            for key in ("answer", "message"):
                value = data.get(key)
                if isinstance(value, str) and value.strip():
                    return value.strip()
        return ""

    @staticmethod
    def _extract_sources(payload: dict[str, Any]) -> list[str]:
        source_items = payload.get("sources")
        if not isinstance(source_items, list):
            return []
        sources: list[str] = []
        for item in source_items:
            if isinstance(item, str) and item.strip():
                sources.append(item.strip())
                continue
            if isinstance(item, dict):
                for key in ("url", "link", "source"):
                    value = item.get(key)
                    if isinstance(value, str) and value.strip():
                        sources.append(value.strip())
                        break
        return sources

    def health(self) -> ToolHealth:
        return probe_http_tool(tool="perplexica", base_url=self.base_url)

    def search(
        self,
        query: str,
        focus_mode: str | None = None,
        optimization_mode: str | None = None,
    ) -> dict[str, Any]:
        payload: dict[str, Any] = {
            "query": query,
            "focusMode": focus_mode or "webSearch",
            "optimizationMode": optimization_mode or "speed",
            "history": [],
        }
        last_error: Exception | None = None
        for path in ("/api/search", "/search"):
            try:
                raw = self._search_request(path=path, payload=payload)
                return {
                    "query": query,
                    "answer": self._extract_answer(raw),
                    "sources": self._extract_sources(raw),
                    "raw": raw,
                }
            except PerplexicaRequestError as exc:
                last_error = exc
                continue
        if last_error is not None:
            raise last_error
        raise PerplexicaRequestError("Perplexica search endpoint is not available")
