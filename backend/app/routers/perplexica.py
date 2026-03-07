from __future__ import annotations

from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, status

from app.adapters.obsidian import ObsidianConflictError, ObsidianPathError
from app.adapters.perplexica import (
    PerplexicaAdapterError,
    PerplexicaAuthenticationError,
    PerplexicaRequestError,
)
from app.dependencies import get_adapter_registry
from app.logging import log_action
from app.models.perplexica import (
    PerplexicaSearchRequest,
    PerplexicaSearchResponse,
    PerplexicaSearchToNoteRequest,
    PerplexicaSearchToNoteResponse,
)
from app.services.adapter_registry import AdapterRegistry

router = APIRouter(prefix="/api/v1/perplexica", tags=["perplexica"])


def _build_markdown(query: str, answer: str, sources: list[str]) -> str:
    timestamp = datetime.now(timezone.utc).isoformat()
    lines = [
        f"# Perplexica Research: {query}",
        "",
        f"- Generated at: {timestamp}",
        "",
        "## Answer",
        "",
        answer.strip() or "_No answer returned by Perplexica._",
        "",
        "## Sources",
        "",
    ]
    if not sources:
        lines.append("- No source URL returned")
    else:
        for source in sources:
            lines.append(f"- {source}")
    lines.append("")
    return "\n".join(lines)


@router.post("/search", response_model=PerplexicaSearchResponse)
def run_search(
    payload: PerplexicaSearchRequest,
    adapters: AdapterRegistry = Depends(get_adapter_registry),
) -> PerplexicaSearchResponse:
    try:
        result = adapters.perplexica.search(
            query=payload.query,
            focus_mode=payload.focus_mode,
            optimization_mode=payload.optimization_mode,
        )
    except PerplexicaAuthenticationError as exc:
        log_action("perplexica", "search", "error", {"reason": str(exc)})
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(exc)) from exc
    except PerplexicaRequestError as exc:
        log_action("perplexica", "search", "error", {"reason": str(exc)})
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=str(exc)) from exc
    except PerplexicaAdapterError as exc:
        log_action("perplexica", "search", "error", {"reason": str(exc)})
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc

    log_action(
        "perplexica",
        "search",
        "ok",
        {"query_length": len(payload.query), "source_count": len(result["sources"])},
    )
    return PerplexicaSearchResponse(
        query=result["query"],
        answer=result["answer"],
        sources=result["sources"],
        raw=result["raw"],
    )


@router.post("/search-to-note", response_model=PerplexicaSearchToNoteResponse, status_code=status.HTTP_201_CREATED)
def search_to_note(
    payload: PerplexicaSearchToNoteRequest,
    adapters: AdapterRegistry = Depends(get_adapter_registry),
) -> PerplexicaSearchToNoteResponse:
    try:
        result = adapters.perplexica.search(
            query=payload.query,
            focus_mode=payload.focus_mode,
            optimization_mode=payload.optimization_mode,
        )
    except PerplexicaAuthenticationError as exc:
        log_action("perplexica", "search_to_note", "error", {"reason": str(exc)})
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(exc)) from exc
    except PerplexicaRequestError as exc:
        log_action("perplexica", "search_to_note", "error", {"reason": str(exc)})
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=str(exc)) from exc
    except PerplexicaAdapterError as exc:
        log_action("perplexica", "search_to_note", "error", {"reason": str(exc)})
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc

    markdown = _build_markdown(
        query=result["query"],
        answer=result["answer"],
        sources=result["sources"],
    )

    try:
        write = adapters.obsidian.create_note(
            note_path=payload.note_path,
            content=markdown,
            create_parents=payload.create_parents,
        )
    except ObsidianPathError as exc:
        log_action(
            "perplexica",
            "search_to_note",
            "error",
            {"note_path": payload.note_path, "reason": str(exc)},
        )
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    except ObsidianConflictError as exc:
        log_action(
            "perplexica",
            "search_to_note",
            "error",
            {"note_path": payload.note_path, "reason": str(exc)},
        )
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc

    log_action(
        "perplexica",
        "search_to_note",
        "ok",
        {
            "note_path": payload.note_path,
            "source_count": len(result["sources"]),
            "bytes_written": write.bytes_written,
        },
    )
    return PerplexicaSearchToNoteResponse(
        query=result["query"],
        answer=result["answer"],
        sources=result["sources"],
        note_path=write.path,
        source_count=len(result["sources"]),
        bytes_written=write.bytes_written,
        modified_at=write.modified_at,
    )
