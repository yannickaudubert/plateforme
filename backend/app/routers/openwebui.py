from __future__ import annotations

from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, status

from app.adapters.obsidian import ObsidianConflictError, ObsidianPathError
from app.adapters.openwebui import (
    OpenWebUIAdapterError,
    OpenWebUIAuthenticationError,
    OpenWebUIRequestError,
)
from app.dependencies import get_adapter_registry
from app.logging import log_action
from app.models.openwebui import (
    OpenWebUIChatRequest,
    OpenWebUIChatResponse,
    OpenWebUIChatToNoteRequest,
    OpenWebUIChatToNoteResponse,
    OpenWebUIModelSummary,
)
from app.services.adapter_registry import AdapterRegistry

router = APIRouter(prefix="/api/v1/openwebui", tags=["openwebui"])


def _chat_markdown(model: str, prompt: str, answer: str) -> str:
    timestamp = datetime.now(timezone.utc).isoformat()
    return "\n".join(
        [
            f"# Open WebUI Chat ({model})",
            "",
            f"- Generated at: {timestamp}",
            "",
            "## Prompt",
            "",
            prompt.strip(),
            "",
            "## Answer",
            "",
            answer.strip() or "_No answer returned by model._",
            "",
        ]
    )


@router.get("/models", response_model=list[OpenWebUIModelSummary])
def list_models(adapters: AdapterRegistry = Depends(get_adapter_registry)) -> list[OpenWebUIModelSummary]:
    try:
        models = adapters.openwebui.list_models()
    except OpenWebUIAuthenticationError as exc:
        log_action("openwebui", "list_models", "error", {"reason": str(exc)})
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(exc)) from exc
    except OpenWebUIRequestError as exc:
        log_action("openwebui", "list_models", "error", {"reason": str(exc)})
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=str(exc)) from exc
    except OpenWebUIAdapterError as exc:
        log_action("openwebui", "list_models", "error", {"reason": str(exc)})
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc

    log_action("openwebui", "list_models", "ok", {"result_count": len(models)})
    return models


@router.post("/chat", response_model=OpenWebUIChatResponse)
def run_chat(
    payload: OpenWebUIChatRequest,
    adapters: AdapterRegistry = Depends(get_adapter_registry),
) -> OpenWebUIChatResponse:
    try:
        result = adapters.openwebui.chat(
            model=payload.model,
            prompt=payload.prompt,
            system_prompt=payload.system_prompt,
            temperature=payload.temperature,
            max_tokens=payload.max_tokens,
        )
    except OpenWebUIAuthenticationError as exc:
        log_action("openwebui", "chat", "error", {"reason": str(exc)})
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(exc)) from exc
    except OpenWebUIRequestError as exc:
        log_action("openwebui", "chat", "error", {"reason": str(exc)})
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=str(exc)) from exc
    except OpenWebUIAdapterError as exc:
        log_action("openwebui", "chat", "error", {"reason": str(exc)})
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc

    log_action("openwebui", "chat", "ok", {"model": payload.model, "prompt_length": len(payload.prompt)})
    return OpenWebUIChatResponse(
        model=result["model"],
        answer=result["answer"],
        usage=result["usage"],
    )


@router.post("/chat-to-note", response_model=OpenWebUIChatToNoteResponse, status_code=status.HTTP_201_CREATED)
def chat_to_note(
    payload: OpenWebUIChatToNoteRequest,
    adapters: AdapterRegistry = Depends(get_adapter_registry),
) -> OpenWebUIChatToNoteResponse:
    try:
        result = adapters.openwebui.chat(
            model=payload.model,
            prompt=payload.prompt,
            system_prompt=payload.system_prompt,
            temperature=payload.temperature,
            max_tokens=payload.max_tokens,
        )
    except OpenWebUIAuthenticationError as exc:
        log_action("openwebui", "chat_to_note", "error", {"reason": str(exc)})
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(exc)) from exc
    except OpenWebUIRequestError as exc:
        log_action("openwebui", "chat_to_note", "error", {"reason": str(exc)})
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=str(exc)) from exc
    except OpenWebUIAdapterError as exc:
        log_action("openwebui", "chat_to_note", "error", {"reason": str(exc)})
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc

    markdown = _chat_markdown(
        model=result["model"],
        prompt=payload.prompt,
        answer=result["answer"],
    )
    try:
        write = adapters.obsidian.create_note(
            note_path=payload.note_path,
            content=markdown,
            create_parents=payload.create_parents,
        )
    except ObsidianPathError as exc:
        log_action("openwebui", "chat_to_note", "error", {"note_path": payload.note_path, "reason": str(exc)})
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    except ObsidianConflictError as exc:
        log_action("openwebui", "chat_to_note", "error", {"note_path": payload.note_path, "reason": str(exc)})
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc

    log_action(
        "openwebui",
        "chat_to_note",
        "ok",
        {
            "model": payload.model,
            "note_path": payload.note_path,
            "bytes_written": write.bytes_written,
        },
    )
    return OpenWebUIChatToNoteResponse(
        model=result["model"],
        note_path=write.path,
        answer=result["answer"],
        bytes_written=write.bytes_written,
        modified_at=write.modified_at,
    )
