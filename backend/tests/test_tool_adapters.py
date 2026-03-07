from __future__ import annotations

from dataclasses import dataclass

from app.adapters.n8n import N8nAdapter
from app.adapters.openwebui import OpenWebUIAdapter
from app.adapters.perplexica import PerplexicaAdapter


@dataclass
class _FakeResponse:
    status_code: int
    payload: object
    text: str = "{}"

    def json(self):
        return self.payload


def test_n8n_list_workflows_parses_data(monkeypatch) -> None:
    def _fake_request(method, url, **kwargs):
        assert method == "GET"
        assert url.endswith("/api/v1/workflows")
        return _FakeResponse(
            status_code=200,
            payload={"data": [{"id": "wf_1", "name": "Import CRM", "active": True}]},
        )

    monkeypatch.setattr("app.adapters.n8n.httpx.request", _fake_request)

    adapter = N8nAdapter(base_url="http://localhost:5678", api_key="key")
    workflows = adapter.list_workflows(limit=10)

    assert len(workflows) == 1
    assert workflows[0].id == "wf_1"
    assert workflows[0].active is True


def test_perplexica_search_fallback_to_search_path(monkeypatch) -> None:
    calls: list[str] = []

    def _fake_post(url, **kwargs):
        calls.append(url)
        if url.endswith("/api/search"):
            return _FakeResponse(status_code=404, payload={"message": "not found"})
        return _FakeResponse(
            status_code=200,
            payload={"answer": "Result answer", "sources": [{"url": "https://example.com"}]},
        )

    monkeypatch.setattr("app.adapters.perplexica.httpx.post", _fake_post)

    adapter = PerplexicaAdapter(base_url="http://localhost:3001", api_key=None)
    result = adapter.search(query="test query")

    assert result["answer"] == "Result answer"
    assert result["sources"] == ["https://example.com"]
    assert calls[0].endswith("/api/search")
    assert calls[1].endswith("/search")


def test_openwebui_chat_parses_completion(monkeypatch) -> None:
    def _fake_request(method, url, **kwargs):
        assert method == "POST"
        assert url.endswith("/api/chat/completions")
        return _FakeResponse(
            status_code=200,
            payload={
                "choices": [{"message": {"content": "Hello from model"}}],
                "usage": {"prompt_tokens": 10, "completion_tokens": 4},
            },
        )

    monkeypatch.setattr("app.adapters.openwebui.httpx.request", _fake_request)

    adapter = OpenWebUIAdapter(base_url="http://localhost:3000", api_key="")
    result = adapter.chat(model="mistral", prompt="hello")

    assert result["answer"] == "Hello from model"
    assert result["usage"]["completion_tokens"] == 4
