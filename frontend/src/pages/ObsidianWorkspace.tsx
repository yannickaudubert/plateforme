import { useEffect, useState } from "react";
import { PageLayout } from "../components/PageLayout";
import {
  createObsidianNote,
  fetchObsidianNote,
  fetchObsidianNotes,
  updateObsidianNote
} from "../lib/api";
import { ObsidianNoteContent } from "../types/api";

export function ObsidianWorkspace() {
  const [notes, setNotes] = useState<string[]>([]);
  const [selectedPath, setSelectedPath] = useState<string>("");
  const [selectedNote, setSelectedNote] = useState<ObsidianNoteContent | null>(null);
  const [editableContent, setEditableContent] = useState<string>("");
  const [newPath, setNewPath] = useState<string>("");
  const [newContent, setNewContent] = useState<string>("");
  const [error, setError] = useState<string | null>(null);
  const [info, setInfo] = useState<string | null>(null);
  const [isLoadingNote, setIsLoadingNote] = useState<boolean>(false);
  const [isSubmitting, setIsSubmitting] = useState<boolean>(false);

  const loadNotes = () => {
    setError(null);
    fetchObsidianNotes(25)
      .then(setNotes)
      .catch((err: Error) => setError(err.message));
  };

  useEffect(() => {
    loadNotes();
  }, []);

  const loadNote = async (path: string): Promise<void> => {
    setSelectedPath(path);
    setInfo(null);
    setError(null);
    setSelectedNote(null);
    setIsLoadingNote(true);
    try {
      const note = await fetchObsidianNote(path);
      setSelectedNote(note);
      setEditableContent(note.content);
    } catch (err) {
      setError((err as Error).message);
      setEditableContent("");
    } finally {
      setIsLoadingNote(false);
    }
  };

  const handleSelectNote = (path: string) => {
    void loadNote(path);
  };

  const handleUpdateNote = async () => {
    if (!selectedPath) {
      return;
    }
    if (!window.confirm("Confirm note update in Obsidian vault?")) {
      return;
    }
    setIsSubmitting(true);
    setInfo(null);
    setError(null);
    try {
      const response = await updateObsidianNote({
        path: selectedPath,
        content: editableContent,
        expected_modified_at: selectedNote?.modified_at,
        create_backup: true
      });
      setInfo(`Updated ${response.path} (${response.bytes_written} bytes)`);
      await loadNote(selectedPath);
      loadNotes();
    } catch (err) {
      setError((err as Error).message);
    } finally {
      setIsSubmitting(false);
    }
  };

  const handleCreateNote = async () => {
    if (!newPath.trim()) {
      setError("Path is required");
      return;
    }
    setIsSubmitting(true);
    setInfo(null);
    setError(null);
    try {
      const response = await createObsidianNote({
        path: newPath.trim(),
        content: newContent,
        create_parents: true
      });
      setInfo(`Created ${response.path} (${response.bytes_written} bytes)`);
      setNewPath("");
      setNewContent("");
      loadNotes();
      await loadNote(response.path);
    } catch (err) {
      setError((err as Error).message);
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <PageLayout
      title="Obsidian Workspace"
      description="Canonical documentary workspace over the Obsidian vault."
    >
      {error ? <p className="error">{error}</p> : null}
      {info ? <p className="success">{info}</p> : null}
      <section className="panel">
        <h3>Vault snapshot</h3>
        <button className="button" onClick={loadNotes} type="button">
          Refresh list
        </button>
        {!error && notes.length === 0 ? <p>No markdown files found.</p> : null}
        {notes.length > 0 ? (
          <ul className="list">
            {notes.map((note) => (
              <li key={note}>
                <button
                  className={note === selectedPath ? "note-link note-link-active" : "note-link"}
                  onClick={() => handleSelectNote(note)}
                  type="button"
                >
                  {note}
                </button>
              </li>
            ))}
          </ul>
        ) : null}
      </section>
      <section className="panel">
        <h3>Selected note</h3>
        {!selectedPath ? <p>Select a note from the list.</p> : null}
        {isLoadingNote ? <p>Loading note...</p> : null}
        {selectedNote ? (
          <>
            <p>
              <strong>Path:</strong> {selectedNote.path}
            </p>
            <p>
              <strong>Last modified:</strong> {new Date(selectedNote.modified_at).toLocaleString()}
            </p>
            <h4>Frontmatter</h4>
            {Object.keys(selectedNote.frontmatter).length === 0 ? (
              <p>No frontmatter detected.</p>
            ) : (
              <ul className="list">
                {Object.entries(selectedNote.frontmatter).map(([key, value]) => (
                  <li key={key}>
                    <strong>{key}:</strong> {value}
                  </li>
                ))}
              </ul>
            )}
            <h4>Content</h4>
            <textarea
              className="textarea"
              value={editableContent}
              onChange={(event) => setEditableContent(event.target.value)}
              rows={16}
            />
            <button className="button" onClick={handleUpdateNote} type="button" disabled={isSubmitting}>
              Save note
            </button>
          </>
        ) : null}
      </section>
      <section className="panel">
        <h3>Create note</h3>
        <label className="label" htmlFor="new-note-path">
          Relative path (.md)
        </label>
        <input
          id="new-note-path"
          className="input"
          placeholder="projects/mission-001.md"
          value={newPath}
          onChange={(event) => setNewPath(event.target.value)}
        />
        <label className="label" htmlFor="new-note-content">
          Content
        </label>
        <textarea
          id="new-note-content"
          className="textarea"
          value={newContent}
          onChange={(event) => setNewContent(event.target.value)}
          rows={10}
        />
        <button className="button" onClick={handleCreateNote} type="button" disabled={isSubmitting}>
          Create note
        </button>
      </section>
    </PageLayout>
  );
}
