import { useEffect, useState } from "react";
import { PageLayout } from "../components/PageLayout";
import { fetchAdminView } from "../lib/api";
import { AdminView } from "../types/api";

export function Administration() {
  const [admin, setAdmin] = useState<AdminView | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchAdminView()
      .then(setAdmin)
      .catch((err: Error) => setError(err.message));
  }, []);

  return (
    <PageLayout
      title="Administration"
      description="Configuration, secrets state, and operational health visibility."
    >
      {error ? <p className="error">Administration API unavailable: {error}</p> : null}
      {!admin ? <p>Loading administration overview...</p> : null}
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
    </PageLayout>
  );
}
