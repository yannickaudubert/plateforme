from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

import httpx

from app.models.nocodb import NocoDBBaseSummary, NocoDBRowsResponse, NocoDBTableSummary
from app.models.system import ToolHealth


class NocoDBAdapterError(Exception):
    """Base class for adapter-level NocoDB errors."""


class NocoDBAuthenticationError(NocoDBAdapterError):
    """Raised when NocoDB authentication is missing or invalid."""


class NocoDBNotFoundError(NocoDBAdapterError):
    """Raised when requested base/table data is not found."""


class NocoDBEndpointNotAvailableError(NocoDBAdapterError):
    """Raised when an endpoint is not available on current NocoDB version."""


class NocoDBRequestError(NocoDBAdapterError):
    """Raised for upstream NocoDB errors."""


class NocoDBAdapter:
    def __init__(self, base_url: str, api_token: str | None = None) -> None:
        self.base_url = base_url.rstrip("/")
        self.api_token = (api_token or "").strip()

    def _headers(self) -> dict[str, str]:
        if not self.api_token:
            return {}
        return {
            "xc-token": self.api_token,
            "Authorization": f"Bearer {self.api_token}",
        }

    @staticmethod
    def _extract_error_message(response: httpx.Response) -> str:
        try:
            payload = response.json()
        except ValueError:
            return (response.text or "NocoDB request failed").strip()

        if isinstance(payload, dict):
            for key in ("message", "msg", "error"):
                value = payload.get(key)
                if isinstance(value, str) and value.strip():
                    return value.strip()
        return "NocoDB request failed"

    def _api_get(
        self,
        path: str,
        params: dict[str, Any] | None = None,
    ) -> Any:
        if not self.base_url:
            raise NocoDBRequestError("NocoDB base URL is not configured")
        if not self.api_token:
            raise NocoDBAuthenticationError("NocoDB API token is required for read operations")

        url = f"{self.base_url}{path}"
        try:
            response = httpx.get(
                url,
                headers=self._headers(),
                params=params,
                timeout=8.0,
                follow_redirects=True,
            )
        except httpx.RequestError as exc:
            raise NocoDBRequestError(f"NocoDB request failed: {exc.__class__.__name__}") from exc

        if response.status_code == 401:
            raise NocoDBAuthenticationError("NocoDB authentication failed (invalid token)")
        if response.status_code == 404:
            detail = self._extract_error_message(response)
            if detail.lower().startswith("cannot get"):
                raise NocoDBEndpointNotAvailableError(detail)
            raise NocoDBNotFoundError(detail)
        if response.status_code >= 400:
            raise NocoDBRequestError(self._extract_error_message(response))

        try:
            return response.json()
        except ValueError as exc:
            raise NocoDBRequestError("NocoDB returned a non-JSON response") from exc

    def _request_with_fallback(
        self,
        paths: list[str],
        params: dict[str, Any] | None = None,
    ) -> Any:
        last_error: Exception | None = None
        for path in paths:
            try:
                return self._api_get(path=path, params=params)
            except NocoDBEndpointNotAvailableError as exc:
                last_error = exc
                continue
        if last_error is not None:
            raise last_error
        raise NocoDBRequestError("No endpoint path available for this request")

    @staticmethod
    def _extract_list(payload: Any) -> list[dict[str, Any]]:
        if isinstance(payload, list):
            return [item for item in payload if isinstance(item, dict)]
        if isinstance(payload, dict):
            for key in ("list", "rows", "data"):
                value = payload.get(key)
                if isinstance(value, list):
                    return [item for item in value if isinstance(item, dict)]
        return []

    @staticmethod
    def _pick_id(item: dict[str, Any]) -> str:
        for key in ("id", "base_id", "table_id", "uuid"):
            value = item.get(key)
            if value is not None:
                return str(value)
        return ""

    @staticmethod
    def _pick_title(item: dict[str, Any]) -> str:
        for key in ("title", "name", "table_name"):
            value = item.get(key)
            if isinstance(value, str) and value.strip():
                return value.strip()
        return ""

    def health(self) -> ToolHealth:
        checked_at = datetime.now(timezone.utc).isoformat()
        if not self.base_url:
            return ToolHealth(
                tool="nocodb",
                status="degraded",
                message="NocoDB base URL not configured",
                checked_at=checked_at,
            )
        if not self.api_token:
            return ToolHealth(
                tool="nocodb",
                status="degraded",
                message="NocoDB token missing (read endpoints require NOCODB_API_TOKEN)",
                checked_at=checked_at,
            )
        try:
            self._request_with_fallback(paths=["/api/v2/meta/bases", "/api/v1/db/meta/projects"])
        except NocoDBAuthenticationError:
            return ToolHealth(
                tool="nocodb",
                status="degraded",
                message="NocoDB token rejected",
                checked_at=checked_at,
            )
        except NocoDBAdapterError as exc:
            return ToolHealth(
                tool="nocodb",
                status="degraded",
                message=str(exc),
                checked_at=checked_at,
            )
        return ToolHealth(
            tool="nocodb",
            status="ok",
            message=f"NocoDB API reachable at {self.base_url}",
            checked_at=checked_at,
        )

    def list_bases(self) -> list[NocoDBBaseSummary]:
        payload = self._request_with_fallback(paths=["/api/v2/meta/bases", "/api/v1/db/meta/projects"])
        items = self._extract_list(payload)
        bases: list[NocoDBBaseSummary] = []
        for item in items:
            base_id = self._pick_id(item)
            if not base_id:
                continue
            title = self._pick_title(item) or base_id
            bases.append(
                NocoDBBaseSummary(
                    id=base_id,
                    title=title,
                    type=str(item.get("type")) if item.get("type") is not None else None,
                )
            )
        return bases

    def list_tables(self, base_id: str) -> list[NocoDBTableSummary]:
        payload = self._request_with_fallback(
            paths=[
                f"/api/v2/meta/bases/{base_id}/tables",
                f"/api/v1/db/meta/projects/{base_id}/tables",
            ]
        )
        items = self._extract_list(payload)
        tables: list[NocoDBTableSummary] = []
        for item in items:
            table_id = self._pick_id(item)
            if not table_id:
                continue
            title = self._pick_title(item) or table_id
            tables.append(
                NocoDBTableSummary(
                    id=table_id,
                    title=title,
                    base_id=base_id,
                    type=str(item.get("type")) if item.get("type") is not None else None,
                )
            )
        return tables

    def list_rows(
        self,
        table_id: str,
        base_id: str | None = None,
        limit: int = 25,
        offset: int = 0,
    ) -> NocoDBRowsResponse:
        paths = [f"/api/v2/tables/{table_id}/records"]
        if base_id:
            paths.append(f"/api/v1/db/data/v1/{base_id}/{table_id}")

        payload = self._request_with_fallback(
            paths=paths,
            params={"limit": limit, "offset": offset},
        )
        rows = self._extract_list(payload)

        total_rows: int | None = None
        if isinstance(payload, dict):
            page_info = payload.get("pageInfo")
            if isinstance(page_info, dict):
                total = page_info.get("totalRows")
                if isinstance(total, int):
                    total_rows = total
            if total_rows is None and isinstance(payload.get("totalRows"), int):
                total_rows = int(payload["totalRows"])

        return NocoDBRowsResponse(
            table_id=table_id,
            base_id=base_id,
            row_count=len(rows),
            total_rows=total_rows,
            rows=rows,
        )
