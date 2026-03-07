from __future__ import annotations

from typing import Any

from pydantic import BaseModel


class NocoDBBaseSummary(BaseModel):
    id: str
    title: str
    type: str | None = None


class NocoDBTableSummary(BaseModel):
    id: str
    title: str
    base_id: str
    type: str | None = None


class NocoDBRowsResponse(BaseModel):
    table_id: str
    base_id: str | None = None
    row_count: int
    total_rows: int | None = None
    rows: list[dict[str, Any]]
