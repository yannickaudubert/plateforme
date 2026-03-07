from __future__ import annotations

from dataclasses import dataclass

import httpx

from app.adapters import http_probe


@dataclass
class _FakeResponse:
    status_code: int


def test_probe_http_tool_marks_5xx_as_degraded(monkeypatch) -> None:
    monkeypatch.setattr(http_probe.httpx, "get", lambda *args, **kwargs: _FakeResponse(503))
    health = http_probe.probe_http_tool("nocodb", "http://example.local-1")
    assert health.status == "degraded"
    assert "HTTP 503" in health.message


def test_probe_http_tool_marks_2xx_as_ok(monkeypatch) -> None:
    monkeypatch.setattr(http_probe.httpx, "get", lambda *args, **kwargs: _FakeResponse(200))
    health = http_probe.probe_http_tool("n8n", "http://example.local-2")
    assert health.status == "ok"


def test_probe_http_tool_handles_unreachable(monkeypatch) -> None:
    def _raise(*args, **kwargs):
        raise httpx.ConnectError("offline")

    monkeypatch.setattr(http_probe.httpx, "get", _raise)
    health = http_probe.probe_http_tool("perplexica", "http://example.local-3")
    assert health.status == "degraded"
    assert "unreachable" in health.message
