from __future__ import annotations

import json
from pathlib import Path

from app.config import ROOT_DIR
from app.models.convergence import ConvergenceRegistry


DEFAULT_REGISTRY_PATH = ROOT_DIR / "config" / "convergence" / "registry.v0.1.json"


class ConvergenceRegistryError(RuntimeError):
    pass


class ConvergenceRegistryService:
    """Read-only loader for the convergence proposal registry."""

    def __init__(self, registry_path: Path | None = None) -> None:
        self.registry_path = registry_path or DEFAULT_REGISTRY_PATH

    def load(self) -> ConvergenceRegistry:
        try:
            raw = self.registry_path.read_text(encoding="utf-8")
        except OSError as exc:
            raise ConvergenceRegistryError(
                f"Unable to read convergence registry at {self.registry_path}"
            ) from exc

        try:
            payload = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise ConvergenceRegistryError("Convergence registry is not valid JSON") from exc

        try:
            return ConvergenceRegistry.model_validate(payload)
        except Exception as exc:
            raise ConvergenceRegistryError("Convergence registry failed schema validation") from exc
