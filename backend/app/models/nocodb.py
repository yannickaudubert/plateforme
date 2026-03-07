from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


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


class NocoDBRowWriteRequest(BaseModel):
    base_id: str | None = Field(default=None, min_length=1, max_length=200)
    data: dict[str, Any] = Field(default_factory=dict)
    confirm_write: bool = False


class NocoDBRowMutationResponse(BaseModel):
    table_id: str
    base_id: str | None = None
    operation: str
    row: dict[str, Any]
