import { PageLayout } from "../components/PageLayout";

export function N8nOrchestrator() {
  return (
    <PageLayout
      title="n8n Orchestrator"
      description="Workflow orchestration visibility and manual trigger surface."
    >
      <section className="panel">
        <h3>Minimal integration state</h3>
        <ul className="list">
          <li>Endpoint health scaffold available</li>
          <li>Workflow list and run history planned</li>
          <li>Run trigger API planned with guardrails</li>
        </ul>
      </section>
    </PageLayout>
  );
}
