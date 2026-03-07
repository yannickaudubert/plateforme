import { AdminView, SystemStatus } from "../types/api";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? "http://localhost:8000";

async function request<T>(path: string): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${path}`);
  if (!response.ok) {
    throw new Error(`API error ${response.status}`);
  }
  return response.json() as Promise<T>;
}

export function fetchSystemStatus(): Promise<SystemStatus> {
  return request<SystemStatus>("/api/v1/system/status");
}

export function fetchAdminView(): Promise<AdminView> {
  return request<AdminView>("/api/v1/admin/overview");
}

export function fetchObsidianNotes(limit = 20): Promise<string[]> {
  return request<string[]>(`/api/v1/obsidian/notes?limit=${limit}`);
}
