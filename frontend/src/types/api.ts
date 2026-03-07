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
  nocodb_writable_tables: string[];
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

export interface AdminDiagnostics {
  generated_at: string;
  files: Record<string, boolean>;
  paths: Record<string, string>;
  path_checks: Record<string, boolean>;
  tool_health: ToolHealth[];
  recommendations: string[];
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

export interface NocoDBRowWritePayload {
  base_id?: string | null;
  data: Record<string, unknown>;
  confirm_write: boolean;
}

export interface NocoDBRowMutationResponse {
  table_id: string;
  base_id: string | null;
  operation: "create" | "update";
  row: Record<string, unknown>;
}

export interface N8nWorkflowSummary {
  id: string;
  name: string;
  active: boolean;
  updated_at: string | null;
}

export interface N8nExecutionSummary {
  id: string;
  workflow_id: string | null;
  status: string;
  mode: string | null;
  started_at: string | null;
  stopped_at: string | null;
}

export interface N8nWorkflowActionPayload {
  confirm: boolean;
}

export interface N8nWorkflowActionResponse {
  workflow_id: string;
  action: "activate" | "deactivate";
  status: string;
  message: string;
}

export interface PerplexicaSearchPayload {
  query: string;
  focus_mode?: string | null;
  optimization_mode?: string | null;
}

export interface PerplexicaSearchResponse {
  query: string;
  answer: string;
  sources: string[];
  raw: Record<string, unknown>;
}

export interface PerplexicaSearchToNotePayload extends PerplexicaSearchPayload {
  note_path: string;
  create_parents?: boolean;
}

export interface PerplexicaSearchToNoteResponse {
  query: string;
  answer: string;
  sources: string[];
  note_path: string;
  source_count: number;
  bytes_written: number;
  modified_at: string;
}

export interface OpenWebUIModelSummary {
  id: string;
  name: string | null;
}

export interface OpenWebUIChatPayload {
  model: string;
  prompt: string;
  system_prompt?: string | null;
  temperature?: number | null;
  max_tokens?: number | null;
}

export interface OpenWebUIChatResponse {
  model: string;
  answer: string;
  usage: Record<string, unknown> | null;
}

export interface OpenWebUIChatToNotePayload extends OpenWebUIChatPayload {
  note_path: string;
  create_parents?: boolean;
}

export interface OpenWebUIChatToNoteResponse {
  model: string;
  note_path: string;
  answer: string;
  bytes_written: number;
  modified_at: string;
}

export interface SetupRuntimeInput {
  app_name: string;
  app_env: string;
  app_host: string;
  app_port: number;
  log_dir: string;
}

export interface SetupObsidianInput {
  vault_path: string;
  allowed_roots: string[];
}

export interface SetupToolsInput {
  nocodb_base_url: string;
  nocodb_writable_tables: string[];
  n8n_base_url: string;
  perplexica_base_url: string;
  openwebui_base_url: string;
}

export interface SetupSecretsInput {
  nocodb_api_token?: string | null;
  n8n_api_key?: string | null;
  perplexica_api_key?: string | null;
  openwebui_api_key?: string | null;
}

export interface SetupConfigurationState {
  config_file: string;
  env_file: string;
  runtime: SetupRuntimeInput;
  obsidian: SetupObsidianInput;
  tools: SetupToolsInput;
  secret_flags: Record<string, boolean>;
}

export interface SetupApplyRequest {
  runtime: SetupRuntimeInput;
  obsidian: SetupObsidianInput;
  tools: SetupToolsInput;
  secrets: SetupSecretsInput;
  update_secrets: boolean;
}

export interface SetupApplyResponse {
  status: string;
  config_file: string;
  env_file: string;
  updated_env_keys: string[];
  updated_secret_keys: string[];
  warnings: string[];
}
