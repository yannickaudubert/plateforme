import { ToolHealth } from "../types/api";

interface ToolStatusCardProps {
  tool: ToolHealth;
}

export function ToolStatusCard({ tool }: ToolStatusCardProps) {
  return (
    <article className="card">
      <div className="card-top">
        <h3>{tool.tool}</h3>
        <span className={tool.status === "ok" ? "pill ok" : "pill degraded"}>
          {tool.status}
        </span>
      </div>
      <p>{tool.message}</p>
      <small>Checked at: {new Date(tool.checked_at).toLocaleString()}</small>
    </article>
  );
}
