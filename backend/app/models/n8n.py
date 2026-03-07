from __future__ import annotations

from pydantic import BaseModel, Field


class N8nWorkflowSummary(BaseModel):
    id: str
    name: str
    active: bool
    updated_at: str | None = None


class N8nExecutionSummary(BaseModel):
    id: str
    workflow_id: str | None = None
    status: str
    mode: str | None = None
    started_at: str | None = None
    stopped_at: str | None = None


class N8nWorkflowActionRequest(BaseModel):
    confirm: bool = False


class N8nWorkflowActionResponse(BaseModel):
    workflow_id: str
    action: str
    status: str
    message: str


class N8nListQuery(BaseModel):
    limit: int = Field(default=25, ge=1, le=200)
