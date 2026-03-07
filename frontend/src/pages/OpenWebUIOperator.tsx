import { PageLayout } from "../components/PageLayout";

export function OpenWebUIOperator() {
  return (
    <PageLayout
      title="Open WebUI Operator"
      description="Operator AI interface entrypoint with future tool invocation hooks."
    >
      <section className="panel">
        <h3>Minimal integration state</h3>
        <ul className="list">
          <li>Endpoint health scaffold available</li>
          <li>Model and context selection planned</li>
          <li>Safe operator tool mode planned</li>
        </ul>
      </section>
    </PageLayout>
  );
}
