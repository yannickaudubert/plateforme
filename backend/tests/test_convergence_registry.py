from __future__ import annotations

from fastapi.testclient import TestClient

from app.main import app
from app.services.convergence_registry import ConvergenceRegistryService


def test_convergence_registry_preserves_authority_invariants() -> None:
    registry = ConvergenceRegistryService().load()
    assert registry.status == "PROPOSAL_READ_ONLY"
    assert registry.authority.lineage_decision == "OPTION-C"
    assert registry.authority.authority_kernel == "v0.7.2-C"
    assert registry.authority.contribution_branch == "v0.8.0-alpha9"
    assert "No second Agent Core" in registry.authority.rules
    assert "No second Capability Core" in registry.authority.rules
    assert "No host executor is enabled by this convergence slice" in registry.authority.rules


def test_convergence_registry_has_specialized_surfaces() -> None:
    registry = ConvergenceRegistryService().load()
    registry_ids = {item.id for item in registry.registries}
    radar_ids = {item.id for item in registry.radars}
    building_ids = {item.id for item in registry.building_profiles}
    assert {"capability", "service", "experience", "regulatory", "improvement"} <= registry_ids
    assert {"resource", "python", "compute", "regulatory"} <= radar_ids
    assert {"dsi-innovation", "consulting", "science", "infra-compute"} <= building_ids


def test_convergence_api_is_read_only() -> None:
    client = TestClient(app)
    summary = client.get("/api/v1/convergence/summary")
    assert summary.status_code == 200
    payload = summary.json()
    assert payload["authority_kernel"] == "v0.7.2-C"
    assert payload["radar_count"] >= 4
    assert client.get("/api/v1/convergence/overview").status_code == 200
    for path in (
        "/api/v1/convergence/overview",
        "/api/v1/convergence/registries",
        "/api/v1/convergence/buildings",
        "/api/v1/convergence/radars",
        "/api/v1/convergence/regulatory",
    ):
        assert client.post(path, json={}).status_code == 405
