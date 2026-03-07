import {
  AdminDiagnostics,
  AdminView,
  N8nExecutionSummary,
  N8nWorkflowActionPayload,
  N8nWorkflowActionResponse,
  N8nWorkflowSummary,
  NocoDBBaseSummary,
  NocoDBRowMutationResponse,
  NocoDBRowWritePayload,
  NocoDBRowsResponse,
  NocoDBTableSummary,
  OpenWebUIChatPayload,
  OpenWebUIChatResponse,
  OpenWebUIChatToNotePayload,
  OpenWebUIChatToNoteResponse,
  OpenWebUIModelSummary,
  ObsidianCreateNotePayload,
  ObsidianNoteContent,
  ObsidianUpdateNotePayload,
  ObsidianWriteResponse,
  PerplexicaSearchPayload,
  PerplexicaSearchResponse,
  PerplexicaSearchToNotePayload,
  PerplexicaSearchToNoteResponse,
  SetupApplyRequest,
  SetupApplyResponse,
  SetupConfigurationState,
  SystemStatus
} from "../types/api";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? "http://localhost:8000";

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${path}`, {
    headers: {
      "Content-Type": "application/json"
    },
    ...init
  });
  if (!response.ok) {
    let detail: string | undefined;
    try {
      const payload = (await response.json()) as { detail?: string };
      detail = payload.detail;
    } catch {
      detail = undefined;
    }
    throw new Error(detail ? `API error ${response.status}: ${detail}` : `API error ${response.status}`);
  }
  return response.json() as Promise<T>;
}

export function fetchSystemStatus(): Promise<SystemStatus> {
  return request<SystemStatus>("/api/v1/system/status");
}

export function fetchAdminView(): Promise<AdminView> {
  return request<AdminView>("/api/v1/admin/overview");
}

export function fetchAdminDiagnostics(): Promise<AdminDiagnostics> {
  return request<AdminDiagnostics>("/api/v1/admin/diagnostics");
}

export function fetchSetupState(): Promise<SetupConfigurationState> {
  return request<SetupConfigurationState>("/api/v1/setup/state");
}

export function applySetupConfiguration(payload: SetupApplyRequest): Promise<SetupApplyResponse> {
  return request<SetupApplyResponse>("/api/v1/setup/apply", {
    method: "PUT",
    body: JSON.stringify(payload)
  });
}

export function fetchObsidianNotes(limit = 20): Promise<string[]> {
  return request<string[]>(`/api/v1/obsidian/notes?limit=${limit}`);
}

export function fetchObsidianNote(path: string): Promise<ObsidianNoteContent> {
  const encodedPath = encodeURIComponent(path);
  return request<ObsidianNoteContent>(`/api/v1/obsidian/note?path=${encodedPath}`);
}

export function createObsidianNote(payload: ObsidianCreateNotePayload): Promise<ObsidianWriteResponse> {
  return request<ObsidianWriteResponse>("/api/v1/obsidian/note", {
    method: "POST",
    body: JSON.stringify(payload)
  });
}

export function updateObsidianNote(payload: ObsidianUpdateNotePayload): Promise<ObsidianWriteResponse> {
  return request<ObsidianWriteResponse>("/api/v1/obsidian/note", {
    method: "PUT",
    body: JSON.stringify(payload)
  });
}

export function fetchNocoDBBases(): Promise<NocoDBBaseSummary[]> {
  return request<NocoDBBaseSummary[]>("/api/v1/nocodb/bases");
}

export function fetchNocoDBTables(baseId: string): Promise<NocoDBTableSummary[]> {
  return request<NocoDBTableSummary[]>(`/api/v1/nocodb/bases/${encodeURIComponent(baseId)}/tables`);
}

export function fetchNocoDBRows(
  tableId: string,
  options?: { baseId?: string; limit?: number; offset?: number }
): Promise<NocoDBRowsResponse> {
  const params = new URLSearchParams();
  if (options?.baseId) {
    params.set("base_id", options.baseId);
  }
  if (typeof options?.limit === "number") {
    params.set("limit", String(options.limit));
  }
  if (typeof options?.offset === "number") {
    params.set("offset", String(options.offset));
  }
  const query = params.toString();
  const suffix = query ? `?${query}` : "";
  return request<NocoDBRowsResponse>(`/api/v1/nocodb/tables/${encodeURIComponent(tableId)}/rows${suffix}`);
}

export function createNocoDBRow(
  tableId: string,
  payload: NocoDBRowWritePayload
): Promise<NocoDBRowMutationResponse> {
  return request<NocoDBRowMutationResponse>(`/api/v1/nocodb/tables/${encodeURIComponent(tableId)}/rows`, {
    method: "POST",
    body: JSON.stringify(payload)
  });
}

export function updateNocoDBRow(
  tableId: string,
  rowId: string,
  payload: NocoDBRowWritePayload
): Promise<NocoDBRowMutationResponse> {
  return request<NocoDBRowMutationResponse>(
    `/api/v1/nocodb/tables/${encodeURIComponent(tableId)}/rows/${encodeURIComponent(rowId)}`,
    {
      method: "PATCH",
      body: JSON.stringify(payload)
    }
  );
}

export function fetchN8nWorkflows(limit = 25): Promise<N8nWorkflowSummary[]> {
  return request<N8nWorkflowSummary[]>(`/api/v1/n8n/workflows?limit=${limit}`);
}

export function fetchN8nExecutions(limit = 25): Promise<N8nExecutionSummary[]> {
  return request<N8nExecutionSummary[]>(`/api/v1/n8n/executions?limit=${limit}`);
}

export function activateN8nWorkflow(
  workflowId: string,
  payload: N8nWorkflowActionPayload
): Promise<N8nWorkflowActionResponse> {
  return request<N8nWorkflowActionResponse>(`/api/v1/n8n/workflows/${encodeURIComponent(workflowId)}/activate`, {
    method: "POST",
    body: JSON.stringify(payload)
  });
}

export function deactivateN8nWorkflow(
  workflowId: string,
  payload: N8nWorkflowActionPayload
): Promise<N8nWorkflowActionResponse> {
  return request<N8nWorkflowActionResponse>(`/api/v1/n8n/workflows/${encodeURIComponent(workflowId)}/deactivate`, {
    method: "POST",
    body: JSON.stringify(payload)
  });
}

export function runPerplexicaSearch(payload: PerplexicaSearchPayload): Promise<PerplexicaSearchResponse> {
  return request<PerplexicaSearchResponse>("/api/v1/perplexica/search", {
    method: "POST",
    body: JSON.stringify(payload)
  });
}

export function savePerplexicaSearchToNote(
  payload: PerplexicaSearchToNotePayload
): Promise<PerplexicaSearchToNoteResponse> {
  return request<PerplexicaSearchToNoteResponse>("/api/v1/perplexica/search-to-note", {
    method: "POST",
    body: JSON.stringify(payload)
  });
}

export function fetchOpenWebUIModels(): Promise<OpenWebUIModelSummary[]> {
  return request<OpenWebUIModelSummary[]>("/api/v1/openwebui/models");
}

export function runOpenWebUIChat(payload: OpenWebUIChatPayload): Promise<OpenWebUIChatResponse> {
  return request<OpenWebUIChatResponse>("/api/v1/openwebui/chat", {
    method: "POST",
    body: JSON.stringify(payload)
  });
}

export function saveOpenWebUIChatToNote(
  payload: OpenWebUIChatToNotePayload
): Promise<OpenWebUIChatToNoteResponse> {
  return request<OpenWebUIChatToNoteResponse>("/api/v1/openwebui/chat-to-note", {
    method: "POST",
    body: JSON.stringify(payload)
  });
}
