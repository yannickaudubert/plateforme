import { useEffect, useState } from "react";
import { PageLayout } from "../components/PageLayout";
import { fetchObsidianNotes } from "../lib/api";

export function ObsidianWorkspace() {
  const [notes, setNotes] = useState<string[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchObsidianNotes(25)
      .then(setNotes)
      .catch((err: Error) => setError(err.message));
  }, []);

  return (
    <PageLayout
      title="Obsidian Workspace"
      description="Canonical documentary workspace over the Obsidian vault."
    >
      <section className="panel">
        <h3>Vault snapshot</h3>
        {error ? <p className="error">Cannot read vault: {error}</p> : null}
        {!error && notes.length === 0 ? <p>No markdown files found.</p> : null}
        {notes.length > 0 ? (
          <ul className="list">
            {notes.map((note) => (
              <li key={note}>{note}</li>
            ))}
          </ul>
        ) : null}
      </section>
      <section className="panel">
        <h3>Planned actions</h3>
        <ul className="list">
          <li>Open note details and frontmatter inspection</li>
          <li>Safe note creation and update with guardrails</li>
          <li>Knowledge export hooks for RAG pipeline</li>
        </ul>
      </section>
    </PageLayout>
  );
}
