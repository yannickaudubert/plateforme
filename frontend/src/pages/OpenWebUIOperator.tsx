import { useEffect, useState } from "react";
import { PageLayout } from "../components/PageLayout";
import { fetchOpenWebUIModels, runOpenWebUIChat, saveOpenWebUIChatToNote } from "../lib/api";
import { OpenWebUIModelSummary } from "../types/api";

export function OpenWebUIOperator() {
  const [models, setModels] = useState<OpenWebUIModelSummary[]>([]);
  const [model, setModel] = useState<string>("");
  const [prompt, setPrompt] = useState<string>("");
  const [systemPrompt, setSystemPrompt] = useState<string>("");
  const [temperature, setTemperature] = useState<number>(0.2);
  const [maxTokens, setMaxTokens] = useState<number>(512);
  const [notePath, setNotePath] = useState<string>("AI/openwebui-chat.md");
  const [createParents, setCreateParents] = useState<boolean>(true);
  const [answer, setAnswer] = useState<string>("");
  const [error, setError] = useState<string | null>(null);
  const [info, setInfo] = useState<string | null>(null);
  const [isLoadingModels, setIsLoadingModels] = useState<boolean>(false);
  const [isSendingChat, setIsSendingChat] = useState<boolean>(false);
  const [isSavingNote, setIsSavingNote] = useState<boolean>(false);

  const loadModels = async () => {
    setIsLoadingModels(true);
    setError(null);
    setInfo(null);
    try {
      const data = await fetchOpenWebUIModels();
      setModels(data);
      if (!data.find((item) => item.id === model)) {
        setModel(data[0]?.id ?? "");
      }
      setInfo(`Loaded ${data.length} model(s).`);
    } catch (err) {
      setError((err as Error).message);
    } finally {
      setIsLoadingModels(false);
    }
  };

  useEffect(() => {
    void loadModels();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const runChat = async () => {
    if (!model.trim() || !prompt.trim()) {
      setError("Model and prompt are required.");
      return;
    }
    setIsSendingChat(true);
    setError(null);
    setInfo(null);
    try {
      const response = await runOpenWebUIChat({
        model: model.trim(),
        prompt: prompt.trim(),
        system_prompt: systemPrompt.trim() || null,
        temperature,
        max_tokens: maxTokens
      });
      setAnswer(response.answer);
      setInfo(`Chat completed with model ${response.model}.`);
    } catch (err) {
      setError((err as Error).message);
    } finally {
      setIsSendingChat(false);
    }
  };

  const chatToNote = async () => {
    if (!model.trim() || !prompt.trim() || !notePath.trim()) {
      setError("Model, prompt and note path are required.");
      return;
    }
    setIsSavingNote(true);
    setError(null);
    setInfo(null);
    try {
      const response = await saveOpenWebUIChatToNote({
        model: model.trim(),
        prompt: prompt.trim(),
        system_prompt: systemPrompt.trim() || null,
        temperature,
        max_tokens: maxTokens,
        note_path: notePath.trim(),
        create_parents: createParents
      });
      setAnswer(response.answer);
      setInfo(`Chat note created: ${response.note_path}`);
    } catch (err) {
      setError((err as Error).message);
    } finally {
      setIsSavingNote(false);
    }
  };

  return (
    <PageLayout
      title="Open WebUI Operator"
      description="Operator AI interactions with model selection and note conversion."
    >
      <section className="panel">
        <h3>Chat operations</h3>
        {error ? <p className="error">{error}</p> : null}
        {info ? <p className="success">{info}</p> : null}
        <button className="button" type="button" onClick={() => void loadModels()} disabled={isLoadingModels}>
          {isLoadingModels ? "Loading models..." : "Refresh models"}
        </button>

        <label className="label" htmlFor="openwebui-model-select">
          Model
        </label>
        <select
          id="openwebui-model-select"
          className="input"
          value={model}
          onChange={(event) => setModel(event.target.value)}
          disabled={models.length === 0 || isLoadingModels}
        >
          {models.map((item) => (
            <option key={item.id} value={item.id}>
              {item.name ? `${item.name} (${item.id})` : item.id}
            </option>
          ))}
        </select>

        <label className="label" htmlFor="openwebui-system-prompt">
          System prompt
        </label>
        <textarea
          id="openwebui-system-prompt"
          className="textarea"
          rows={3}
          value={systemPrompt}
          onChange={(event) => setSystemPrompt(event.target.value)}
        />

        <label className="label" htmlFor="openwebui-prompt">
          User prompt
        </label>
        <textarea
          id="openwebui-prompt"
          className="textarea"
          rows={6}
          value={prompt}
          onChange={(event) => setPrompt(event.target.value)}
        />

        <label className="label" htmlFor="openwebui-temperature">
          Temperature
        </label>
        <input
          id="openwebui-temperature"
          className="input"
          type="number"
          min={0}
          max={2}
          step={0.1}
          value={temperature}
          onChange={(event) => setTemperature(Number(event.target.value) || 0)}
        />

        <label className="label" htmlFor="openwebui-max-tokens">
          Max tokens
        </label>
        <input
          id="openwebui-max-tokens"
          className="input"
          type="number"
          min={1}
          max={8192}
          value={maxTokens}
          onChange={(event) => setMaxTokens(Number(event.target.value) || 256)}
        />

        <button className="button" type="button" onClick={() => void runChat()} disabled={isSendingChat}>
          {isSendingChat ? "Running..." : "Run chat"}
        </button>
      </section>

      <section className="panel">
        <h3>Save chat to Obsidian note</h3>
        <label className="label" htmlFor="openwebui-note-path">
          Note path
        </label>
        <input
          id="openwebui-note-path"
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
        <button className="button" type="button" onClick={() => void chatToNote()} disabled={isSavingNote}>
          {isSavingNote ? "Saving..." : "Chat and save to note"}
        </button>
      </section>

      <section className="panel">
        <h3>Latest answer</h3>
        {!answer ? <p>No answer generated yet.</p> : <pre className="command-block">{answer}</pre>}
      </section>
    </PageLayout>
  );
}
