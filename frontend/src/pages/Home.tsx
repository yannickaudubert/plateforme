import { useEffect, useState } from "react";
import { PageLayout } from "../components/PageLayout";
import { ToolStatusCard } from "../components/ToolStatusCard";
import { fetchSystemStatus } from "../lib/api";
import { SystemStatus } from "../types/api";

export function Home() {
  const [status, setStatus] = useState<SystemStatus | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchSystemStatus()
      .then(setStatus)
      .catch((err: Error) => setError(err.message));
  }, []);

  return (
    <PageLayout
      title="Home"
      description="Unified operator control center for transverse DSI operations."
    >
      {error ? <p className="error">Backend unavailable: {error}</p> : null}
      {!status ? <p>Loading system status...</p> : null}
      {status ? (
        <>
          <div className="grid">
            {status.tools.map((tool) => (
              <ToolStatusCard key={tool.tool} tool={tool} />
            ))}
          </div>
          <section className="panel">
            <h3>Recent actions</h3>
            {status.recent_actions.length === 0 ? (
              <p>No actions recorded yet.</p>
            ) : (
              <ul className="list">
                {status.recent_actions.map((entry) => (
                  <li key={`${entry.timestamp}-${entry.tool}-${entry.action}`}>
                    <strong>{entry.tool}</strong> - {entry.action} - {entry.status} ({new Date(entry.timestamp).toLocaleString()})
                  </li>
                ))}
              </ul>
            )}
          </section>
        </>
      ) : null}
    </PageLayout>
  );
}
