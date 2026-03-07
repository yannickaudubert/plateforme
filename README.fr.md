# Cockpit OS DSI Transverse

Cockpit OS DSI Transverse est une surcouche operateur locale au-dessus de Windows.  
Il unifie la supervision et les actions operationnelles sur:

- Obsidian (documentation canonique)
- NocoDB (donnees structurees transverses)
- n8n (orchestration de workflows)
- Perplexica (recherche et exploration)
- Open WebUI (interface IA operateur)

Versions de langue:

- English: `README.md`
- Francais: `README.fr.md`

## Etat actuel (fondation v0.1)

Ce depot est maintenant une fondation operateur executable et testable:

- architecture modulaire claire (`frontend`, `backend`, `config`, `docs`, `scripts`)
- sept pages operateur en React + TypeScript
- backend FastAPI avec adapters explicites par outil
- journalisation des actions et endpoints de sante
- flux Obsidian read/write securises
- flux NocoDB en lecture (bases, tables, lignes) avec garde-fous d'authentification
- assistant de configuration bilingue FR/EN en formulaires par etapes

## Structure du depot

- `frontend/` UI operateur (React + TypeScript, Vite)
- `backend/` API, adapters, services, regles de securite, logs
- `config/` configuration runtime non-secrete (`app.json`)
- `docs/` architecture et conventions
- `scripts/` scripts utilitaires local dev
- `logs/` sortie locale du journal d'actions (gitignore)

## Modele de configuration

Priorite des valeurs runtime:

1. variables d'environnement dans `.env`
2. valeurs de `config/app.json`
3. valeurs par defaut backend (modeles pydantic)

Variables cles dans `.env`:

- `OBSIDIAN_VAULT_PATH` racine du vault canonique (defaut `D:/Yannick`)
- `OBSIDIAN_ALLOWED_ROOTS` racines autorisees pour les actions Obsidian
- `NOCODB_BASE_URL`, `N8N_BASE_URL`, `PERPLEXICA_BASE_URL`, `OPENWEBUI_BASE_URL`
- `NOCODB_API_TOKEN` requis pour les endpoints de lecture NocoDB

Initialisation:

```powershell
Copy-Item .env.example .env
```

## Developpement local

Prerequis:

- Node.js 20+
- Python 3.11+
- Docker Desktop (optionnel)

Lancer le frontend:

```powershell
Set-Location frontend
npm install
npm run dev
```

Lancer le backend:

```powershell
Set-Location backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Points d'acces:

- Frontend: http://localhost:5173
- Docs backend: http://localhost:8000/docs
- Sante backend: http://localhost:8000/health

## Assistant de configuration (nouveau)

L'assistant est disponible dans l'UI sur `/setup`.

Parcours operateur:

1. Choisir la langue (`Francais` ou `English`)
2. Renseigner runtime et chemins Obsidian
3. Renseigner les endpoints outils
4. Renseigner les secrets (optionnel)
5. Verifier et appliquer

Lors de l'application:

- `config/app.json` est mis a jour
- `.env` est mis a jour
- les caches runtime backend sont rafraichis immediatement

Si vous utilisez la stack complete docker compose, relancer `.\scripts\up.ps1` apres un changement majeur d'endpoints ou de secrets pour realigner tous les services.

## Docker compose (local dev)

```powershell
docker compose up --build
```

Compose inclut:

- frontend: http://localhost:5173
- backend: http://localhost:8000

Les services externes (NocoDB, n8n, Perplexica, Open WebUI) sont attendus a part, sur leurs URLs configurees.

## Scripts de deploiement full stack

Utiliser les scripts operateur pour une stack locale complete (backend, frontend, NocoDB, n8n, Open WebUI, Perplexica optionnelle):

```powershell
.\scripts\bootstrap.ps1
.\scripts\up.ps1
.\scripts\status.ps1
.\scripts\down.ps1
```

Pour inclure Perplexica:

```powershell
.\scripts\up.ps1 -WithPerplexica
.\scripts\status.ps1 -WithPerplexica
```

La definition compose complete est dans `docker-compose.full.yml`.

## Capacites operateur implementees

Home:

- vue consolidee de la sante des outils
- affichage du journal d'actions recentes

Obsidian Workspace:

- liste des notes (exclusion `.obsidian`)
- lecture du contenu de note et frontmatter
- creation de note avec garde-fous sur les chemins
- mise a jour de note avec verrou optimiste (`expected_modified_at`)
- ecritures atomiques et backups automatiques dans `.cockpit-backups/`

NocoDB Control:

- liste des bases
- liste des tables d'une base
- lecture des lignes d'une table
- gestion explicite des erreurs d'auth, ressources absentes et erreurs upstream

Assistant de configuration:

- formulaires guides par etapes
- choix de langue Francais/English
- saisie runtime, chemins, endpoints outils et secrets
- ecriture de `config/app.json` et `.env` via API backend
- prise en compte immediate par rafraichissement des caches runtime

## Surface API (actuelle)

Systeme et administration:

- `GET /health`
- `GET /api/v1/system/status`
- `GET /api/v1/admin/overview`
- `GET /api/v1/admin/diagnostics`
- `GET /api/v1/setup/state`
- `PUT /api/v1/setup/apply`

Obsidian:

- `GET /api/v1/obsidian/notes`
- `GET /api/v1/obsidian/note?path=...`
- `POST /api/v1/obsidian/note`
- `PUT /api/v1/obsidian/note`

NocoDB:

- `GET /api/v1/nocodb/bases`
- `GET /api/v1/nocodb/bases/{base_id}/tables`
- `GET /api/v1/nocodb/tables/{table_id}/rows?base_id=...&limit=...&offset=...`

## Notes securite et surete

- `.obsidian` est bloque pour les operations metier.
- les chemins hors racine autorisee et les traversals relatifs sont rejetes.
- les secrets ne sont jamais renvoyes par l'API, seulement des flags booleens dans l'overview admin.
- le journal masque les cles contenant `secret`, `token` ou `key`.
- les APIs NocoDB repondent `401` si `NOCODB_API_TOKEN` est absent/invalide.

## Validation et tests

Backend:

```powershell
Set-Location backend
.\.venv\Scripts\Activate.ps1
pytest -q
python -m compileall app
```

Frontend:

```powershell
Set-Location frontend
npm run build
```

## Limites actuelles

- n8n, Perplexica et Open WebUI ont un scaffolding de sante mais pas encore d'integration metier profonde.
- le scope NocoDB est lecture seule dans cette iteration.
- la persistance du journal est basee sur fichier (migration SQLite prevue ensuite).
