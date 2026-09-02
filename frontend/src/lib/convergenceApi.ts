const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? "http://localhost:8000";

export interface PlaneEntry { id: string; purpose: string; }
export interface RegistryEntry { id: string; label: string; status: string; owner_plane: string; }
export interface DistrictEntry { id: string; label: string; purpose: string; }
export interface BuildingProfileEntry { id: string; label: string; status: string; }
export interface TeamDeckEntry { id: string; label: string; activation: string; }
export interface RadarEntry { id: string; label: string; status: string; scope: string; }
export interface RegulatorySource { id: string; label: string; authority_type: string; jurisdiction: string; source_url: string; current_note: string; }
export interface SalvageEntry { source: string; decision: string; assets: string[]; }
export interface GateEntry { id: string; label: string; state: string; }

export interface ConvergenceRegistry {
  schema_version: string;
  registry_id: string;
  status: string;
  generated_at: string;
  authority: { lineage_decision: string; authority_kernel: string; contribution_branch: string; rules: string[]; };
  planes: PlaneEntry[];
  truth_facets: string[];
  registries: RegistryEntry[];
  districts: DistrictEntry[];
  building_profiles: BuildingProfileEntry[];
  team_decks: TeamDeckEntry[];
  radars: RadarEntry[];
  compute_provider_classes: string[];
  regulatory_seed: { status: string; verified_on: string; sources: RegulatorySource[]; };
  salvage: SalvageEntry[];
  gates: GateEntry[];
}

async function request<T>(path: string): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${path}`, { headers: { "Content-Type": "application/json" } });
  if (!response.ok) {
    let detail: string | undefined;
    try { detail = ((await response.json()) as { detail?: string }).detail; } catch { detail = undefined; }
    throw new Error(detail ? `API error ${response.status}: ${detail}` : `API error ${response.status}`);
  }
  return response.json() as Promise<T>;
}

export function fetchConvergenceOverview(): Promise<ConvergenceRegistry> {
  return request<ConvergenceRegistry>("/api/v1/convergence/overview");
}
