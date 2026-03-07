import { useState } from "react";
import { PageLayout } from "../components/PageLayout";
import { runPerplexicaSearch, savePerplexicaSearchToNote } from "../lib/api";
import { PerplexicaSearchResponse } from "../types/api";

export function PerplexicaResearch() {
  const [query, setQuery] = useState<string>("");
  const [focusMode, setFocusMode] = useState<string>("webSearch");
  const [optimizationMode, setOptimizationMode] = useState<string>("speed");
  const [notePath, setNotePath] = useState<string>("Research/perplexica-note.md");
  const [createParents, setCreateParents] = useState<boolean>(true);
  const [result, setResult] = useState<PerplexicaSearchResponse | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [info, setInfo] = useState<string | null>(null);
  const [isSearching, setIsSearching] = useState<boolean>(false);
  const [isSaving, setIsSaving] = useState<boolean>(false);

  const runSearch = async () => {
    if (!query.trim()) {
      setError("Query is required.");
      return;
    }
    setIsSearching(true);
    setError(null);
    setInfo(null);
    try {
      const response = await runPerplexicaSearch({
        query: query.trim(),
        focus_mode: focusMode,
        optimization_mode: optimizationMode
      });
      setResult(response);
      setInfo(`Search completed with ${response.sources.length} source(s).`);
    } catch (err) {
      setError((err as Error).message);
    } finally {
      setIsSearching(false);
    }
  };

  const runSearchToNote = async () => {
    if (!query.trim()) {
      setError("Query is required.");
      return;
    }
    if (!notePath.trim()) {
      setError("Note path is required for conversion.");
      return;
    }
    setIsSaving(true);
    setError(null);
    setInfo(null);
    try {
      const response = await savePerplexicaSearchToNote({
        query: query.trim(),
        focus_mode: focusMode,
        optimization_mode: optimizationMode,
        note_path: notePath.trim(),
        create_parents: createParents
      });
      setResult({
        query: response.query,
        answer: response.answer,
        sources: response.sources,
        raw: {}
      });
      setInfo(`Research note created: ${response.note_path}`);
    } catch (err) {
      setError((err as Error).message);
    } finally {
      setIsSaving(false);
    }
  };

  return (
    <PageLayout
      title="Perplexica Research"
      description="Research execution and conversion into reusable knowledge assets."
    >
      <section className="panel">
        <h3>Research query</h3>
        {error ? <p className="error">{error}</p> : null}
        {info ? <p className="success">{info}</p> : null}
        <label className="label" htmlFor="perplexica-query">
          Query
        </label>
        <textarea
          id="perplexica-query"
          className="textarea"
          rows={5}
          value={query}
          onChange={(event) => setQuery(event.target.value)}
        />
        <label className="label" htmlFor="perplexica-focus-mode">
          Focus mode
        </label>
        <input
          id="perplexica-focus-mode"
          className="input"
          value={focusMode}
          onChange={(event) => setFocusMode(event.target.value)}
        />
        <label className="label" htmlFor="perplexica-optimization-mode">
          Optimization mode
        </label>
        <input
          id="perplexica-optimization-mode"
          className="input"
          value={optimizationMode}
          onChange={(event) => setOptimizationMode(event.target.value)}
        />
        <button className="button" type="button" onClick={() => void runSearch()} disabled={isSearching}>
          {isSearching ? "Searching..." : "Run search"}
        </button>
      </section>

      <section className="panel">
        <h3>Convert research to Obsidian note</h3>
        <label className="label" htmlFor="perplexica-note-path">
          Note path
        </label>
        <input
          id="perplexica-note-path"
          className="input"
          value={notePath}
          onChange={(event) => setNotePath(event.target.value)}
        />
        <label className="label">
          <input
            type="checkbox"
            checked={createParents}
            onChange={(event) => setCreateParents(event.target.checked)}
          />{" "}
          Create missing note folders
        </label>
        <button className="button" type="button" onClick={() => void runSearchToNote()} disabled={isSaving}>
          {isSaving ? "Saving..." : "Search and save to note"}
        </button>
      </section>

      <section className="panel">
        <h3>Latest result</h3>
        {!result ? <p>No research result yet.</p> : null}
        {result ? (
          <>
            <p><strong>Query:</strong> {result.query}</p>
            <p><strong>Answer:</strong></p>
            <pre className="command-block">{result.answer || "(empty answer)"}</pre>
            <p><strong>Sources:</strong></p>
            {result.sources.length === 0 ? <p>No sources returned.</p> : null}
            {result.sources.length > 0 ? (
              <ul className="list">
                {result.sources.map((source) => (
                  <li key={source}>
                    <a href={source} target="_blank" rel="noreferrer">{source}</a>
                  </li>
                ))}
              </ul>
            ) : null}
          </>
        ) : null}
      </section>
    </PageLayout>
  );
}
