from fastapi import APIRouter, Depends, Query

from app.dependencies import get_adapter_registry
from app.logging import log_action
from app.services.adapter_registry import AdapterRegistry

router = APIRouter(prefix="/api/v1/obsidian", tags=["obsidian"])


@router.get("/notes", response_model=list[str])
def list_notes(
    limit: int = Query(default=20, ge=1, le=200),
    adapters: AdapterRegistry = Depends(get_adapter_registry),
) -> list[str]:
    notes = adapters.obsidian.list_markdown_files(limit=limit)
    log_action(
        tool="obsidian",
        action="list_notes",
        status="ok",
        details={"limit": limit, "result_count": len(notes)},
    )
    return notes
