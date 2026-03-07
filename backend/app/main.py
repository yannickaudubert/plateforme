from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import build_runtime_config
from app.logging import log_action, setup_logging
from app.routers import admin, health, obsidian, system

runtime = build_runtime_config()

setup_logging()

app = FastAPI(title=runtime.app_name, version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(system.router)
app.include_router(obsidian.router)
app.include_router(admin.router)


@app.on_event("startup")
def startup_log() -> None:
    log_action(
        tool="system",
        action="startup",
        status="ok",
        details={"environment": runtime.app_env},
    )
