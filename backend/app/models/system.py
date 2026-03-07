from pydantic import BaseModel


class ToolHealth(BaseModel):
    tool: str
    status: str
    message: str
    checked_at: str


class ActionLogEntry(BaseModel):
    timestamp: str
    tool: str
    action: str
    status: str
    details: dict[str, object]


class SystemStatusResponse(BaseModel):
    environment: str
    tools: list[ToolHealth]
    recent_actions: list[ActionLogEntry]


class AdminOverviewResponse(BaseModel):
    app_name: str
    environment: str
    config_file: str
    obsidian_vault_path: str
    obsidian_allowed_roots: list[str]
    tools: dict[str, str]
    secrets: dict[str, bool]
