import { useEffect, useState } from "react";
import { ConvergenceRegistry, fetchConvergenceOverview } from "../lib/convergenceApi";

function statusClass(status: string): string {
  const normalized = status.toLowerCase();
  if (normalized.includes("preserve") || normalized.includes("admit") || normalized.includes("existing")) return "ok";
  return "degraded";
}

export function SIIAOSFabric() {
  const [registry, setRegistry] = useState<ConvergenceRegistry | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchConvergenceOverview()
      .then((payload) => { setRegistry(payload); setError(null); })
      .catch((err: unknown) => setError(err instanceof Error ? err.message : "Unable to load convergence registry"));
  }, []);

  if (error) return <div className="error">{error}</div>;
  if (!registry) return <div className="panel">Loading SIIAOS convergence registry…</div>;

  return (
    <section>
      <header className="page-header">
        <h2>SIIAOS Fabric</h2>
        <p>Read-only convergence view — authority kernel {registry.authority.authority_kernel}, contribution {registry.authority.contribution_branch}.</p>
      </header>

      <div className="grid">
        <article className="card">
          <div className="card-top"><strong>Authority lineage</strong><span className="pill ok">{registry.authority.lineage_decision}</span></div>
          <p>{registry.status}</p>
          <ul className="list">{registry.authority.rules.map((rule) => <li key={rule}>{rule}</li>)}</ul>
        </article>
        <article className="card">
          <strong>Current convergence surface</strong>
          <ul className="list">
            <li>{registry.registries.length} specialized registries</li><li>{registry.districts.length} operator districts</li>
            <li>{registry.building_profiles.length} building profiles</li><li>{registry.team_decks.length} dormant team decks</li>
            <li>{registry.radars.length} radar families</li>
          </ul>
        </article>
        <article className="card"><strong>Truth facets</strong><p>{registry.truth_facets.join(" · ")}</p></article>
      </div>

      <section className="panel"><h3>Operator city / districts</h3><div className="grid">
        {registry.districts.map((district) => <article className="card" key={district.id}><strong>{district.label}</strong><p>{district.purpose}</p></article>)}
      </div></section>

      <section className="panel"><h3>Specialized registries</h3><div className="table-scroll"><table className="data-table">
        <thead><tr><th>Registry</th><th>Plane</th><th>Status</th></tr></thead><tbody>
          {registry.registries.map((item) => <tr key={item.id}><td>{item.label}</td><td>{item.owner_plane}</td><td><span className={`pill ${statusClass(item.status)}`}>{item.status}</span></td></tr>)}
        </tbody></table></div></section>

      <section className="panel"><h3>Buildings / specialist cockpits</h3><div className="grid">
        {registry.building_profiles.map((building) => <article className="card" key={building.id}><div className="card-top"><strong>{building.label}</strong><span className={`pill ${statusClass(building.status)}`}>{building.status}</span></div></article>)}
      </div></section>

      <section className="panel"><h3>Dormant agent teams</h3><div className="grid">
        {registry.team_decks.map((team) => <article className="card" key={team.id}><strong>{team.label}</strong><p>{team.activation}</p></article>)}
      </div></section>

      <section className="panel"><h3>Radar & admission fabric</h3><div className="table-scroll"><table className="data-table">
        <thead><tr><th>Radar</th><th>Scope</th><th>Status</th></tr></thead><tbody>
          {registry.radars.map((radar) => <tr key={radar.id}><td>{radar.label}</td><td>{radar.scope}</td><td><span className={`pill ${statusClass(radar.status)}`}>{radar.status}</span></td></tr>)}
        </tbody></table></div></section>

      <section className="panel"><h3>Regulatory seed</h3>
        <p>{registry.regulatory_seed.status} · verified {registry.regulatory_seed.verified_on}. Source metadata is kept distinct from interpretation and machine policy.</p>
        <div className="table-scroll"><table className="data-table"><thead><tr><th>Source</th><th>Type / jurisdiction</th><th>Current note</th></tr></thead><tbody>
          {registry.regulatory_seed.sources.map((source) => <tr key={source.id}><td><a href={source.source_url} target="_blank" rel="noreferrer">{source.label}</a></td><td>{source.authority_type} · {source.jurisdiction}</td><td>{source.current_note}</td></tr>)}
        </tbody></table></div>
      </section>

      <section className="panel"><h3>Salvage / migration decisions</h3><div className="grid">
        {registry.salvage.map((item) => <article className="card" key={item.source}><strong>{item.source}</strong><p>{item.decision}</p><ul className="list">{item.assets.map((asset) => <li key={asset}>{asset}</li>)}</ul></article>)}
      </div></section>

      <section className="panel"><h3>Gates</h3><div className="grid">
        {registry.gates.map((gate) => <article className="card" key={gate.id}><div className="card-top"><strong>{gate.id} — {gate.label}</strong><span className={`pill ${statusClass(gate.state)}`}>{gate.state}</span></div></article>)}
      </div></section>
    </section>
  );
}
