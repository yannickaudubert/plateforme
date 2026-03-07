import { NavLink, Route, Routes } from "react-router-dom";
import { Home } from "./pages/Home";
import { ObsidianWorkspace } from "./pages/ObsidianWorkspace";
import { NocoDBControl } from "./pages/NocoDBControl";
import { N8nOrchestrator } from "./pages/N8nOrchestrator";
import { PerplexicaResearch } from "./pages/PerplexicaResearch";
import { OpenWebUIOperator } from "./pages/OpenWebUIOperator";
import { Administration } from "./pages/Administration";
import { SetupWizard } from "./pages/SetupWizard";

const navItems = [
  { path: "/", label: "Home" },
  { path: "/obsidian", label: "Obsidian Workspace" },
  { path: "/nocodb", label: "NocoDB Control" },
  { path: "/n8n", label: "n8n Orchestrator" },
  { path: "/perplexica", label: "Perplexica Research" },
  { path: "/openwebui", label: "Open WebUI Operator" },
  { path: "/setup", label: "Setup Wizard" },
  { path: "/admin", label: "Administration" }
];

function App() {
  return (
    <div className="app-shell">
      <aside className="sidebar">
        <h1>Cockpit OS</h1>
        <p>DSI Transverse</p>
        <nav>
          {navItems.map((item) => (
            <NavLink
              key={item.path}
              className={({ isActive }) =>
                isActive ? "nav-link nav-link-active" : "nav-link"
              }
              to={item.path}
              end={item.path === "/"}
            >
              {item.label}
            </NavLink>
          ))}
        </nav>
      </aside>
      <main className="main-content">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/obsidian" element={<ObsidianWorkspace />} />
          <Route path="/nocodb" element={<NocoDBControl />} />
          <Route path="/n8n" element={<N8nOrchestrator />} />
          <Route path="/perplexica" element={<PerplexicaResearch />} />
          <Route path="/openwebui" element={<OpenWebUIOperator />} />
          <Route path="/setup" element={<SetupWizard />} />
          <Route path="/admin" element={<Administration />} />
        </Routes>
      </main>
    </div>
  );
}

export default App;
