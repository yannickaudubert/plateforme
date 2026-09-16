import pytest
from pydantic import ValidationError

from app.models.v100 import (
    AvailabilityRing,
    CapabilityAvailability,
    CapabilityCard,
    ClientTransferPack,
    EngineRecord,
    ExperimentContract,
    LicenseClass,
    MaturityLevel,
    NativePrimitive,
    PipelineStage,
    ProductionPipelineSpec,
)


def test_engine_record_preserves_native_primitives() -> None:
    record = EngineRecord(
        engine_id="openproject",
        name="OpenProject",
        license_class=LicenseClass.OSI_OPEN_SOURCE,
        native_primitives=[
            NativePrimitive(name="work_package", kind="project-management"),
            NativePrimitive(name="milestone", kind="planning"),
        ],
        capabilities_exposed=["pmo.manage_backlog", "pmo.plan_dependencies"],
    )

    assert record.native_primitives[0].name == "work_package"
    assert record.replaceable is True


def test_l8_capability_requires_evidence() -> None:
    with pytest.raises(ValidationError):
        CapabilityCard(
            capability_id="cap.document-production",
            name="Document production",
            maturity=MaturityLevel.PRODUCTION,
            availability=CapabilityAvailability(ring=AvailabilityRing.NOW, sandy=True),
        )


def test_l8_capability_accepts_evidence() -> None:
    card = CapabilityCard(
        capability_id="cap.document-production",
        name="Document production",
        maturity=MaturityLevel.PRODUCTION,
        availability=CapabilityAvailability(ring=AvailabilityRing.NOW, sandy=True),
        proof={"evidence_refs": ["evidence://acceptance/document-production/001"]},
    )

    assert card.maturity == MaturityLevel.PRODUCTION


def test_pipeline_supports_parallel_and_join_stages() -> None:
    pipeline = ProductionPipelineSpec(
        pipeline_id="pipeline.audit",
        name="Audit and diagnostic",
        purpose="Produce a traceable audit deliverable",
        stages=[
            PipelineStage(
                stage_id="context",
                name="Build context",
                outputs=["context-pack"],
            ),
            PipelineStage(
                stage_id="analysis",
                name="Parallel analyses",
                mode="parallel",
                inputs=["context-pack"],
                outputs=["findings", "architecture", "risks"],
            ),
            PipelineStage(
                stage_id="review",
                name="Human review",
                mode="join",
                inputs=["findings", "architecture", "risks"],
                evidence_required=["review-receipt"],
            ),
        ],
    )

    assert pipeline.stages[1].mode == "parallel"
    assert pipeline.stages[2].mode == "join"


def test_experiment_contract_requires_positive_time_budget() -> None:
    with pytest.raises(ValidationError):
        ExperimentContract(
            experiment_id="exp-001",
            hypothesis="Candidate improves retrieval quality",
            baseline="current-search",
            candidate="candidate-search",
            success_metrics=["precision"],
            time_budget_minutes=0,
            test_corpus_ref="corpus://neutral/retrieval-v1",
        )


def test_client_transfer_pack_is_portable_contract() -> None:
    pack = ClientTransferPack(
        transfer_id="transfer-001",
        capability_id="cap.search",
        architecture_refs=["arch://search/v1"],
        rollback_refs=["runbook://rollback/search-v1"],
        exit_export_refs=["runbook://export/search-v1"],
    )

    assert pack.capability_id == "cap.search"
    assert pack.exit_export_refs
