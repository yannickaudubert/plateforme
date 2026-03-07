export interface ToolHealth {
  tool: string;
  status: "ok" | "degraded";
  message: string;
  checked_at: string;
}

export interface ActionJournalEntry {
  timestamp: string;
  tool: string;
  action: string;
  status: string;
  details: Record<string, unknown>;
}

export interface SystemStatus {
  environment: string;
  tools: ToolHealth[];
  recent_actions: ActionJournalEntry[];
}

export interface AdminView {
  app_name: string;
  environment: string;
  config_file: string;
  obsidian_vault_path: string;
  obsidian_allowed_roots: string[];
  tools: {
    nocodb_base_url: string;
    n8n_base_url: string;
    perplexica_base_url: string;
    openwebui_base_url: string;
  };
  secrets: {
    nocodb_token_set: boolean;
    n8n_api_key_set: boolean;
    perplexica_api_key_set: boolean;
    openwebui_api_key_set: boolean;
  };
}

export interface ObsidianNoteContent {
  path: string;
  content: string;
  frontmatter: Record<string, string>;
  bytes_size: number;
  modified_at: string;
}

export interface ObsidianCreateNotePayload {
  path: string;
  content: string;
  create_parents?: boolean;
}

export interface ObsidianUpdateNotePayload {
  path: string;
  content: string;
  expected_modified_at?: string;
  create_backup?: boolean;
}

export interface ObsidianWriteResponse {
  path: string;
  status: string;
  bytes_written: number;
  modified_at: string;
}

export interface NocoDBBaseSummary {
  id: string;
  title: string;
  type: string | null;
}

export interface NocoDBTableSummary {
  id: string;
  title: string;
  base_id: string;
  type: string | null;
}

export interface NocoDBRowsResponse {
  table_id: string;
  base_id: string | null;
  row_count: number;
  total_rows: number | null;
  rows: Record<string, unknown>[];
}
