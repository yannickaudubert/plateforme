import {
  AdminDiagnostics,
  AdminView,
  NocoDBBaseSummary,
  NocoDBRowsResponse,
  NocoDBTableSummary,
  ObsidianCreateNotePayload,
  ObsidianNoteContent,
  ObsidianUpdateNotePayload,
  ObsidianWriteResponse,
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
