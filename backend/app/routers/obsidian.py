from fastapi import APIRouter, Depends, HTTPException, Query, status

from app.adapters.obsidian import (
    ObsidianConflictError,
    ObsidianNotFoundError,
    ObsidianPreconditionError,
    ObsidianPathError,
)
from app.dependencies import get_adapter_registry
from app.logging import log_action
from app.models.obsidian import (
    ObsidianCreateNoteRequest,
    ObsidianNoteContent,
    ObsidianUpdateNoteRequest,
    ObsidianWriteResponse,
)
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


@router.get("/note", response_model=ObsidianNoteContent)
def get_note(
    path: str = Query(min_length=1, max_length=500),
    adapters: AdapterRegistry = Depends(get_adapter_registry),
) -> ObsidianNoteContent:
    try:
        note = adapters.obsidian.read_note(path)
    except ObsidianPathError as exc:
        log_action(
            tool="obsidian",
            action="read_note",
            status="error",
            details={"path": path, "reason": str(exc)},
        )
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    except ObsidianNotFoundError as exc:
        log_action(
            tool="obsidian",
            action="read_note",
            status="error",
            details={"path": path, "reason": str(exc)},
        )
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc

    log_action(
        tool="obsidian",
        action="read_note",
        status="ok",
        details={"path": note.path, "bytes_read": len(note.content.encode("utf-8"))},
    )
    return note


@router.post("/note", response_model=ObsidianWriteResponse, status_code=status.HTTP_201_CREATED)
def create_note(
    payload: ObsidianCreateNoteRequest,
    adapters: AdapterRegistry = Depends(get_adapter_registry),
) -> ObsidianWriteResponse:
    try:
        result = adapters.obsidian.create_note(
            note_path=payload.path,
            content=payload.content,
            create_parents=payload.create_parents,
        )
    except ObsidianPathError as exc:
        log_action(
            tool="obsidian",
            action="create_note",
            status="error",
            details={"path": payload.path, "reason": str(exc)},
        )
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    except ObsidianConflictError as exc:
        log_action(
            tool="obsidian",
            action="create_note",
            status="error",
            details={"path": payload.path, "reason": str(exc)},
        )
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc

    log_action(
        tool="obsidian",
        action="create_note",
        status="ok",
        details={"path": result.path, "bytes_written": result.bytes_written},
    )
    return result


@router.put("/note", response_model=ObsidianWriteResponse)
def update_note(
    payload: ObsidianUpdateNoteRequest,
    adapters: AdapterRegistry = Depends(get_adapter_registry),
) -> ObsidianWriteResponse:
    try:
        result = adapters.obsidian.update_note(
            note_path=payload.path,
            content=payload.content,
            expected_modified_at=payload.expected_modified_at,
            create_backup=payload.create_backup,
        )
    except ObsidianPathError as exc:
        log_action(
            tool="obsidian",
            action="update_note",
            status="error",
            details={"path": payload.path, "reason": str(exc)},
        )
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    except ObsidianNotFoundError as exc:
        log_action(
            tool="obsidian",
            action="update_note",
            status="error",
            details={"path": payload.path, "reason": str(exc)},
        )
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except ObsidianPreconditionError as exc:
        log_action(
            tool="obsidian",
            action="update_note",
            status="error",
            details={"path": payload.path, "reason": str(exc)},
        )
        raise HTTPException(status_code=status.HTTP_412_PRECONDITION_FAILED, detail=str(exc)) from exc

    log_action(
        tool="obsidian",
        action="update_note",
        status="ok",
        details={"path": result.path, "bytes_written": result.bytes_written},
    )
    return result
