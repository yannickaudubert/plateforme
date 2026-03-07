from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

import httpx

from app.adapters.http_probe import probe_http_tool
from app.models.n8n import N8nExecutionSummary, N8nWorkflowSummary
from app.models.system import ToolHealth


class N8nAdapterError(Exception):
    """Base class for n8n adapter errors."""


class N8nAuthenticationError(N8nAdapterError):
    """Raised when n8n API authentication fails."""


class N8nNotFoundError(N8nAdapterError):
    """Raised when n8n resource does not exist."""


class N8nRequestError(N8nAdapterError):
    """Raised for n8n upstream request errors."""


class N8nAdapter:
    def __init__(self, base_url: str, api_key: str | None = None) -> None:
        self.base_url = base_url.rstrip("/")
        self.api_key = (api_key or "").strip()

    def _headers(self) -> dict[str, str]:
        headers: dict[str, str] = {}
        if self.api_key:
            headers["X-N8N-API-KEY"] = self.api_key
        return headers

    @staticmethod
    def _extract_error_message(response: httpx.Response) -> str:
        try:
            payload = response.json()
        except ValueError:
            return (response.text or "n8n request failed").strip()
        if isinstance(payload, dict):
            for key in ("message", "error"):
                value = payload.get(key)
                if isinstance(value, str) and value.strip():
                    return value.strip()
        return "n8n request failed"

    def _request(
        self,
        method: str,
        path: str,
        params: dict[str, Any] | None = None,
        payload: dict[str, Any] | None = None,
        require_api_key: bool = True,
    ) -> Any:
        if not self.base_url:
            raise N8nRequestError("n8n base URL is not configured")
        if require_api_key and not self.api_key:
            raise N8nAuthenticationError("N8N_API_KEY is required for this operation")

        try:
            response = httpx.request(
                method=method,
                url=f"{self.base_url}{path}",
                headers=self._headers(),
                params=params,
                json=payload,
                timeout=8.0,
                follow_redirects=True,
            )
        except httpx.RequestError as exc:
            raise N8nRequestError(f"n8n request failed: {exc.__class__.__name__}") from exc

        if response.status_code == 401:
            raise N8nAuthenticationError("n8n authentication failed (invalid API key)")
        if response.status_code == 404:
            raise N8nNotFoundError(self._extract_error_message(response))
        if response.status_code >= 400:
            raise N8nRequestError(self._extract_error_message(response))

        if not response.text.strip():
            return {}
        try:
            return response.json()
        except ValueError:
            return {"message": response.text.strip()}

    @staticmethod
    def _extract_list(payload: Any) -> list[dict[str, Any]]:
        if isinstance(payload, list):
            return [item for item in payload if isinstance(item, dict)]
        if isinstance(payload, dict):
            for key in ("data", "items", "list"):
                value = payload.get(key)
                if isinstance(value, list):
                    return [item for item in value if isinstance(item, dict)]
        return []

    def health(self) -> ToolHealth:
        checked_at = datetime.now(timezone.utc).isoformat()
        probe = probe_http_tool(tool="n8n", base_url=self.base_url)
        if probe.status != "ok":
            return probe
        if not self.api_key:
            return ToolHealth(
                tool="n8n",
                status="degraded",
                message="n8n reachable but N8N_API_KEY is missing for workflow controls",
                checked_at=checked_at,
            )
        return ToolHealth(
            tool="n8n",
            status="ok",
            message=f"n8n API reachable at {self.base_url}",
            checked_at=checked_at,
        )

    def list_workflows(self, limit: int = 25) -> list[N8nWorkflowSummary]:
        payload = self._request(
            method="GET",
            path="/api/v1/workflows",
            params={"limit": limit},
        )
        workflows: list[N8nWorkflowSummary] = []
        for item in self._extract_list(payload):
            workflow_id = str(item.get("id") or "").strip()
            if not workflow_id:
                continue
            name = str(item.get("name") or workflow_id)
            workflows.append(
                N8nWorkflowSummary(
                    id=workflow_id,
                    name=name,
                    active=bool(item.get("active")),
                    updated_at=item.get("updatedAt"),
                )
            )
        return workflows

    def list_executions(self, limit: int = 25) -> list[N8nExecutionSummary]:
        payload = self._request(
            method="GET",
            path="/api/v1/executions",
            params={"limit": limit},
        )
        executions: list[N8nExecutionSummary] = []
        for item in self._extract_list(payload):
            execution_id = str(item.get("id") or "").strip()
            if not execution_id:
                continue
            executions.append(
                N8nExecutionSummary(
                    id=execution_id,
                    workflow_id=str(item.get("workflowId")) if item.get("workflowId") is not None else None,
                    status=str(item.get("status") or "unknown"),
                    mode=str(item.get("mode")) if item.get("mode") is not None else None,
                    started_at=item.get("startedAt"),
                    stopped_at=item.get("stoppedAt"),
                )
            )
        return executions

    def activate_workflow(self, workflow_id: str) -> None:
        self._request(
            method="POST",
            path=f"/api/v1/workflows/{workflow_id}/activate",
            require_api_key=True,
        )

    def deactivate_workflow(self, workflow_id: str) -> None:
        self._request(
            method="POST",
            path=f"/api/v1/workflows/{workflow_id}/deactivate",
            require_api_key=True,
        )
