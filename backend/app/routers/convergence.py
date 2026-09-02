from __future__ import annotations

from fastapi import APIRouter, HTTPException

from app.models.convergence import (
    BuildingProfileEntry,
    ConvergenceRegistry,
    ConvergenceSummary,
    DistrictEntry,
    RadarEntry,
    RegistryEntry,
    RegulatorySeed,
    SalvageEntry,
    TeamDeckEntry,
)
from app.services.convergence_registry import ConvergenceRegistryError, ConvergenceRegistryService


router = APIRouter(prefix="/api/v1/convergence", tags=["siiaos-convergence"])


def _registry() -> ConvergenceRegistry:
    try:
        return ConvergenceRegistryService().load()
    except ConvergenceRegistryError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc


@router.get("/summary", response_model=ConvergenceSummary)
def convergence_summary() -> ConvergenceSummary:
    registry = _registry()
    return ConvergenceSummary(
        schema_version=registry.schema_version,
        registry_id=registry.registry_id,
        status=registry.status,
        generated_at=registry.generated_at,
        authority_kernel=registry.authority.authority_kernel,
        contribution_branch=registry.authority.contribution_branch,
        district_count=len(registry.districts),
        registry_count=len(registry.registries),
        building_profile_count=len(registry.building_profiles),
        team_deck_count=len(registry.team_decks),
        radar_count=len(registry.radars),
        regulatory_source_count=len(registry.regulatory_seed.sources),
        blocking_gates=[gate for gate in registry.gates if gate.state.startswith("BLOCKING")],
    )


@router.get("/overview", response_model=ConvergenceRegistry)
def convergence_overview() -> ConvergenceRegistry:
    return _registry()


@router.get("/registries", response_model=list[RegistryEntry])
def convergence_registries() -> list[RegistryEntry]:
    return _registry().registries


@router.get("/districts", response_model=list[DistrictEntry])
def convergence_districts() -> list[DistrictEntry]:
    return _registry().districts


@router.get("/buildings", response_model=list[BuildingProfileEntry])
def convergence_buildings() -> list[BuildingProfileEntry]:
    return _registry().building_profiles


@router.get("/teams", response_model=list[TeamDeckEntry])
def convergence_teams() -> list[TeamDeckEntry]:
    return _registry().team_decks


@router.get("/radars", response_model=list[RadarEntry])
def convergence_radars() -> list[RadarEntry]:
    return _registry().radars


@router.get("/regulatory", response_model=RegulatorySeed)
def convergence_regulatory() -> RegulatorySeed:
    return _registry().regulatory_seed


@router.get("/salvage", response_model=list[SalvageEntry])
def convergence_salvage() -> list[SalvageEntry]:
    return _registry().salvage
