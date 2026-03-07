from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query, status

from app.adapters.nocodb import (
    NocoDBAdapterError,
    NocoDBAuthenticationError,
    NocoDBNotFoundError,
    NocoDBRequestError,
)
from app.dependencies import get_adapter_registry
from app.logging import log_action
from app.models.nocodb import NocoDBBaseSummary, NocoDBRowsResponse, NocoDBTableSummary
from app.services.adapter_registry import AdapterRegistry

router = APIRouter(prefix="/api/v1/nocodb", tags=["nocodb"])


@router.get("/bases", response_model=list[NocoDBBaseSummary])
def list_bases(adapters: AdapterRegistry = Depends(get_adapter_registry)) -> list[NocoDBBaseSummary]:
    try:
        bases = adapters.nocodb.list_bases()
    except NocoDBAuthenticationError as exc:
        log_action("nocodb", "list_bases", "error", {"reason": str(exc)})
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(exc)) from exc
    except NocoDBRequestError as exc:
        log_action("nocodb", "list_bases", "error", {"reason": str(exc)})
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=str(exc)) from exc
    except NocoDBAdapterError as exc:
        log_action("nocodb", "list_bases", "error", {"reason": str(exc)})
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc

    log_action("nocodb", "list_bases", "ok", {"result_count": len(bases)})
    return bases


@router.get("/bases/{base_id}/tables", response_model=list[NocoDBTableSummary])
def list_tables(
    base_id: str,
    adapters: AdapterRegistry = Depends(get_adapter_registry),
) -> list[NocoDBTableSummary]:
    try:
        tables = adapters.nocodb.list_tables(base_id=base_id)
    except NocoDBAuthenticationError as exc:
        log_action("nocodb", "list_tables", "error", {"base_id": base_id, "reason": str(exc)})
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(exc)) from exc
    except NocoDBNotFoundError as exc:
        log_action("nocodb", "list_tables", "error", {"base_id": base_id, "reason": str(exc)})
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except NocoDBRequestError as exc:
        log_action("nocodb", "list_tables", "error", {"base_id": base_id, "reason": str(exc)})
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=str(exc)) from exc
    except NocoDBAdapterError as exc:
        log_action("nocodb", "list_tables", "error", {"base_id": base_id, "reason": str(exc)})
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc

    log_action("nocodb", "list_tables", "ok", {"base_id": base_id, "result_count": len(tables)})
    return tables


@router.get("/tables/{table_id}/rows", response_model=NocoDBRowsResponse)
def list_rows(
    table_id: str,
    base_id: str | None = Query(default=None, min_length=1, max_length=200),
    limit: int = Query(default=25, ge=1, le=200),
    offset: int = Query(default=0, ge=0),
    adapters: AdapterRegistry = Depends(get_adapter_registry),
) -> NocoDBRowsResponse:
    try:
        rows = adapters.nocodb.list_rows(
            table_id=table_id,
            base_id=base_id,
            limit=limit,
            offset=offset,
        )
    except NocoDBAuthenticationError as exc:
        log_action(
            "nocodb",
            "list_rows",
            "error",
            {"table_id": table_id, "base_id": base_id or "", "reason": str(exc)},
        )
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(exc)) from exc
    except NocoDBNotFoundError as exc:
        log_action(
            "nocodb",
            "list_rows",
            "error",
            {"table_id": table_id, "base_id": base_id or "", "reason": str(exc)},
        )
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except NocoDBRequestError as exc:
        log_action(
            "nocodb",
            "list_rows",
            "error",
            {"table_id": table_id, "base_id": base_id or "", "reason": str(exc)},
        )
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=str(exc)) from exc
    except NocoDBAdapterError as exc:
        log_action(
            "nocodb",
            "list_rows",
            "error",
            {"table_id": table_id, "base_id": base_id or "", "reason": str(exc)},
        )
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc

    log_action(
        "nocodb",
        "list_rows",
        "ok",
        {
            "table_id": table_id,
            "base_id": base_id or "",
            "row_count": rows.row_count,
            "limit": limit,
            "offset": offset,
        },
    )
    return rows
