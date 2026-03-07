import { useEffect, useState } from "react";
import { PageLayout } from "../components/PageLayout";
import { createNocoDBRow, fetchNocoDBBases, fetchNocoDBRows, fetchNocoDBTables, updateNocoDBRow } from "../lib/api";
import { NocoDBBaseSummary, NocoDBRowsResponse, NocoDBTableSummary } from "../types/api";

function parseJsonRecord(raw: string): Record<string, unknown> {
  const parsed = JSON.parse(raw) as unknown;
  if (!parsed || typeof parsed !== "object" || Array.isArray(parsed)) {
    throw new Error("Payload must be a JSON object");
  }
  return parsed as Record<string, unknown>;
}

export function NocoDBControl() {
  const [bases, setBases] = useState<NocoDBBaseSummary[]>([]);
  const [tables, setTables] = useState<NocoDBTableSummary[]>([]);
  const [rowsResponse, setRowsResponse] = useState<NocoDBRowsResponse | null>(null);
  const [selectedBaseId, setSelectedBaseId] = useState<string>("");
  const [selectedTableId, setSelectedTableId] = useState<string>("");
  const [limit, setLimit] = useState<number>(25);
  const [error, setError] = useState<string | null>(null);
  const [info, setInfo] = useState<string | null>(null);
  const [isLoadingBases, setIsLoadingBases] = useState<boolean>(false);
  const [isLoadingTables, setIsLoadingTables] = useState<boolean>(false);
  const [isLoadingRows, setIsLoadingRows] = useState<boolean>(false);
  const [createPayloadText, setCreatePayloadText] = useState<string>('{"Title": "Example"}');
  const [updateRowId, setUpdateRowId] = useState<string>("");
  const [updatePayloadText, setUpdatePayloadText] = useState<string>('{"Title": "Updated"}');
  const [confirmCreate, setConfirmCreate] = useState<boolean>(false);
  const [confirmUpdate, setConfirmUpdate] = useState<boolean>(false);
  const [isCreatingRow, setIsCreatingRow] = useState<boolean>(false);
  const [isUpdatingRow, setIsUpdatingRow] = useState<boolean>(false);

  const loadBases = async () => {
    setIsLoadingBases(true);
    setError(null);
    setInfo(null);
    try {
      const nextBases = await fetchNocoDBBases();
      setBases(nextBases);
      if (nextBases.length === 0) {
        setSelectedBaseId("");
        setTables([]);
        setSelectedTableId("");
        setRowsResponse(null);
        setInfo("No NocoDB bases found for current token.");
      } else if (!nextBases.find((base) => base.id === selectedBaseId)) {
        const firstBaseId = nextBases[0].id;
        setSelectedBaseId(firstBaseId);
      }
    } catch (err) {
      setError((err as Error).message);
    } finally {
      setIsLoadingBases(false);
    }
  };

  const loadTables = async (baseId: string) => {
    if (!baseId) {
      setTables([]);
      setSelectedTableId("");
      setRowsResponse(null);
      return;
    }
    setIsLoadingTables(true);
    setError(null);
    setInfo(null);
    setRowsResponse(null);
    try {
      const nextTables = await fetchNocoDBTables(baseId);
      setTables(nextTables);
      if (nextTables.length === 0) {
        setSelectedTableId("");
        setInfo("No tables found in selected base.");
      } else if (!nextTables.find((table) => table.id === selectedTableId)) {
        setSelectedTableId(nextTables[0].id);
      }
    } catch (err) {
      setError((err as Error).message);
      setTables([]);
      setSelectedTableId("");
    } finally {
      setIsLoadingTables(false);
    }
  };

  const loadRows = async (tableId: string, baseId: string) => {
    if (!tableId) {
      setRowsResponse(null);
      return;
    }
    setIsLoadingRows(true);
    setError(null);
    setInfo(null);
    try {
      const response = await fetchNocoDBRows(tableId, {
        baseId: baseId || undefined,
        limit,
        offset: 0
      });
      setRowsResponse(response);
      setInfo(`Loaded ${response.row_count} row(s)${response.total_rows !== null ? ` / total ${response.total_rows}` : ""}.`);
    } catch (err) {
      setError((err as Error).message);
      setRowsResponse(null);
    } finally {
      setIsLoadingRows(false);
    }
  };

  useEffect(() => {
    void loadBases();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  useEffect(() => {
    void loadTables(selectedBaseId);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [selectedBaseId]);

  const createRow = async () => {
    if (!selectedTableId) {
      return;
    }
    setIsCreatingRow(true);
    setError(null);
    setInfo(null);
    try {
      const data = parseJsonRecord(createPayloadText);
      const result = await createNocoDBRow(selectedTableId, {
        base_id: selectedBaseId || null,
        data,
        confirm_write: confirmCreate
      });
      setInfo(`Row created on table ${result.table_id}.`);
      await loadRows(selectedTableId, selectedBaseId);
    } catch (err) {
      setError((err as Error).message);
    } finally {
      setIsCreatingRow(false);
    }
  };

  const updateRow = async () => {
    if (!selectedTableId || !updateRowId.trim()) {
      setError("Table ID and row ID are required for update.");
      return;
    }
    setIsUpdatingRow(true);
    setError(null);
    setInfo(null);
    try {
      const data = parseJsonRecord(updatePayloadText);
      const result = await updateNocoDBRow(selectedTableId, updateRowId.trim(), {
        base_id: selectedBaseId || null,
        data,
        confirm_write: confirmUpdate
      });
      setInfo(`Row ${updateRowId.trim()} updated on table ${result.table_id}.`);
      await loadRows(selectedTableId, selectedBaseId);
    } catch (err) {
      setError((err as Error).message);
    } finally {
      setIsUpdatingRow(false);
    }
  };

  const columns = rowsResponse && rowsResponse.rows.length > 0 ? Object.keys(rowsResponse.rows[0]) : [];

  return (
    <PageLayout
      title="NocoDB Control"
      description="Structured transverse data control with base, table, and row reads."
    >
      {error ? <p className="error">{error}</p> : null}
      {info ? <p className="success">{info}</p> : null}

      <section className="panel">
        <h3>Source selection</h3>
        <button className="button" onClick={() => void loadBases()} type="button" disabled={isLoadingBases}>
          {isLoadingBases ? "Loading bases..." : "Refresh bases"}
        </button>

        <label className="label" htmlFor="nocodb-base-select">
          Base
        </label>
        <select
          id="nocodb-base-select"
          className="input"
          value={selectedBaseId}
          onChange={(event) => setSelectedBaseId(event.target.value)}
          disabled={isLoadingBases || bases.length === 0}
        >
          {bases.map((base) => (
            <option key={base.id} value={base.id}>
              {base.title} ({base.id})
            </option>
          ))}
        </select>

        <button
          className="button"
          onClick={() => void loadTables(selectedBaseId)}
          type="button"
          disabled={isLoadingTables || !selectedBaseId}
        >
          {isLoadingTables ? "Loading tables..." : "Refresh tables"}
        </button>

        <label className="label" htmlFor="nocodb-table-select">
          Table
        </label>
        <select
          id="nocodb-table-select"
          className="input"
          value={selectedTableId}
          onChange={(event) => setSelectedTableId(event.target.value)}
          disabled={isLoadingTables || tables.length === 0}
        >
          {tables.map((table) => (
            <option key={table.id} value={table.id}>
              {table.title} ({table.id})
            </option>
          ))}
        </select>

        <label className="label" htmlFor="nocodb-row-limit">
          Row limit
        </label>
        <input
          id="nocodb-row-limit"
          className="input"
          type="number"
          min={1}
          max={200}
          value={limit}
          onChange={(event) => {
            const next = Number(event.target.value);
            if (Number.isFinite(next)) {
              setLimit(Math.max(1, Math.min(200, next)));
            }
          }}
        />

        <button
          className="button"
          onClick={() => void loadRows(selectedTableId, selectedBaseId)}
          type="button"
          disabled={isLoadingRows || !selectedTableId}
        >
          {isLoadingRows ? "Loading rows..." : "Load rows"}
        </button>
      </section>

      <section className="panel">
        <h3>Rows preview</h3>
        {!rowsResponse ? <p>No rows loaded yet.</p> : null}
        {rowsResponse && rowsResponse.row_count === 0 ? <p>No rows returned.</p> : null}
        {rowsResponse && rowsResponse.row_count > 0 ? (
          <div className="table-scroll">
            <table className="data-table">
              <thead>
                <tr>
                  {columns.map((column) => (
                    <th key={column}>{column}</th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {rowsResponse.rows.map((row, index) => (
                  <tr key={`${index}-${String(row[columns[0] ?? ""])}`}>
                    {columns.map((column) => (
                      <td key={`${index}-${column}`}>{String(row[column] ?? "")}</td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        ) : null}
      </section>

      <section className="panel">
        <h3>Safe write actions</h3>
        <p>
          Write operations require both confirmation and backend allowlist (`NOCODB_WRITABLE_TABLES`).
        </p>

        <h4>Create row</h4>
        <label className="label" htmlFor="nocodb-create-payload">
          JSON payload
        </label>
        <textarea
          id="nocodb-create-payload"
          className="textarea"
          rows={6}
          value={createPayloadText}
          onChange={(event) => setCreatePayloadText(event.target.value)}
        />
        <label className="label">
          <input
            type="checkbox"
            checked={confirmCreate}
            onChange={(event) => setConfirmCreate(event.target.checked)}
          />{" "}
          Confirm create write
        </label>
        <button
          className="button"
          type="button"
          onClick={() => void createRow()}
          disabled={isCreatingRow || !selectedTableId}
        >
          {isCreatingRow ? "Creating..." : "Create row"}
        </button>

        <h4>Update row</h4>
        <label className="label" htmlFor="nocodb-update-row-id">
          Row ID
        </label>
        <input
          id="nocodb-update-row-id"
          className="input"
          value={updateRowId}
          onChange={(event) => setUpdateRowId(event.target.value)}
        />
        <label className="label" htmlFor="nocodb-update-payload">
          JSON payload
        </label>
        <textarea
          id="nocodb-update-payload"
          className="textarea"
          rows={6}
          value={updatePayloadText}
          onChange={(event) => setUpdatePayloadText(event.target.value)}
        />
        <label className="label">
          <input
            type="checkbox"
            checked={confirmUpdate}
            onChange={(event) => setConfirmUpdate(event.target.checked)}
          />{" "}
          Confirm update write
        </label>
        <button
          className="button"
          type="button"
          onClick={() => void updateRow()}
          disabled={isUpdatingRow || !selectedTableId || !updateRowId.trim()}
        >
          {isUpdatingRow ? "Updating..." : "Update row"}
        </button>
      </section>
    </PageLayout>
  );
}
