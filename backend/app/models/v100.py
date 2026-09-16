from enum import StrEnum
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class MaturityLevel(StrEnum):
    DISCOVERED = "L0-DISCOVERED"
    STAGED = "L1-STAGED"
    OPERABLE = "L2-OPERABLE"
    GOVERNED = "L3-GOVERNED"
    RELIABLE = "L4-RELIABLE"
    COMPOSABLE = "L5-COMPOSABLE"
    MEASURED = "L6-MEASURED"
    FEDERATED = "L7-FEDERATED"
    PRODUCTION = "L8-PRODUCTION"
    SELF_IMPROVING_GOVERNED = "L9-SELF-IMPROVING-GOVERNED"


class AvailabilityRing(StrEnum):
    NOW = "NOW"
    READY = "READY"
    NEAR = "NEAR"
    DISCOVER = "DISCOVER"
    FRONTIER = "FRONTIER"
    CLIENT = "CLIENT"
    HUMAN = "HUMAN"


class LicenseClass(StrEnum):
    OSI_OPEN_SOURCE = "osi-open-source"
    COPYLEFT = "copyleft"
    OPEN_CORE = "open-core"
    SOURCE_AVAILABLE = "source-available"
    FAIR_CODE = "fair-code"
    COMMERCIAL = "commercial"
    UNKNOWN = "unknown"


class ExecutionMode(StrEnum):
    NATIVE_UI = "native-ui"
    DEEP_LINK = "deep-link"
    API = "api"
    MCP = "mcp"
    CLI = "cli"
    FILESYSTEM = "filesystem"
    WORKFLOW = "workflow"
    LIBRARY = "library"
    HUMAN = "human"


class NativePrimitive(StrictModel):
    name: str = Field(min_length=1)
    kind: str = Field(min_length=1)
    description: str = ""


class EngineRecord(StrictModel):
    engine_id: str = Field(min_length=1)
    name: str = Field(min_length=1)
    upstream: str | None = None
    version: str | None = None
    license_class: LicenseClass = LicenseClass.UNKNOWN
    native_primitives: list[NativePrimitive] = Field(default_factory=list)
    capabilities_exposed: list[str] = Field(default_factory=list)
    integration_modes: list[ExecutionMode] = Field(default_factory=list)
    deployment_modes: list[str] = Field(default_factory=list)
    replaceable: bool = True
    notes: list[str] = Field(default_factory=list)


class CapabilityAvailability(StrictModel):
    ring: AvailabilityRing
    sandy: bool = False
    consultant_nodes: list[str] = Field(default_factory=list)
    client_native: bool = False
    external_candidates: list[str] = Field(default_factory=list)


class CapabilityTransfer(StrictModel):
    portable: bool = True
    deployment_modes: list[str] = Field(default_factory=list)
    required_client_prerequisites: list[str] = Field(default_factory=list)
    migration_path: list[str] = Field(default_factory=list)
    rollback: str | None = None
    exit_strategy: str | None = None


class CapabilitySecurity(StrictModel):
    data_classes: list[str] = Field(default_factory=list)
    network_requirements: list[str] = Field(default_factory=list)
    permissions: list[str] = Field(default_factory=list)
    known_risks: list[str] = Field(default_factory=list)


class CapabilityOperations(StrictModel):
    install_time_estimate: str | None = None
    integration_time_estimate: str | None = None
    runbook_ref: str | None = None
    observability: list[str] = Field(default_factory=list)
    backup_restore_ref: str | None = None
    maintenance_load: str | None = None


class CapabilityValue(StrictModel):
    expected_human_time_saved: str | None = None
    expected_risk_reduction: str | None = None
    expected_autonomy_gain: str | None = None
    expected_quality_gain: str | None = None
    expected_revenue_or_cost_effect: str | None = None
    expected_digital_wellbeing_effect: str | None = None


class CapabilityProof(StrictModel):
    neutral_benchmarks: list[str] = Field(default_factory=list)
    previous_projects: list[str] = Field(default_factory=list)
    known_failures: list[str] = Field(default_factory=list)
    antiskills: list[str] = Field(default_factory=list)
    evidence_refs: list[str] = Field(default_factory=list)


class CapabilityCard(StrictModel):
    capability_id: str = Field(min_length=1)
    name: str = Field(min_length=1)
    description: str = ""
    business_outcomes: list[str] = Field(default_factory=list)
    user_outcomes: list[str] = Field(default_factory=list)
    wellbeing_effects: list[str] = Field(default_factory=list)
    resilience_effects: list[str] = Field(default_factory=list)
    value_chain_effects: list[str] = Field(default_factory=list)
    maturity: MaturityLevel = MaturityLevel.DISCOVERED
    availability: CapabilityAvailability
    providers: list[str] = Field(default_factory=list)
    compositions: list[str] = Field(default_factory=list)
    preconditions: list[str] = Field(default_factory=list)
    dependencies: list[str] = Field(default_factory=list)
    transfer: CapabilityTransfer = Field(default_factory=CapabilityTransfer)
    security: CapabilitySecurity = Field(default_factory=CapabilitySecurity)
    operations: CapabilityOperations = Field(default_factory=CapabilityOperations)
    value: CapabilityValue = Field(default_factory=CapabilityValue)
    proof: CapabilityProof = Field(default_factory=CapabilityProof)

    @model_validator(mode="after")
    def production_requires_evidence(self) -> "CapabilityCard":
        if self.maturity == MaturityLevel.PRODUCTION and not self.proof.evidence_refs:
            raise ValueError("L8-PRODUCTION capability requires at least one evidence_ref")
        return self


class PipelineStage(StrictModel):
    stage_id: str = Field(min_length=1)
    name: str = Field(min_length=1)
    mode: Literal["serial", "parallel", "join", "loop", "gate"] = "serial"
    capability_ids: list[str] = Field(default_factory=list)
    engine_ids: list[str] = Field(default_factory=list)
    native_primitive_refs: list[str] = Field(default_factory=list)
    inputs: list[str] = Field(default_factory=list)
    outputs: list[str] = Field(default_factory=list)
    human_roles: list[str] = Field(default_factory=list)
    policy_refs: list[str] = Field(default_factory=list)
    evidence_required: list[str] = Field(default_factory=list)


class ProductionPipelineSpec(StrictModel):
    pipeline_id: str = Field(min_length=1)
    name: str = Field(min_length=1)
    purpose: str = Field(min_length=1)
    stages: list[PipelineStage] = Field(min_length=1)
    artifact_graph_refs: list[str] = Field(default_factory=list)
    acceptance_criteria: list[str] = Field(default_factory=list)
    fallback_modes: list[str] = Field(default_factory=list)


class ExperimentContract(StrictModel):
    experiment_id: str = Field(min_length=1)
    hypothesis: str = Field(min_length=1)
    baseline: str = Field(min_length=1)
    candidate: str = Field(min_length=1)
    success_metrics: list[str] = Field(min_length=1)
    failure_thresholds: list[str] = Field(default_factory=list)
    resource_budget: dict[str, float] = Field(default_factory=dict)
    time_budget_minutes: int = Field(gt=0)
    security_constraints: list[str] = Field(default_factory=list)
    test_corpus_ref: str
    repeatability_requirements: list[str] = Field(default_factory=list)
    teardown_required: bool = True


class ClientTransferPack(StrictModel):
    transfer_id: str = Field(min_length=1)
    capability_id: str = Field(min_length=1)
    architecture_refs: list[str] = Field(default_factory=list)
    prerequisites: list[str] = Field(default_factory=list)
    deployment_profile_refs: list[str] = Field(default_factory=list)
    automation_refs: list[str] = Field(default_factory=list)
    iam_policy_refs: list[str] = Field(default_factory=list)
    network_policy_refs: list[str] = Field(default_factory=list)
    observability_refs: list[str] = Field(default_factory=list)
    backup_restore_refs: list[str] = Field(default_factory=list)
    test_refs: list[str] = Field(default_factory=list)
    security_evidence_refs: list[str] = Field(default_factory=list)
    sbom_refs: list[str] = Field(default_factory=list)
    license_refs: list[str] = Field(default_factory=list)
    runbook_refs: list[str] = Field(default_factory=list)
    operator_guide_refs: list[str] = Field(default_factory=list)
    user_guide_refs: list[str] = Field(default_factory=list)
    training_refs: list[str] = Field(default_factory=list)
    slo_refs: list[str] = Field(default_factory=list)
    cost_model_refs: list[str] = Field(default_factory=list)
    rollback_refs: list[str] = Field(default_factory=list)
    exit_export_refs: list[str] = Field(default_factory=list)
