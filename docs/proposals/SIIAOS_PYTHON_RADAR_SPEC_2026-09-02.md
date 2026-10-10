# SIIAOS Python Radar — spécification v0.1

**Statut :** PROPOSAL  
**Priorité proposée :** P0 design / P1 implementation  
**But :** transformer l'écosystème Python en registre de capacités gouverné, sans installer automatiquement les packages découverts.

## 1. Pourquoi un Radar Python distinct

Le Resource Radar sait découvrir des modèles, datasets, repos, publications et artefacts. Il ne répond pas encore à la question SIIAOS :

> « Parmi les centaines de milliers de packages Python et leurs versions, quelles fonctions deviennent réellement disponibles pour cette mission, sur ce nœud, avec quels coûts, dépendances, risques, licences, performances, interfaces et preuves ? »

Un package n'est pas une capability. Un package peut offrir plusieurs bras : bibliothèque importable, CLI, serveur, plugin, protocole, format, backend GPU, pipeline, visualisation, ingestion, automation, test ou intégration.

Le Python Radar doit donc faire :

`package → versions → distributions → dépendances → sécurité/provenance → interfaces → fonctions → capabilities → compatibilité nœud → expérience bornée → admission provider`.

## 2. Sources primaires et secondaires

### PyPI Index API / JSON API

Source primaire de packaging Python pour : projet, versions, distributions, `requires-python`, yanked status, hashes, metadata, URLs et informations de release. Les nouvelles intégrations doivent privilégier l'Index API JSON pour l'index/distributions.

### PyPI Integrity / attestations

Quand disponibles : provenance de publication, Trusted Publisher, attestations et vérification d'artefact. Cela ne remplace pas l'évaluation de sécurité du code.

### deps.dev API v3

Enrichissement : licences SPDX, dépendances résolues, versions, projets upstream, advisories et relations package↔project. deps.dev agrège notamment PyPI, OSV, OpenSSF Scorecard et OSS-Fuzz.

### OSV

Couche vulnérabilités par package/version PyPI, requêtes unitaires ou batch.

### GitHub/GitLab/upstream déclaré

Santé du projet : releases, activité, tags, CI, issues, docs, licence source, sécurité, mainteneurs et provenance. Une URL déclarée n'est pas automatiquement considérée comme fiable.

### Documentation officielle du projet

Extraction des APIs, CLI, extras, backends, exemples, limitations, compatibilités et surfaces d'intégration.

## 3. Schéma `PythonPackageCandidate`

Champs minimaux :

- `package_id`, nom normalisé, aliases ;
- version, date publication, yanked/deprecated ;
- Python min/max connus ;
- distributions wheel/sdist, plateformes/ABI/architectures ;
- hashes et attestations disponibles ;
- licence déclarée + licence normalisée + ambiguïtés ;
- source repo et documentation ;
- dépendances directes et graphe transitif ;
- extras/features ;
- vulnérabilités directes/transitives ;
- health/maintenance signals ;
- native/system dependencies ;
- CPU/GPU/CUDA/ROCm/DirectML/MPS requirements si applicables ;
- RAM/VRAM/disk/network observations ;
- data classes manipulées ;
- telemetry/egress observé ou documenté ;
- APIs/import surface ;
- CLI/entry points ;
- serveur/ports si applicable ;
- formats/protocoles ;
- tests disponibles ;
- benchmark evidence ;
- `observed_at`, `source`, `confidence`.

## 4. Schéma `PythonCapabilityArm`

Chaque bras fonctionnel contient :

- `capability_id` ;
- `provider = python:<package>@<version>` ;
- fonction métier/technique ;
- module/import ou entry point ;
- inputs/outputs ;
- préconditions ;
- optional extras ;
- dépendances natives ;
- node compatibility ;
- permissions et accès filesystem/network ;
- coût CPU/RAM/GPU/VRAM/latence ;
- qualité/benchmark ;
- risques/licence ;
- exemples reproductibles ;
- test minimal ;
- rollback/uninstall strategy ;
- niveau de maturité ;
- alternatives et combinaisons possibles.

## 5. Taxonomie initiale à couvrir

Le Radar ne doit pas être limité à « IA ». Il doit couvrir au minimum :

- scientific computing et numerical ;
- dataframes, SQL, ETL, validation, quality ;
- statistics, econometrics et causal inference ;
- ML classique, deep learning et inference ;
- NLP/LLM/RAG/embeddings ;
- vision/image/video ;
- audio/ASR/TTS/music/signal ;
- GIS/geospatial/remote sensing ;
- graphs/network science/knowledge graphs ;
- optimization, operations research et simulation ;
- quantum SDKs et remote backends ;
- web/API/servers ;
- browser automation/scraping ;
- document/PDF/Office/OCR ;
- search/IR/OSINT ;
- security/crypto/SBOM/static analysis ;
- DevOps/Git/containers/Kubernetes/cloud ;
- observability/metrics/tracing/logging ;
- workflows/queues/schedulers ;
- databases/vector/object stores ;
- testing/property testing/benchmarking ;
- visualization/dashboards/UI ;
- hardware/sensors/serial/IoT ;
- robotics/control ;
- scientific domain packages : bio, neuro, chemistry, physics, astronomy, climate, ecology, health, social sciences ;
- open science/reproducibility/publication ;
- file formats/conversion/archive/compression ;
- local OS/Windows/WSL automation.

## 6. Détection des « bras »

Le pipeline combine :

1. metadata/entry points/extras ;
2. documentation et README ;
3. symbol/API inspection en sandbox lorsque permis ;
4. exemples/tests upstream ;
5. dépendances et backends optionnels ;
6. micro-expérience bornée ;
7. qualification par agents spécialisés ;
8. validation humaine avant admission.

Agents proposés : `PythonScout`, `MetadataClassifier`, `DependencyAnalyst`, `LicenseReviewer`, `SecurityReviewer`, `APIMapper`, `CapabilityMiner`, `BenchmarkRunner`, `NodeCompatibilityAnalyst`, `Integrator`, `Archivist`.

Ces rôles sont des spécialisations de l'Agent Operator Fabric ; ils ne constituent pas un second système agentique.

## 7. Compatibilité SandY / WSL / autres nœuds

Le Radar calcule une matrice par nœud :

`Python version × OS × architecture × GPU stack × drivers × native libs × memory × storage × policy`.

Exemples de décisions possibles :

- `COMPATIBLE_WINDOWS_NATIVE` ;
- `PREFER_WSL2` ;
- `GPU_CUDA_REQUIRED` ;
- `CPU_ONLY_OK` ;
- `BUILD_FROM_SOURCE_REQUIRED` ;
- `CONFLICTS_WITH_CURRENT_ENV` ;
- `ISOLATED_ENV_REQUIRED` ;
- `NOT_COMPATIBLE` ;
- `UNKNOWN_NEEDS_PROBE`.

Aucune installation n'est déclenchée par le Radar. Il génère un `ExperimentProposal` comprenant environnement isolé, lockfile, commandes proposées, ressources, tests, preuves et rollback.

## 8. Environnements Python gouvernés

Le SIIAOS doit traiter les environnements comme actifs :

- interpreter ;
- venv/uv/conda/pixi/autre provider retenu ;
- lockfile ;
- package set ;
- hashes ;
- purpose/mission ;
- owner ;
- node ;
- storage location ;
- secrets refs ;
- last verified ;
- reproducibility status ;
- lifecycle.

Éviter un `pip install` global non tracé sur SandY. Les environnements d'expérimentation doivent être jetables et reproductibles.

## 9. Scoring et décision Radar

Pas de score unique opaque. Conserver des axes séparés :

- functional fit ;
- maturity ;
- maintenance ;
- security ;
- provenance ;
- license compatibility ;
- reversibility ;
- local-first fitness ;
- node compatibility ;
- resource efficiency ;
- interoperability ;
- testability ;
- documentation ;
- community/ecosystem ;
- replacement availability.

Décisions : `WATCH`, `RESEARCH`, `EXPERIMENT`, `ADMIT_PROVIDER`, `PREFER_EXISTING`, `REJECT`, `QUARANTINE`, `DEPRECATE`, `ARCHIVE`.

## 10. Golden journeys v0.1

### Journey A — « J'ai besoin d'une fonction »

Besoin : « extraire des tableaux d'un PDF scientifique ». Le Capability Router interroge Python Radar + providers existants, compare packages, services déjà installés et méthodes sans Python, puis propose le meilleur provider avec preuve.

### Journey B — « Que peut m'offrir ce package ? »

Entrée `polars` ou `networkx`. Le Radar ne renvoie pas seulement une fiche package : il construit les bras fonctionnels, dépendances, usages SIIAOS, alternatives, compatibilité SandY et expériences possibles.

### Journey C — « Que manque-t-il à ce cockpit métier ? »

Le cockpit scientifique exprime ses capabilities requises ; Python Radar révèle des providers possibles, sans installation, et les passe au Radar d'admission.

### Journey D — « Peut-on remplacer une brique ? »

Le système cherche providers Python + services OSS + APIs externes correspondant à une capability, puis simule remplacement, parallèle ou série.

## 11. Interfaces

Le Python Radar doit exister comme :

- vue dans le Radar District du SIIAOS Admin ;
- recherche globale depuis le Hall ;
- API locale ;
- provider pour agents ;
- export JSON/YAML ;
- éventuellement surface publique Vercel **uniquement pour les données publiques**, sans environnements locaux, secrets ou capacités d'installation.

## 12. Première tranche de code proposée

1. schémas `PythonPackageCandidate`, `PythonCapabilityArm`, `PythonEnvironment`, `ExperimentProposal` ;
2. connecteur PyPI Index/JSON avec cache/ETag ;
3. enrichisseur deps.dev ;
4. scanner OSV batch ;
5. normalisation package/version/source ;
6. stockage SQLite local + export JSON ;
7. recherche et filtres dans le backoffice ;
8. test sur 20 packages représentant plusieurs familles ;
9. aucune installation automatique ;
10. Evidence records pour toutes les décisions.

## 13. Definition of Done

V0.1 est validable si le système peut partir d'un nom de package ou d'une capability, produire une fiche sourcée et fraîche, construire au moins un bras fonctionnel vérifiable, résoudre dépendances/licence/vulnérabilités/compatibilité nœud, comparer au moins une alternative, générer une expérience isolée et enregistrer la décision sans modifier l'environnement hôte.
