from datetime import datetime, timezone
from pathlib import Path

from fastapi import APIRouter, Depends

from app.config import ROOT_DIR, RuntimeConfig
from app.dependencies import get_runtime_config, get_status_service
from app.models.system import AdminDiagnosticsResponse, AdminOverviewResponse
from app.secrets import get_secret_flags
from app.services.status_service import StatusService

router = APIRouter(prefix="/api/v1/admin", tags=["administration"])


@router.get("/overview", response_model=AdminOverviewResponse)
def admin_overview(config: RuntimeConfig = Depends(get_runtime_config)) -> AdminOverviewResponse:
    return AdminOverviewResponse(
        app_name=config.app_name,
        environment=config.app_env,
        config_file=config.config_file,
        obsidian_vault_path=config.obsidian_vault_path,
        obsidian_allowed_roots=config.obsidian_allowed_roots,
        nocodb_writable_tables=config.nocodb_writable_tables,
        tools={
            "nocodb_base_url": config.nocodb_base_url,
            "n8n_base_url": config.n8n_base_url,
            "perplexica_base_url": config.perplexica_base_url,
            "openwebui_base_url": config.openwebui_base_url,
        },
        secrets=get_secret_flags(),
    )


@router.get("/diagnostics", response_model=AdminDiagnosticsResponse)
def admin_diagnostics(
    config: RuntimeConfig = Depends(get_runtime_config),
    status_service: StatusService = Depends(get_status_service),
) -> AdminDiagnosticsResponse:
    root = ROOT_DIR
    env_file = root / ".env"
    compose_default = root / "docker-compose.yml"
    compose_full = root / "docker-compose.full.yml"
    scripts_dir = root / "scripts"
    logs_dir = Path(config.log_dir)
    vault_dir = Path(config.obsidian_vault_path)
    config_file = Path(config.config_file)

    files = {
        ".env": env_file.exists(),
        "config_file": config_file.exists(),
        "docker_compose": compose_default.exists(),
        "docker_compose_full": compose_full.exists(),
        "scripts_dir": scripts_dir.exists(),
    }
    paths = {
        "repo_root": str(root),
        "config_file": str(config_file),
        "log_dir": str(logs_dir),
        "obsidian_vault_path": str(vault_dir),
    }
    path_checks = {
        "log_dir_exists": logs_dir.exists(),
        "obsidian_vault_exists": vault_dir.exists(),
        "obsidian_allowed_roots_non_empty": len(config.obsidian_allowed_roots) > 0,
    }

    tool_health = status_service.system_status().tools
    secret_flags = get_secret_flags()
    recommendations: list[str] = []

    if not files[".env"]:
        recommendations.append("Create .env from .env.example before starting the stack.")
    if not path_checks["obsidian_vault_exists"]:
        recommendations.append("Obsidian vault path is missing. Update OBSIDIAN_VAULT_PATH.")
    if not secret_flags["nocodb_token_set"]:
        recommendations.append("Set NOCODB_API_TOKEN for NocoDB read operations.")
    if len(config.nocodb_writable_tables) == 0:
        recommendations.append("Set NOCODB_WRITABLE_TABLES to enable explicit NocoDB write scope.")
    if not files["docker_compose_full"]:
        recommendations.append("docker-compose.full.yml is missing; full stack deployment is unavailable.")

    degraded_tools = [tool.tool for tool in tool_health if tool.status != "ok"]
    if degraded_tools:
        recommendations.append(
            "Fix degraded tool endpoints before production use: " + ", ".join(degraded_tools)
        )

    return AdminDiagnosticsResponse(
        generated_at=datetime.now(timezone.utc).isoformat(),
        files=files,
        paths=paths,
        path_checks=path_checks,
        tool_health=tool_health,
        recommendations=recommendations,
    )
