from pydantic import BaseModel, ConfigDict


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class AuthorityContract(StrictModel):
    lineage_decision: str
    authority_kernel: str
    contribution_branch: str
    rules: list[str]


class PlaneEntry(StrictModel):
    id: str
    purpose: str


class RegistryEntry(StrictModel):
    id: str
    label: str
    status: str
    owner_plane: str


class DistrictEntry(StrictModel):
    id: str
    label: str
    purpose: str


class BuildingProfileEntry(StrictModel):
    id: str
    label: str
    status: str


class TeamDeckEntry(StrictModel):
    id: str
    label: str
    activation: str


class RadarEntry(StrictModel):
    id: str
    label: str
    status: str
    scope: str


class RegulatorySource(StrictModel):
    id: str
    label: str
    authority_type: str
    jurisdiction: str
    source_url: str
    current_note: str


class RegulatorySeed(StrictModel):
    status: str
    verified_on: str
    sources: list[RegulatorySource]


class SalvageEntry(StrictModel):
    source: str
    decision: str
    assets: list[str]


class GateEntry(StrictModel):
    id: str
    label: str
    state: str


class ConvergenceRegistry(StrictModel):
    schema_version: str
    registry_id: str
    status: str
    generated_at: str
    authority: AuthorityContract
    planes: list[PlaneEntry]
    truth_facets: list[str]
    registries: list[RegistryEntry]
    districts: list[DistrictEntry]
    building_profiles: list[BuildingProfileEntry]
    team_decks: list[TeamDeckEntry]
    radars: list[RadarEntry]
    compute_provider_classes: list[str]
    regulatory_seed: RegulatorySeed
    salvage: list[SalvageEntry]
    gates: list[GateEntry]


class ConvergenceSummary(StrictModel):
    schema_version: str
    registry_id: str
    status: str
    generated_at: str
    authority_kernel: str
    contribution_branch: str
    district_count: int
    registry_count: int
    building_profile_count: int
    team_deck_count: int
    radar_count: int
    regulatory_source_count: int
    blocking_gates: list[GateEntry]
