from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class OpenWebUIModelSummary(BaseModel):
    id: str
    name: str | None = None


class OpenWebUIChatRequest(BaseModel):
    model: str = Field(min_length=1, max_length=200)
    prompt: str = Field(min_length=1, max_length=12000)
    system_prompt: str | None = Field(default=None, max_length=4000)
    temperature: float | None = Field(default=None, ge=0.0, le=2.0)
    max_tokens: int | None = Field(default=None, ge=1, le=8192)


class OpenWebUIChatResponse(BaseModel):
    model: str
    answer: str
    usage: dict[str, Any] | None = None


class OpenWebUIChatToNoteRequest(OpenWebUIChatRequest):
    note_path: str = Field(min_length=1, max_length=500)
    create_parents: bool = True


class OpenWebUIChatToNoteResponse(BaseModel):
    model: str
    note_path: str
    answer: str
    bytes_written: int
    modified_at: str
