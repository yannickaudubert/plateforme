from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query, status

from app.adapters.n8n import (
    N8nAdapterError,
    N8nAuthenticationError,
    N8nNotFoundError,
    N8nRequestError,
)
from app.dependencies import get_adapter_registry
from app.logging import log_action
from app.models.n8n import (
    N8nExecutionSummary,
    N8nWorkflowActionRequest,
    N8nWorkflowActionResponse,
    N8nWorkflowSummary,
)
from app.services.adapter_registry import AdapterRegistry

router = APIRouter(prefix="/api/v1/n8n", tags=["n8n"])


def _require_confirmation(payload: N8nWorkflowActionRequest, action: str) -> None:
    if not payload.confirm:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"confirm must be true to {action} a workflow",
        )


@router.get("/workflows", response_model=list[N8nWorkflowSummary])
def list_workflows(
    limit: int = Query(default=25, ge=1, le=200),
    adapters: AdapterRegistry = Depends(get_adapter_registry),
) -> list[N8nWorkflowSummary]:
    try:
        workflows = adapters.n8n.list_workflows(limit=limit)
    except N8nAuthenticationError as exc:
        log_action("n8n", "list_workflows", "error", {"reason": str(exc)})
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(exc)) from exc
    except N8nRequestError as exc:
        log_action("n8n", "list_workflows", "error", {"reason": str(exc)})
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=str(exc)) from exc
    except N8nAdapterError as exc:
        log_action("n8n", "list_workflows", "error", {"reason": str(exc)})
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc

    log_action("n8n", "list_workflows", "ok", {"limit": limit, "result_count": len(workflows)})
    return workflows


@router.get("/executions", response_model=list[N8nExecutionSummary])
def list_executions(
    limit: int = Query(default=25, ge=1, le=200),
    adapters: AdapterRegistry = Depends(get_adapter_registry),
) -> list[N8nExecutionSummary]:
    try:
        executions = adapters.n8n.list_executions(limit=limit)
    except N8nAuthenticationError as exc:
        log_action("n8n", "list_executions", "error", {"reason": str(exc)})
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(exc)) from exc
    except N8nRequestError as exc:
        log_action("n8n", "list_executions", "error", {"reason": str(exc)})
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=str(exc)) from exc
    except N8nAdapterError as exc:
        log_action("n8n", "list_executions", "error", {"reason": str(exc)})
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc

    log_action("n8n", "list_executions", "ok", {"limit": limit, "result_count": len(executions)})
    return executions


@router.post("/workflows/{workflow_id}/activate", response_model=N8nWorkflowActionResponse)
def activate_workflow(
    workflow_id: str,
    payload: N8nWorkflowActionRequest,
    adapters: AdapterRegistry = Depends(get_adapter_registry),
) -> N8nWorkflowActionResponse:
    _require_confirmation(payload=payload, action="activate")

    try:
        adapters.n8n.activate_workflow(workflow_id=workflow_id)
    except N8nAuthenticationError as exc:
        log_action("n8n", "activate_workflow", "error", {"workflow_id": workflow_id, "reason": str(exc)})
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(exc)) from exc
    except N8nNotFoundError as exc:
        log_action("n8n", "activate_workflow", "error", {"workflow_id": workflow_id, "reason": str(exc)})
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except N8nRequestError as exc:
        log_action("n8n", "activate_workflow", "error", {"workflow_id": workflow_id, "reason": str(exc)})
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=str(exc)) from exc
    except N8nAdapterError as exc:
        log_action("n8n", "activate_workflow", "error", {"workflow_id": workflow_id, "reason": str(exc)})
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc

    log_action("n8n", "activate_workflow", "ok", {"workflow_id": workflow_id})
    return N8nWorkflowActionResponse(
        workflow_id=workflow_id,
        action="activate",
        status="ok",
        message="Workflow activation command sent",
    )


@router.post("/workflows/{workflow_id}/deactivate", response_model=N8nWorkflowActionResponse)
def deactivate_workflow(
    workflow_id: str,
    payload: N8nWorkflowActionRequest,
    adapters: AdapterRegistry = Depends(get_adapter_registry),
) -> N8nWorkflowActionResponse:
    _require_confirmation(payload=payload, action="deactivate")

    try:
        adapters.n8n.deactivate_workflow(workflow_id=workflow_id)
    except N8nAuthenticationError as exc:
        log_action("n8n", "deactivate_workflow", "error", {"workflow_id": workflow_id, "reason": str(exc)})
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(exc)) from exc
    except N8nNotFoundError as exc:
        log_action("n8n", "deactivate_workflow", "error", {"workflow_id": workflow_id, "reason": str(exc)})
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except N8nRequestError as exc:
        log_action("n8n", "deactivate_workflow", "error", {"workflow_id": workflow_id, "reason": str(exc)})
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=str(exc)) from exc
    except N8nAdapterError as exc:
        log_action("n8n", "deactivate_workflow", "error", {"workflow_id": workflow_id, "reason": str(exc)})
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc

    log_action("n8n", "deactivate_workflow", "ok", {"workflow_id": workflow_id})
    return N8nWorkflowActionResponse(
        workflow_id=workflow_id,
        action="deactivate",
        status="ok",
        message="Workflow deactivation command sent",
    )
