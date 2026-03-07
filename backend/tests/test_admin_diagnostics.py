from __future__ import annotations

from fastapi.testclient import TestClient

from app.dependencies import get_status_service
from app.main import app
from app.models.system import SystemStatusResponse, ToolHealth


class _FakeStatusService:
    def system_status(self) -> SystemStatusResponse:
        return SystemStatusResponse(
            environment="test",
            tools=[
                ToolHealth(
                    tool="obsidian",
                    status="ok",
                    message="ok",
                    checked_at="2026-01-01T00:00:00+00:00",
                ),
                ToolHealth(
                    tool="nocodb",
                    status="degraded",
                    message="token missing",
                    checked_at="2026-01-01T00:00:00+00:00",
                ),
            ],
            recent_actions=[],
        )


def test_admin_diagnostics_contract() -> None:
    app.dependency_overrides[get_status_service] = lambda: _FakeStatusService()
    try:
        client = TestClient(app)
        response = client.get("/api/v1/admin/diagnostics")
        assert response.status_code == 200
        payload = response.json()
        assert "generated_at" in payload
        assert "files" in payload
        assert "paths" in payload
        assert "path_checks" in payload
        assert "tool_health" in payload
        assert "recommendations" in payload
        assert isinstance(payload["tool_health"], list)
    finally:
        app.dependency_overrides.clear()
