from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status

from app.config import RuntimeConfig
from app.dependencies import (
    clear_runtime_caches,
    get_runtime_config,
    get_setup_service,
)
from app.logging import log_action
from app.models.setup import (
    SetupApplyRequest,
    SetupApplyResponse,
    SetupConfigurationState,
    SetupObsidianInput,
    SetupRuntimeInput,
    SetupToolsInput,
)
from app.secrets import get_secret_flags
from app.services.setup_service import SetupService, SetupValidationError

router = APIRouter(prefix="/api/v1/setup", tags=["setup"])


@router.get("/state", response_model=SetupConfigurationState)
def setup_state(
    runtime: RuntimeConfig = Depends(get_runtime_config),
    setup_service: SetupService = Depends(get_setup_service),
):
    runtime_state = {
        "runtime": SetupRuntimeInput(
            app_name=runtime.app_name,
            app_env=runtime.app_env,
            app_host=runtime.app_host,
            app_port=runtime.app_port,
            log_dir=runtime.log_dir,
        ),
        "obsidian": SetupObsidianInput(
            vault_path=runtime.obsidian_vault_path,
            allowed_roots=runtime.obsidian_allowed_roots,
        ),
        "tools": SetupToolsInput(
            nocodb_base_url=runtime.nocodb_base_url,
            n8n_base_url=runtime.n8n_base_url,
            perplexica_base_url=runtime.perplexica_base_url,
            openwebui_base_url=runtime.openwebui_base_url,
        ),
    }
    return setup_service.get_state(runtime=runtime_state, secret_flags=get_secret_flags())


@router.put("/apply", response_model=SetupApplyResponse)
def setup_apply(
    payload: SetupApplyRequest,
    setup_service: SetupService = Depends(get_setup_service),
) -> SetupApplyResponse:
    try:
        result = setup_service.apply(payload)
    except SetupValidationError as exc:
        log_action(
            tool="setup",
            action="apply_configuration",
            status="error",
            details={"reason": str(exc)},
        )
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    except OSError as exc:
        log_action(
            tool="setup",
            action="apply_configuration",
            status="error",
            details={"reason": "filesystem_error", "type": exc.__class__.__name__},
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to write configuration files",
        ) from exc

    clear_runtime_caches()
    log_action(
        tool="setup",
        action="apply_configuration",
        status="ok",
        details={
            "updated_env_keys_count": len(result.updated_env_keys),
            "updated_secret_keys_count": len(result.updated_secret_keys),
        },
    )
    return result
