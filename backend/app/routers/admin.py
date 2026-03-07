from fastapi import APIRouter, Depends

from app.config import RuntimeConfig
from app.dependencies import get_runtime_config
from app.models.system import AdminOverviewResponse
from app.secrets import get_secret_flags

router = APIRouter(prefix="/api/v1/admin", tags=["administration"])


@router.get("/overview", response_model=AdminOverviewResponse)
def admin_overview(config: RuntimeConfig = Depends(get_runtime_config)) -> AdminOverviewResponse:
    return AdminOverviewResponse(
        app_name=config.app_name,
        environment=config.app_env,
        config_file=config.config_file,
        obsidian_vault_path=config.obsidian_vault_path,
        obsidian_allowed_roots=config.obsidian_allowed_roots,
        tools={
            "nocodb_base_url": config.nocodb_base_url,
            "n8n_base_url": config.n8n_base_url,
            "perplexica_base_url": config.perplexica_base_url,
            "openwebui_base_url": config.openwebui_base_url,
        },
        secrets=get_secret_flags(),
    )
