import { useEffect, useState } from "react";
import { PageLayout } from "../components/PageLayout";
import { applySetupConfiguration, fetchSetupState } from "../lib/api";
import {
  SetupApplyResponse,
  SetupConfigurationState,
  SetupSecretsInput
} from "../types/api";

type Language = "fr" | "en";

const TEXT = {
  en: {
    title: "Setup Wizard",
    description: "Step-by-step configuration assistant for operator deployment.",
    steps: ["Language", "Runtime & Paths", "Tool Endpoints", "Secrets", "Review & Apply"],
    languageLabel: "Language",
    refresh: "Reload state",
    loading: "Loading setup state...",
    previous: "Previous",
    next: "Next",
    apply: "Apply configuration",
    runtime: "Runtime",
    appName: "App name",
    appEnv: "Environment",
    appHost: "Host",
    appPort: "Port",
    logDir: "Log directory",
    obsidian: "Obsidian",
    vaultPath: "Vault path",
    allowedRoots: "Allowed roots (comma separated)",
    tools: "Tool endpoints",
    nocodb: "NocoDB base URL",
    nocodbWritableTables: "Writable NocoDB tables (comma separated IDs, optional)",
    n8n: "n8n base URL",
    perplexica: "Perplexica base URL",
    openwebui: "Open WebUI base URL",
    secrets: "Secrets",
    updateSecrets: "Apply non-empty secret values",
    nocodbToken: "NocoDB API token",
    n8nKey: "n8n API key",
    perplexicaKey: "Perplexica API key",
    openwebuiKey: "Open WebUI API key",
    review: "Review",
    configFile: "Config file",
    envFile: "Env file",
    success: "Configuration applied.",
    noWarnings: "No warnings.",
    invalidStep: "Complete required fields before continuing."
  },
  fr: {
    title: "Assistant de configuration",
    description: "Assistant pas a pas pour parametrer le cockpit et le deploiement.",
    steps: ["Langue", "Runtime et chemins", "Endpoints outils", "Secrets", "Revision et application"],
    languageLabel: "Langue",
    refresh: "Recharger l'etat",
    loading: "Chargement de la configuration...",
    previous: "Precedent",
    next: "Suivant",
    apply: "Appliquer la configuration",
    runtime: "Runtime",
    appName: "Nom application",
    appEnv: "Environnement",
    appHost: "Host",
    appPort: "Port",
    logDir: "Dossier logs",
    obsidian: "Obsidian",
    vaultPath: "Chemin vault",
    allowedRoots: "Racines autorisees (separees par virgule)",
    tools: "Endpoints outils",
    nocodb: "URL NocoDB",
    nocodbWritableTables: "Tables NocoDB ecrivable (IDs separes par virgule, optionnel)",
    n8n: "URL n8n",
    perplexica: "URL Perplexica",
    openwebui: "URL Open WebUI",
    secrets: "Secrets",
    updateSecrets: "Appliquer les secrets non vides",
    nocodbToken: "Token API NocoDB",
    n8nKey: "Cle API n8n",
    perplexicaKey: "Cle API Perplexica",
    openwebuiKey: "Cle API Open WebUI",
    review: "Revision",
    configFile: "Fichier config",
    envFile: "Fichier env",
    success: "Configuration appliquee.",
    noWarnings: "Aucun avertissement.",
    invalidStep: "Completer les champs requis avant de continuer."
  }
} as const;

export function SetupWizard() {
  const [language, setLanguage] = useState<Language>("fr");
  const [step, setStep] = useState<number>(0);
  const [state, setState] = useState<SetupConfigurationState | null>(null);
  const [secrets, setSecrets] = useState<SetupSecretsInput>({});
  const [allowedRootsText, setAllowedRootsText] = useState<string>("");
  const [nocodbWritableTablesText, setNocodbWritableTablesText] = useState<string>("");
  const [updateSecrets, setUpdateSecrets] = useState<boolean>(true);
  const [applyResult, setApplyResult] = useState<SetupApplyResponse | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [isApplying, setIsApplying] = useState<boolean>(false);

  const t = TEXT[language];

  const loadState = async () => {
    setIsLoading(true);
    setError(null);
    try {
      const payload = await fetchSetupState();
      setState(payload);
      setAllowedRootsText(payload.obsidian.allowed_roots.join(","));
      setNocodbWritableTablesText(payload.tools.nocodb_writable_tables.join(","));
    } catch (err) {
      setError((err as Error).message);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    void loadState();
  }, []);

  const validateCurrentStep = (): boolean => {
    if (!state) {
      return false;
    }
    if (step === 1) {
      return Boolean(state.runtime.app_name.trim()) && Boolean(state.obsidian.vault_path.trim()) && Boolean(allowedRootsText.trim());
    }
    if (step === 2) {
      return (
        Boolean(state.tools.nocodb_base_url.trim()) &&
        Boolean(state.tools.n8n_base_url.trim()) &&
        Boolean(state.tools.perplexica_base_url.trim()) &&
        Boolean(state.tools.openwebui_base_url.trim())
      );
    }
    return true;
  };

  const onNext = () => {
    if (!validateCurrentStep()) {
      setError(t.invalidStep);
      return;
    }
    setError(null);
    setStep((current) => Math.min(current + 1, t.steps.length - 1));
  };

  const onPrevious = () => {
    setError(null);
    setStep((current) => Math.max(current - 1, 0));
  };

  const onApply = async () => {
    if (!state) {
      return;
    }
    setIsApplying(true);
    setError(null);
    setApplyResult(null);
    try {
      const cleanedWritableTables = nocodbWritableTablesText
        .split(",")
        .map((item) => item.trim())
        .filter(Boolean);
      const payload = {
        runtime: state.runtime,
        obsidian: {
          vault_path: state.obsidian.vault_path,
          allowed_roots: allowedRootsText.split(",").map((item) => item.trim()).filter(Boolean)
        },
        tools: {
          ...state.tools,
          nocodb_writable_tables: cleanedWritableTables
        },
        secrets,
        update_secrets: updateSecrets
      };
      const result = await applySetupConfiguration(payload);
      setApplyResult(result);
      await loadState();
    } catch (err) {
      setError((err as Error).message);
    } finally {
      setIsApplying(false);
    }
  };

  return (
    <PageLayout title={t.title} description={t.description}>
      <section className="panel">
        <label className="label" htmlFor="wizard-language">{t.languageLabel}</label>
        <select
          id="wizard-language"
          className="input"
          value={language}
          onChange={(event) => setLanguage(event.target.value as Language)}
        >
          <option value="fr">Francais</option>
          <option value="en">English</option>
        </select>
        <button className="button" onClick={() => void loadState()} type="button">{t.refresh}</button>
      </section>

      {error ? <p className="error">{error}</p> : null}
      {applyResult ? (
        <section className="panel">
          <p className="success">{t.success}</p>
          <p>{t.configFile}: {applyResult.config_file}</p>
          <p>{t.envFile}: {applyResult.env_file}</p>
          <p>Updated env keys: {applyResult.updated_env_keys.length}</p>
          <p>Updated secret keys: {applyResult.updated_secret_keys.length}</p>
          <p>{applyResult.warnings.length > 0 ? applyResult.warnings.join(" | ") : t.noWarnings}</p>
        </section>
      ) : null}

      {!state || isLoading ? <p>{t.loading}</p> : null}
      {state ? (
        <section className="panel">
          <div className="wizard-steps">
            {t.steps.map((label, index) => (
              <span key={label} className={index === step ? "wizard-step wizard-step-active" : "wizard-step"}>
                {index + 1}. {label}
              </span>
            ))}
          </div>

          {step === 0 ? (
            <div>
              <p>{language === "fr" ? "Choisissez la langue puis continuez." : "Select language then continue."}</p>
            </div>
          ) : null}

          {step === 1 ? (
            <div>
              <h3>{t.runtime}</h3>
              <label className="label">{t.appName}</label>
              <input
                className="input"
                value={state.runtime.app_name}
                onChange={(event) =>
                  setState({
                    ...state,
                    runtime: { ...state.runtime, app_name: event.target.value }
                  })
                }
              />
              <label className="label">{t.appEnv}</label>
              <input
                className="input"
                value={state.runtime.app_env}
                onChange={(event) =>
                  setState({
                    ...state,
                    runtime: { ...state.runtime, app_env: event.target.value }
                  })
                }
              />
              <label className="label">{t.appHost}</label>
              <input
                className="input"
                value={state.runtime.app_host}
                onChange={(event) =>
                  setState({
                    ...state,
                    runtime: { ...state.runtime, app_host: event.target.value }
                  })
                }
              />
              <label className="label">{t.appPort}</label>
              <input
                className="input"
                type="number"
                min={1}
                max={65535}
                value={state.runtime.app_port}
                onChange={(event) =>
                  setState({
                    ...state,
                    runtime: { ...state.runtime, app_port: Number(event.target.value) || 8000 }
                  })
                }
              />
              <label className="label">{t.logDir}</label>
              <input
                className="input"
                value={state.runtime.log_dir}
                onChange={(event) =>
                  setState({
                    ...state,
                    runtime: { ...state.runtime, log_dir: event.target.value }
                  })
                }
              />

              <h3>{t.obsidian}</h3>
              <label className="label">{t.vaultPath}</label>
              <input
                className="input"
                value={state.obsidian.vault_path}
                onChange={(event) =>
                  setState({
                    ...state,
                    obsidian: { ...state.obsidian, vault_path: event.target.value }
                  })
                }
              />
              <label className="label">{t.allowedRoots}</label>
              <input
                className="input"
                value={allowedRootsText}
                onChange={(event) => setAllowedRootsText(event.target.value)}
              />
            </div>
          ) : null}

          {step === 2 ? (
            <div>
              <h3>{t.tools}</h3>
              <label className="label">{t.nocodb}</label>
              <input
                className="input"
                value={state.tools.nocodb_base_url}
                onChange={(event) =>
                  setState({
                    ...state,
                    tools: { ...state.tools, nocodb_base_url: event.target.value }
                  })
                }
              />
              <label className="label">{t.nocodbWritableTables}</label>
              <input
                className="input"
                value={nocodbWritableTablesText}
                onChange={(event) => setNocodbWritableTablesText(event.target.value)}
              />
              <label className="label">{t.n8n}</label>
              <input
                className="input"
                value={state.tools.n8n_base_url}
                onChange={(event) =>
                  setState({
                    ...state,
                    tools: { ...state.tools, n8n_base_url: event.target.value }
                  })
                }
              />
              <label className="label">{t.perplexica}</label>
              <input
                className="input"
                value={state.tools.perplexica_base_url}
                onChange={(event) =>
                  setState({
                    ...state,
                    tools: { ...state.tools, perplexica_base_url: event.target.value }
                  })
                }
              />
              <label className="label">{t.openwebui}</label>
              <input
                className="input"
                value={state.tools.openwebui_base_url}
                onChange={(event) =>
                  setState({
                    ...state,
                    tools: { ...state.tools, openwebui_base_url: event.target.value }
                  })
                }
              />
            </div>
          ) : null}

          {step === 3 ? (
            <div>
              <h3>{t.secrets}</h3>
              <label className="label">
                <input
                  type="checkbox"
                  checked={updateSecrets}
                  onChange={(event) => setUpdateSecrets(event.target.checked)}
                />{" "}
                {t.updateSecrets}
              </label>
              <label className="label">{t.nocodbToken}</label>
              <input
                className="input"
                type="password"
                value={secrets.nocodb_api_token ?? ""}
                onChange={(event) =>
                  setSecrets({ ...secrets, nocodb_api_token: event.target.value })
                }
              />
              <label className="label">{t.n8nKey}</label>
              <input
                className="input"
                type="password"
                value={secrets.n8n_api_key ?? ""}
                onChange={(event) => setSecrets({ ...secrets, n8n_api_key: event.target.value })}
              />
              <label className="label">{t.perplexicaKey}</label>
              <input
                className="input"
                type="password"
                value={secrets.perplexica_api_key ?? ""}
                onChange={(event) =>
                  setSecrets({ ...secrets, perplexica_api_key: event.target.value })
                }
              />
              <label className="label">{t.openwebuiKey}</label>
              <input
                className="input"
                type="password"
                value={secrets.openwebui_api_key ?? ""}
                onChange={(event) =>
                  setSecrets({ ...secrets, openwebui_api_key: event.target.value })
                }
              />
            </div>
          ) : null}

          {step === 4 ? (
            <div>
              <h3>{t.review}</h3>
              <p>{t.configFile}: {state.config_file}</p>
              <p>{t.envFile}: {state.env_file}</p>
              <p>{t.appName}: {state.runtime.app_name}</p>
              <p>{t.vaultPath}: {state.obsidian.vault_path}</p>
              <p>{t.nocodb}: {state.tools.nocodb_base_url}</p>
              <p>{t.nocodbWritableTables}: {nocodbWritableTablesText || "-"}</p>
              <p>{t.n8n}: {state.tools.n8n_base_url}</p>
              <p>{t.perplexica}: {state.tools.perplexica_base_url}</p>
              <p>{t.openwebui}: {state.tools.openwebui_base_url}</p>
            </div>
          ) : null}

          <div className="wizard-actions">
            <button className="button" type="button" onClick={onPrevious} disabled={step === 0}>
              {t.previous}
            </button>
            {step < t.steps.length - 1 ? (
              <button className="button" type="button" onClick={onNext}>
                {t.next}
              </button>
            ) : (
              <button className="button" type="button" onClick={() => void onApply()} disabled={isApplying}>
                {isApplying ? "..." : t.apply}
              </button>
            )}
          </div>
        </section>
      ) : null}
    </PageLayout>
  );
}
