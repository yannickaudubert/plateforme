import { PageLayout } from "../components/PageLayout";

export function NocoDBControl() {
  return (
    <PageLayout
      title="NocoDB Control"
      description="Structured transverse data control and schema visibility."
    >
      <section className="panel">
        <h3>Minimal integration state</h3>
        <ul className="list">
          <li>Endpoint health scaffold available</li>
          <li>Base/table listing to be added in next iteration</li>
          <li>Safe row operations planned with journaling</li>
        </ul>
      </section>
    </PageLayout>
  );
}
