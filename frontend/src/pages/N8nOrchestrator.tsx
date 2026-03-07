import { useState } from "react";
import { PageLayout } from "../components/PageLayout";
import { activateN8nWorkflow, deactivateN8nWorkflow, fetchN8nExecutions, fetchN8nWorkflows } from "../lib/api";
import { N8nExecutionSummary, N8nWorkflowSummary } from "../types/api";

export function N8nOrchestrator() {
  const [workflows, setWorkflows] = useState<N8nWorkflowSummary[]>([]);
  const [executions, setExecutions] = useState<N8nExecutionSummary[]>([]);
  const [selectedWorkflowId, setSelectedWorkflowId] = useState<string>("");
  const [confirmAction, setConfirmAction] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);
  const [info, setInfo] = useState<string | null>(null);
  const [isLoadingWorkflows, setIsLoadingWorkflows] = useState<boolean>(false);
  const [isLoadingExecutions, setIsLoadingExecutions] = useState<boolean>(false);
  const [isSendingAction, setIsSendingAction] = useState<boolean>(false);

  const loadWorkflows = async () => {
    setIsLoadingWorkflows(true);
    setError(null);
    setInfo(null);
    try {
      const data = await fetchN8nWorkflows(50);
      setWorkflows(data);
      if (!data.find((workflow) => workflow.id === selectedWorkflowId)) {
        setSelectedWorkflowId(data[0]?.id ?? "");
      }
      setInfo(`Loaded ${data.length} workflow(s).`);
    } catch (err) {
      setError((err as Error).message);
    } finally {
      setIsLoadingWorkflows(false);
    }
  };

  const loadExecutions = async () => {
    setIsLoadingExecutions(true);
    setError(null);
    setInfo(null);
    try {
      const data = await fetchN8nExecutions(25);
      setExecutions(data);
      setInfo(`Loaded ${data.length} execution(s).`);
    } catch (err) {
      setError((err as Error).message);
    } finally {
      setIsLoadingExecutions(false);
    }
  };

  const runWorkflowAction = async (action: "activate" | "deactivate") => {
    if (!selectedWorkflowId) {
      return;
    }
    setIsSendingAction(true);
    setError(null);
    setInfo(null);
    try {
      if (action === "activate") {
        await activateN8nWorkflow(selectedWorkflowId, { confirm: confirmAction });
      } else {
        await deactivateN8nWorkflow(selectedWorkflowId, { confirm: confirmAction });
      }
      setInfo(`Workflow ${selectedWorkflowId} ${action} command sent.`);
      await loadWorkflows();
    } catch (err) {
      setError((err as Error).message);
    } finally {
      setIsSendingAction(false);
    }
  };

  return (
    <PageLayout
      title="n8n Orchestrator"
      description="Workflow visibility and operator controls (activate/deactivate)."
    >
      <section className="panel">
        <h3>n8n actions</h3>
        {error ? <p className="error">{error}</p> : null}
        {info ? <p className="success">{info}</p> : null}
        <button className="button" type="button" onClick={() => void loadWorkflows()} disabled={isLoadingWorkflows}>
          {isLoadingWorkflows ? "Loading workflows..." : "Refresh workflows"}
        </button>
        <button className="button" type="button" onClick={() => void loadExecutions()} disabled={isLoadingExecutions}>
          {isLoadingExecutions ? "Loading executions..." : "Refresh executions"}
        </button>

        <label className="label" htmlFor="n8n-workflow-select">
          Workflow
        </label>
        <select
          id="n8n-workflow-select"
          className="input"
          value={selectedWorkflowId}
          onChange={(event) => setSelectedWorkflowId(event.target.value)}
          disabled={workflows.length === 0 || isLoadingWorkflows}
        >
          {workflows.map((workflow) => (
            <option key={workflow.id} value={workflow.id}>
              {workflow.name} ({workflow.id}) - {workflow.active ? "active" : "inactive"}
            </option>
          ))}
        </select>

        <label className="label">
          <input
            type="checkbox"
            checked={confirmAction}
            onChange={(event) => setConfirmAction(event.target.checked)}
          />{" "}
          Confirm workflow state change
        </label>

        <div>
          <button
            className="button"
            type="button"
            onClick={() => void runWorkflowAction("activate")}
            disabled={isSendingAction || !selectedWorkflowId}
          >
            {isSendingAction ? "Sending..." : "Activate workflow"}
          </button>
          <button
            className="button"
            type="button"
            onClick={() => void runWorkflowAction("deactivate")}
            disabled={isSendingAction || !selectedWorkflowId}
          >
            {isSendingAction ? "Sending..." : "Deactivate workflow"}
          </button>
        </div>
      </section>

      <section className="panel">
        <h3>Workflows</h3>
        {workflows.length === 0 ? <p>No workflows loaded.</p> : null}
        {workflows.length > 0 ? (
          <ul className="list">
            {workflows.map((workflow) => (
              <li key={workflow.id}>
                {workflow.name} ({workflow.id}) - {workflow.active ? "active" : "inactive"}
              </li>
            ))}
          </ul>
        ) : null}
      </section>

      <section className="panel">
        <h3>Recent executions</h3>
        {executions.length === 0 ? <p>No executions loaded.</p> : null}
        {executions.length > 0 ? (
          <ul className="list">
            {executions.map((execution) => (
              <li key={execution.id}>
                {execution.id} - {execution.status}
                {execution.workflow_id ? ` (workflow ${execution.workflow_id})` : ""}
              </li>
            ))}
          </ul>
        ) : null}
      </section>
    </PageLayout>
  );
}
