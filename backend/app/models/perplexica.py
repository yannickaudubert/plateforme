from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class PerplexicaSearchRequest(BaseModel):
    query: str = Field(min_length=2, max_length=2000)
    focus_mode: str | None = Field(default=None, max_length=100)
    optimization_mode: str | None = Field(default=None, max_length=100)


class PerplexicaSearchResponse(BaseModel):
    query: str
    answer: str
    sources: list[str]
    raw: dict[str, Any]


class PerplexicaSearchToNoteRequest(PerplexicaSearchRequest):
    note_path: str = Field(min_length=1, max_length=500)
    create_parents: bool = True


class PerplexicaSearchToNoteResponse(BaseModel):
    query: str
    answer: str
    sources: list[str]
    note_path: str
    source_count: int
    bytes_written: int
    modified_at: str
