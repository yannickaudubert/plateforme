from __future__ import annotations

from dataclasses import dataclass

import pytest

from app.adapters.nocodb import (
    NocoDBAdapter,
    NocoDBAuthenticationError,
)


@dataclass
class _FakeResponse:
    status_code: int
    payload: object
    text: str = ""

    def json(self):
        return self.payload


def test_list_bases_falls_back_from_v2_to_v1(monkeypatch) -> None:
    calls: list[str] = []

    def _fake_get(url, **kwargs):
        calls.append(url)
        if url.endswith("/api/v2/meta/bases"):
            return _FakeResponse(status_code=404, payload={"msg": "Cannot GET /api/v2/meta/bases"})
        return _FakeResponse(
            status_code=200,
            payload={"list": [{"id": "base-main", "title": "Main Base", "type": "database"}]},
        )

    monkeypatch.setattr("app.adapters.nocodb.httpx.get", _fake_get)

    adapter = NocoDBAdapter(base_url="http://localhost:8080", api_token="token")
    bases = adapter.list_bases()

    assert [item.id for item in bases] == ["base-main"]
    assert calls[0].endswith("/api/v2/meta/bases")
    assert calls[1].endswith("/api/v1/db/meta/projects")


def test_list_rows_requires_token() -> None:
    adapter = NocoDBAdapter(base_url="http://localhost:8080", api_token=None)
    with pytest.raises(NocoDBAuthenticationError):
        adapter.list_rows(table_id="tbl_123")


def test_list_rows_parses_page_info(monkeypatch) -> None:
    def _fake_get(url, **kwargs):
        assert url.endswith("/api/v2/tables/tbl_123/records")
        return _FakeResponse(
            status_code=200,
            payload={
                "list": [{"Id": 1, "Name": "Alpha"}, {"Id": 2, "Name": "Beta"}],
                "pageInfo": {"totalRows": 2},
            },
        )

    monkeypatch.setattr("app.adapters.nocodb.httpx.get", _fake_get)

    adapter = NocoDBAdapter(base_url="http://localhost:8080", api_token="token")
    rows = adapter.list_rows(table_id="tbl_123", limit=25, offset=0)

    assert rows.row_count == 2
    assert rows.total_rows == 2
    assert rows.rows[0]["Name"] == "Alpha"


def test_create_row_falls_back_from_v2_to_v1(monkeypatch) -> None:
    calls: list[tuple[str, str]] = []

    def _fake_request(method, url, **kwargs):
        calls.append((method, url))
        if url.endswith("/api/v2/tables/tbl_123/records"):
            return _FakeResponse(status_code=404, payload={"msg": "Cannot POST /api/v2/tables/tbl_123/records"})
        return _FakeResponse(status_code=200, payload={"Id": 99, "Name": "Gamma"})

    monkeypatch.setattr("app.adapters.nocodb.httpx.request", _fake_request)

    adapter = NocoDBAdapter(base_url="http://localhost:8080", api_token="token")
    row = adapter.create_row(table_id="tbl_123", data={"Name": "Gamma"}, base_id="base_main")

    assert row["Name"] == "Gamma"
    assert calls[0][0] == "POST"
    assert calls[0][1].endswith("/api/v2/tables/tbl_123/records")
    assert calls[-1][1].endswith("/api/v1/db/data/v1/base_main/tbl_123")


def test_update_row_requires_token() -> None:
    adapter = NocoDBAdapter(base_url="http://localhost:8080", api_token=None)
    with pytest.raises(NocoDBAuthenticationError):
        adapter.update_row(table_id="tbl_123", row_id="1", data={"Name": "Delta"})
