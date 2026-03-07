import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { PageLayout } from "../components/PageLayout";
import { fetchAdminDiagnostics, fetchAdminView } from "../lib/api";
import { AdminDiagnostics, AdminView } from "../types/api";

export function Administration() {
  const [admin, setAdmin] = useState<AdminView | null>(null);
  const [diagnostics, setDiagnostics] = useState<AdminDiagnostics | null>(null);
  const [error, setError] = useState<string | null>(null);

  const loadAdministration = () => {
    setError(null);
    Promise.all([fetchAdminView(), fetchAdminDiagnostics()])
      .then(([overview, diagnostic]) => {
        setAdmin(overview);
        setDiagnostics(diagnostic);
      })
      .catch((err: Error) => setError(err.message));
  };

  useEffect(() => {
    loadAdministration();
  }, []);

  return (
    <PageLayout
      title="Administration"
      description="Configuration, secrets state, and operational health visibility."
    >
      {error ? <p className="error">Administration API unavailable: {error}</p> : null}
      <button className="button" onClick={loadAdministration} type="button">
        Refresh diagnostics
      </button>
      <Link className="button" to="/setup">Open setup wizard</Link>
      {!admin || !diagnostics ? <p>Loading administration overview...</p> : null}
      {admin ? (
        <div className="grid">
          <article className="card">
            <h3>Environment</h3>
            <p>{admin.environment}</p>
            <p>{admin.app_name}</p>
            <p>Config file: {admin.config_file}</p>
          </article>
          <article className="card">
            <h3>Obsidian</h3>
            <p>Vault path: {admin.obsidian_vault_path}</p>
            <p>Allowed roots: {admin.obsidian_allowed_roots.join(", ")}</p>
          </article>
          <article className="card">
            <h3>Tool endpoints</h3>
            <ul className="list">
              <li>NocoDB: {admin.tools.nocodb_base_url}</li>
              <li>n8n: {admin.tools.n8n_base_url}</li>
              <li>Perplexica: {admin.tools.perplexica_base_url}</li>
              <li>Open WebUI: {admin.tools.openwebui_base_url}</li>
            </ul>
          </article>
          <article className="card">
            <h3>Secrets state (masked)</h3>
            <ul className="list">
              <li>NocoDB token set: {String(admin.secrets.nocodb_token_set)}</li>
              <li>n8n API key set: {String(admin.secrets.n8n_api_key_set)}</li>
              <li>Perplexica API key set: {String(admin.secrets.perplexica_api_key_set)}</li>
              <li>Open WebUI API key set: {String(admin.secrets.openwebui_api_key_set)}</li>
            </ul>
          </article>
        </div>
      ) : null}
      {diagnostics ? (
        <>
          <section className="panel">
            <h3>Deployment diagnostics</h3>
            <p>Generated at: {new Date(diagnostics.generated_at).toLocaleString()}</p>
            <h4>Files</h4>
            <ul className="list">
              {Object.entries(diagnostics.files).map(([key, value]) => (
                <li key={key}>
                  {key}: {String(value)}
                </li>
              ))}
            </ul>
            <h4>Path checks</h4>
            <ul className="list">
              {Object.entries(diagnostics.path_checks).map(([key, value]) => (
                <li key={key}>
                  {key}: {String(value)}
                </li>
              ))}
            </ul>
            <h4>Tool health</h4>
            <ul className="list">
              {diagnostics.tool_health.map((tool) => (
                <li key={tool.tool}>
                  {tool.tool}: {tool.status} ({tool.message})
                </li>
              ))}
            </ul>
            <h4>Recommended actions</h4>
            {diagnostics.recommendations.length === 0 ? (
              <p>No blocking recommendations.</p>
            ) : (
              <ul className="list">
                {diagnostics.recommendations.map((recommendation) => (
                  <li key={recommendation}>{recommendation}</li>
                ))}
              </ul>
            )}
          </section>
          <section className="panel">
            <h3>Stack commands</h3>
            <pre className="command-block">.\\scripts\\bootstrap.ps1</pre>
            <pre className="command-block">.\\scripts\\up.ps1</pre>
            <pre className="command-block">.\\scripts\\up.ps1 -WithPerplexica</pre>
            <pre className="command-block">.\\scripts\\status.ps1</pre>
            <pre className="command-block">.\\scripts\\down.ps1</pre>
          </section>
        </>
      ) : null}
    </PageLayout>
  );
}
