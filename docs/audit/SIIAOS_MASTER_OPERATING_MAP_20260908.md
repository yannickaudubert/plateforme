# SIIAOS — Carte maîtresse opérante et probatoire

Date : 2026-09-08  
Branche : `audit/git-estate-truth-20260907`  
Statut : `MASTER / EVIDENCE-BASED / ARCHITECTURE-CONVERGED / RUNTIME-PROOFS-PENDING`  
Objet : convergence des conversations, archives Codex locales, audits machines, Library, GitHub, Gmail et Google Calendar en une carte exploitable sans recréer une nouvelle architecture.

> **Décision de méthode** — La matière disponible est désormais suffisante pour fixer les grandes lignées, les responsabilités et les frontières d'autorité du SIIAOS. Ce qui reste ouvert relève surtout de la preuve d'état courant, de la couverture de salvage, de la promotion de versions et de l'intégration M2→M3. Un probe machine peut changer un statut `running/healthy/mission-ready` ou une décision de retrait de repo ; il ne peut plus, seul, redéfinir l'architecture.

---

## 0. Modèle de preuve utilisé

La carte sépare systématiquement :

- **INTENTION** : conversation, cahier des charges, proposition ;
- **ARTEFACT** : fichier, pack, repo, branche, contrat, schéma réellement produit ;
- **EXÉCUTÉ-HISTORIQUE** : test, smoke, service ou scénario attesté à une date ;
- **OBSERVÉ-ACTUEL** : état live daté d'une machine ou d'un service ;
- **AUTORITÉ** : décision explicite sur qui possède le droit de faire foi ;
- **PROJECTION** : interface, index, graphe, RAG, site, cockpit ou cloud rendant visible une autorité située ailleurs ;
- **SALVAGE** : patrimoine utile à réintégrer objet par objet ;
- **HERITAGE** : version conservée pour preuve/filiation mais qui ne pilote plus ;
- **UNKNOWN / NEEDS_EVIDENCE** : information non reconstruite plutôt qu'inventée.

Une source copiée ou une rétrospective Calendar dérivée n'est pas une confirmation indépendante. Les rétros Calendar servent de colonne vertébrale temporelle et sont recoupées avec artefacts, traces Codex, GitHub, audits machines et courriels.

---

# 1. Verdict consolidé

Le SIIAOS n'est plus un projet à inventer. Il possède déjà :

1. une constitution/invariants ;
2. un noyau de contrats d'autorité et une règle de succession ;
3. plusieurs générations de cockpits et interfaces ;
4. une architecture multi-Building ;
5. une Mission Factory et une Interface Factory conçues pour instancier des environnements dédiés ;
6. des équipes, rôles, positions responsables et protocoles de délibération ;
7. une architecture de connaissance multi-Vault, graphes, RAG et preuves ;
8. une chaîne Hyperveille/Resource Radar ;
9. des runtimes locaux et nœuds machines ;
10. un patrimoine Codex massif retraçant la construction ;
11. des verticales et missions réelles ;
12. un backlog opérant de 257 chantiers.

Le déficit actuel n'est donc **pas un manque de concepts ou d'interfaces**. Le déficit principal est la dernière couche d'industrialisation : **lier les bons contrats aux bons artefacts actuels, démontrer les golden journeys, fermer les boucles d'agents, prouver restore/rollback, normaliser les registres de teams/buildings et promouvoir les versions retenues**.

---

# 2. Finalité et invariants du SIIAOS

## 2.1 Finalité générale

Le SIIAOS augmente la capacité d'une personne, d'une équipe ou d'une organisation à :

- comprendre un système complexe ;
- rechercher et qualifier de l'information ;
- débattre et conserver le désaccord utile ;
- décider sous preuve et contraintes ;
- construire et exploiter des capacités numériques/IA ;
- produire des livrables ;
- agir de manière bornée ;
- transmettre les savoirs et le RETEX ;
- réviser ses décisions ;
- rester propriétaire de ses données, méthodes, décisions et possibilités de sortie.

Il ne vise pas un « super-chatbot ». Il sert de **couche d'organisation gouvernée** entre humains, logiciels déterministes, modèles probabilistes, documents, services, machines et communautés ouvertes.

## 2.2 Douze invariants stables

1. primauté humaine ;
2. local-first ;
3. open-first et droit de sortie ;
4. preuve avant autorité ;
5. conservation du dissensus ;
6. modularité, fédération, anti-monolithe ;
7. harness autour des modèles plutôt que dépendance à un modèle ;
8. observabilité native ;
9. réversibilité, sauvegarde et restore ;
10. versions testables ;
11. pluralité cognitive ;
12. propriété/exportabilité/migrabilité par l'utilisateur.

## 2.3 Anti-objectifs

- aucune application n'est le SIIAOS ;
- aucun modèle n'est le SIIAOS ;
- aucun RAG ou graphe n'est la vérité par lui-même ;
- aucun cockpit ne possède automatiquement l'état métier qu'il affiche ;
- aucun agent ne peut s'auto-attribuer une autorité ;
- aucun cloud ou repo distant n'est automatiquement le runtime canonique ;
- aucune fédération ne justifie de fusionner les données privées de ses membres ;
- aucune version plus récente ne gagne seulement parce qu'elle est plus récente.

---

# 3. Topologie d'autorité

```text
HUMAIN / YANNICK
  finalité · arbitrage · STOP · promotion · autorisations sensibles
        |
        v
ROOT PROFESSIONAL BUILDING
  Cabinet / Studio / Lab / Missions / Recherche / Produits
        |
        +------------------------+
        |                        |
        v                        v
CONTROL + POLICY              KNOWLEDGE AUTHORITIES
Core contracts               first (technique/système)
Mission / Mandate            mon_vault (pro/métier)
Identity / Tenant            autres Vaults bornés
Gate / Lease / Policy             |
        |                         v
        |                  Knowledge Fabric
        |                  projections / lineage / indexes
        v
CAPABILITY / AGENT / MODEL FABRIC
Teams · roles · skills · adapters · harnesses · models
        |
        v
RUNTIME NODES
SandY · ARAGORN · Galaxy · cloud/external anchors
        |
        v
PROJECTIONS
plateforme · Building/Godot · Client Rooms · Radar · site · livre · academy
        |
        v
EVIDENCE / RETEX
OperationRecord · events · hashes · tests · costs · decisions · recovery
```

### Décisions fermées

- **Core** : `0.7.2-C` reste le noyau d'autorité de référence ; `alpha9` est une branche de contributions à réintégrer objet par objet (`OPTION-C`, 30/08/2026).
- **Building** : l'UI/Godot est projection ; les objets métier/control font foi derrière elle.
- **Knowledge** : `first` et `mon_vault` sont des autorités différentes par périmètre ; pas de fusion brute.
- **Hyperveille** : une seule chaîne canonique ; Resource Radar est découverte/ingestion/projection, pas une seconde Hyperveille.
- **Graphes/RAG** : dérivés reconstructibles, jamais canon implicite.
- **Nodes** : SandY/ARAGORN sont des nœuds, pas le produit.

---

# 4. Les quatre âges Codex — filiation reconstruite

Les quatre archives `sessions.part1..4.rar` ont été consolidées : **265 traces**, du **7 mars au 18 juillet 2026**, **2 118 demandes**, **1 952 clôtures**, **24 136 appels shell**, **3 622 patches** et **2 131 chemins patchés distincts**. Elles correspondent aux 265 threads de `state_5.sqlite`.

La mémoire synthétique Codex (`memories_1.sqlite`) n'a conservé que 24 sorties, dont 13 réutilisées : elle est donc un cache de travail, **pas la mémoire canonique du SIIAOS**.

## Âge 1 — mars : explosion créative

- `plateforme` : cockpit DSI transverse / intégrateur ;
- `YanIA` : workbench IA conversationnel/documentaire/agentique ;
- `IrinA` : foundry de convergence souveraine, graph/timeline/event store ;
- `site` : vitrine, acquisition, système éditorial ;
- verticales Sandrine/herboristerie/territoire ;
- `mon_vault` : mémoire professionnelle.

## Âge 2 — avril : `first` devient siège de convergence

- doctrines, politiques et registres ;
- premiers contrats inter-Vaults ;
- cockpit consultant ;
- n8n/Docker catalogués ;
- passage de prototypes isolés vers un plan de contrôle.

## Âge 3 — mai : raccordement des organes

- cockpit consultant FastAPI/SQLite/HTML/JS ;
- fédération read-only `first`/`mon_vault` ;
- Hermes, BrowserOS, Jarvis ;
- LM Studio prioritaire, Ollama complémentaire ;
- n8n, Docker, Paperless, Syncthing, Grist, Skyvern ;
- Obsidian-Hermes Cockpit.

## Âge 4 — juin-juillet : institution opératoire

- audit-first ;
- mandats et permissions ;
- équipes de sous-agents ;
- Building / Immeuble agentique ;
- Mission Factory ;
- KOS et stacks ;
- Hyperveille ;
- Office Factory ;
- capacités et registres ;
- passage de « cockpit » à « institution numérique opératoire ».

---

# 5. Lignées de versions à finaliser

## 5.1 Core / Immeuble / Building

```text
Citadelle / cellule opérable
  -> cockpit local minimal
  -> Building local-game v0.2 / v0.3 / v1
  -> ARAGORN V1 / V1.3 / V2.2 / trajectoire V3
  -> Immeuble opérant v0.2.0 / v0.2.1
  -> v0.3 / v0.4 / v0.5 / v0.6 / v0.6.1
  -> v0.7.0 / v0.7.1 / v0.7.1.2
  -> 0.7.2-C authority kernel
  -> 0.8.0-alpha9 contributions
  -> v0.8 browser projection alpha0/alpha1
```

**Décision** : cette suite est une lignée, pas 15 produits. `0.7.2-C + contributions admises` reste la base d'autorité ; les projections 0.8 doivent se brancher sur les contrats sans les remplacer.

## 5.2 Cockpit / Operator Experience

```text
Demo Cockpit Sandbox
 -> plateforme DSI
 -> cockpit territorial / maires
 -> IrinA cockpit-foundry
 -> cockpit consultant first
 -> Obsidian Hermes Cockpit
 -> Odysseus console
 -> os-cockpit-autogrow v4/v5/v6
 -> siiaos_v7_cockpit
 -> siiaos_v8_activity_cockpit
 -> siiaos-agentic-cockpit alpha/v2
 -> si-local-admin / systeme_operant_mvp / SIIAOS-v1 UI
 -> Building/Hall/Client Rooms
 -> plateforme Admin Fabric
```

**Destination** : une famille de projections réutilisant les mêmes objets Mission/Capability/Policy/Evidence, pas des backends concurrents.

## 5.3 Knowledge

```text
Obsidian personnel
 -> mon_vault + first
 -> dual/multi-Vault doctrine
 -> Vault Savoir Exchange / Capsule Ledger
 -> knowledge-index-local
 -> Obsidian-Hermes memory layers
 -> Knowledge Fabric PILOT
 -> Context Graph / Graphify projections
```

**Destination** : autorités documentaires séparées + federation read-only/controlled projection + indexes reconstructibles.

## 5.4 Radar / Hyperveille

```text
Capabilities Radar territorial
 -> Open Source Radar _siaos
 -> Hyperveille staging existante
 -> Resource Radar V2/V3
 -> V4 local-master / bridge
 -> V5 graph/lineage / RC4 resolution suggestions
```

**Destination** : Radar = découvrir/qualifier/suggérer ; Hyperveille = staging/revue ; Registry/Knowledge = promotion après gate humain.

## 5.5 Agent / Harness / ModelOps

```text
agents-personas
 -> skills/capabilities governed
 -> Hermes visible local
 -> Codex handoffs
 -> Mission Factory
 -> KOS / teams
 -> Codex-Hermes ModelOps
 -> Agent Model Runtime
 -> Model Gateway / Harness target
 -> Bridge Beta lease+gate model
```

**Destination** : providers interchangeables derrière contrats SIIAOS ; modèle/harness n'obtient jamais l'autorité.

## 5.6 Data / Office / Interface Factory

```text
production documentaire manuelle assistée
 -> Office Factory dry-runs
 -> PostgreSQL/Grist/NocoDB structured data
 -> multi-format factory
 -> Ephemeral Interface Factory
 -> generic Client Room + ViewSpec
```

**Destination** : produire données, interfaces et livrables mission-owned, traçables et destructibles/reconstructibles.

---

# 6. Registre des interfaces fabriquées ou spécifiées

Les statuts ci-dessous ne signifient pas « service encore actif aujourd'hui ». Ils indiquent la place dans la lignée.

| # | Interface / surface | Époque | Objectif | Statut convergé |
|---:|---|---|---|---|
| 1 | Demo Cockpit Sandbox | mars | pipeline, rôles, twin, archives, approvals | `ANCESTOR` |
| 2 | `plateforme` cockpit DSI | mars→ | cockpit transverse + adapters | `CURRENT OPERATOR PROJECTION` |
| 3 | site professionnel + backoffice local | mars→ | acquisition, preuve, publication, conversion | `CURRENT PUBLIC` |
| 4 | YanIA workbench | mars | conversation/document/agent gateway | `SALVAGE UX/GATEWAY` |
| 5 | YanIA Control Tower | mars | pilotage providers/capacités | `SALVAGE` |
| 6 | IrinA cockpit-foundry | 12 mars | graphes/timelines/gouvernance/runtime | `CORE-HERITAGE SALVAGE` |
| 7 | site Sandrine | mars→ | public/commerce/identité | `VERTICAL` |
| 8 | Easy Herboristerie | mars→ | savoir/operations locale | `VERTICAL HERITAGE` |
| 9 | cockpit maires / territorial | mars-avril | décision territoriale multi-acteurs | `BUILDING TEMPLATE/SALVAGE` |
| 10 | observatoire territorial | avril→ | signaux/open data/capacités | `PROGRAM SURFACE` |
| 11 | Smart Grid Cognitique / EarthGrid | avril-mai | carte relations/capacités/flux | `RESEARCH/PROJECTION` |
| 12 | QGIS/Cesium territorial views | avril-mai | mémoire ↔ territoire | `PROJECTION` |
| 13 | cockpit consultant `first` | avril-mai | missions/projets/état/preuves | `ANCESTOR` |
| 14 | Obsidian Hermes Cockpit | mai | agent visible + Vault + MCP | `SALVAGE / KNOWLEDGE UI` |
| 15 | Odysseus local/mobile console | juin | contrôle local sécurisé | `PROVIDER/ANCESTOR` |
| 16 | `os-cockpit-autogrow` v4 | juin | auto-inventaire/cockpit | `ANCESTOR VERSION` |
| 17 | `os-cockpit-autogrow` v5 | juin | idem enrichi | `ANCESTOR VERSION` |
| 18 | `os-cockpit-autogrow` v6 | juin | idem enrichi | `ANCESTOR VERSION` |
| 19 | `siiaos_v7_cockpit` | juin | vue SIIAOS machine/activity | `ANCESTOR VERSION` |
| 20 | `siiaos_v8_activity_cockpit` | juin | activité/capacités | `ANCESTOR VERSION` |
| 21 | `siiaos-agentic-cockpit` alpha | juin | mission/handoff/agents | `ANCESTOR` |
| 22 | `siiaos-agentic-cockpit` v2 | juin | contexte/registries/handoffs | `ANCESTOR/SALVAGE` |
| 23 | Building local-game v0.2 | juin | rendre SI visible/jouable | `ANCESTOR` |
| 24 | Building local-game v0.3 | juin | idem enrichi | `ANCESTOR` |
| 25 | Building local-game v1 | juin | idem + contracts | `ANCESTOR/SALVAGE` |
| 26 | ARAGORN V1 cockpit `127.0.0.1:8790` | juin | scan/health/governance read-only | `HISTORICAL EXECUTABLE` |
| 27 | ARAGORN V1.3 audit rooms | juin | maturity/teams/capabilities | `SALVAGE` |
| 28 | `systeme_operant_mvp` | juin-juil | backend Python/Go + web + Grist | `SALVAGE` |
| 29 | `si-local-admin` | juin-juil | service allowlist, scans, gates | `SALVAGE DIRECT ANCESTOR` |
| 30 | SIIAOS-v1 generated local UI | juin | control/governance harness | `SALVAGE` |
| 31 | Hypergrille / cockpit système opérant | juil | grille relations/actions/états | `RESEARCH/SALVAGE` |
| 32 | Godot Building | juin-août | serious game / simulation / rooms | `PROJECTION` |
| 33 | Hall / Client Rooms v0.7.x | août | views by audience/tenant | `PROJECTION LINEAGE` |
| 34 | v0.8 browser projection | août-sept | Operator/Consultant/Ambassador/Client/Public | `CURRENT TARGET PROJECTION` |
| 35 | GraphifyOperant Neurocampus | août | relations/capacités/commun scientifique | `GRAPH PROJECTION / VERTICAL` |
| 36 | Resource Radar V2/V3 | août | catalogue/recherche/resources | `ANCESTOR VERSIONS` |
| 37 | Resource Radar V4 | sept | local-master shell/UI/bridge | `SALVAGE/CURRENT LINEAGE` |
| 38 | Resource Radar V5/RC4 | sept | graph/lineage/resolution suggestions | `CURRENT RADAR LINEAGE` |
| 39 | generic Client Room | août→ | surface mission configurable | `TARGET REUSABLE UI` |
| 40 | Ephemeral Interface Factory | août→ | compiler ViewSpec + interface mission | `TARGET FACTORY` |
| 41 | Fred Mission Operations Cockpit | spec | opérations/mission | `DEMONSTRATOR TEMPLATE` |
| 42 | Sylvie Financial Scenario Room | spec | scénarios DAF/finance | `DEMONSTRATOR TEMPLATE` |
| 43 | Christophe Interactive Client Dossier | spec | dossier interactif/pédagogique | `DEMONSTRATOR TEMPLATE` |
| 44 | Yannick/SandY Architecture Studio | spec | architecture/lab | `DEMONSTRATOR TEMPLATE` |
| 45 | PASS Student OS / Enora | août | parcours étudiant/santé | `VERTICAL` |
| 46 | VOOLUME backoffice | 2026 | SI/édition/opérations | `CLIENT SYSTEM` |
| 47 | France Fleurs app métier / backoffice | 2026 | exploitation/DSI/data | `CLIENT SYSTEM` |
| 48 | CHVE twin clinique | 2026 | clinique/jumeau | `VERTICAL` |
| 49 | DAF augmentée | 2026 | finance/scénarios/contrôle | `CAPABILITY/VERTICAL` |
| 50 | `siiaos-livre` Obsidian/Git surface | août→ | corpus éditorial | `SCOPED AUTHORITY` |
| 51 | `universite-libre` | août→ | wiki/academy/commons | `SCOPED PEDAGOGICAL AUTHORITY` |
| 52 | `twinSIIAOS` Public Resource Hub | août→ | démonstrateur Radar/twin | `PUBLIC PROJECTION` |
| 53 | Graphify + Obsidian + AppFlowy tri-surface | août | relations / mémoire / collaboration | `COMPLEMENTARY SURFACES` |

**Règle de convergence UI** : `REUSE -> EXTEND -> CREATE -> REJECT`. Une nouvelle UI n'est autorisée que si le generic Client Room / ViewSpec / modules existants ne couvrent pas le besoin.

---

# 7. Portefeuille : tous les programmes et projets identifiés

## 7.1 Programmes (16)

1. Catalogue / parcours formation TUNICA
2. Commune rurale 3.0 sous SIIAOS
3. Formadist v5.1→v5.3
4. Hub data / innovation Vendée
5. Incubateur rural Castillon-la-Bataille
6. Incubateur rural Luçon / Vendée
7. Marché public citoyen
8. Neurocampus / CNRS — programme IA et connaissance
9. Observatoire / supply chain MIN Bordeaux Brienne
10. Observatoire territorial
11. PASS / SIIAOS étudiant
12. Ressourcerie numérique
13. SIIAOS
14. SIIAOS Broca / CNRS / GENCI
15. Territoires Augmentés
16. Université Libre

## 7.2 Projets (13)

1. Audit DSI / IA / DevOps France Fleurs 2026 — **mission réelle, lancée/facturée**
2. Clean2Gether
3. Clean4Green / Cleanforgreen
4. Clinique de Conques
5. Crise viticole Entre-deux-Mers
6. Fishing Friendly
7. Mission Metapolis — Association Déclic
8. Mission Metapolis — DRANE Occitanie
9. Mission VOOLUME Sep-Dec 2026 — **cadrage/rendez-vous réels**
10. PEGAS / CRISTAL
11. POC Innovet Tech + Pegasus Asso
12. Simon — Corps, Mouvement, Coach et Atelier des Mondes
13. Transmission savoir-faire André Duffau

### Autres engagements/propositions à ne pas confondre avec projets actifs

- Neurocampus/CNRS Phase 0 : **validée côté client, devis/fiche mission transmis** ;
- Artisans Décapeurs : **proposition d'accompagnement envoyée**, pas classée mission active sans acceptation ;
- AgorIA : fédération/collaboration transverse, pas client unique ;
- Sandrine / Ferme aux Fleurs : vertical personnel/métier à plusieurs sous-projets ;
- cabinet consultant Yannick : racine professionnelle du système, pas un « client » du SIIAOS.

---

# 8. Systèmes / briques nommées dans le portefeuille (60)

Cette liste représente le patrimoine fonctionnel, historique ou candidat — **pas 60 services live**.

1. AgorIA Hyperveille
2. AgorIA cartographie collective
3. France Fleurs app métier
4. ARAGORN/SIIAOS Starter Kit
5. VOOLUME back-office
6. Tunica Vault/RAG
7. Chorus/Isys
8. CHVE twin clinique
9. cockpit territorial
10. Sandrine cockpit / DB
11. Codex-Hermes ModelOps
12. DAF augmentée
13. Dolibarr Sandrine
14. Drift Guard
15. Easy Herboristerie
16. Ephemeral Interface Factory
17. EquiVet
18. EquiVet Dental
19. farmOS Sandrine
20. GraphifyOperant Neurocampus
21. Hermes SiteOps
22. Hermes Skills Packs
23. Hypergrille / cockpit système opérant
24. Hyperveille SIIAOS
25. knowledge-index-local
26. Machine Evidence
27. Machine File Ledger
28. Minimum Viable SIIAOS / Citadelle
29. territorial brand engine Sandrine
30. MÉTAC
31. os-cockpit-autogrow v5
32. PASS Enora v4
33. PASS Student OS
34. PosologAIequine
35. Neurocampus governed RAG
36. Resource Planner
37. Resource Radar
38. MBILO FCA local-first SI
39. Artisans Décapeurs target SI
40. SIG parcellaire
41. SIIAOS Archiviste
42. SIIAOS Building / BuildingState
43. SIIAOS Cartographie Maître
44. SIIAOS Control Plane
45. SIIAOS Core
46. SIIAOS Git Fabric SandY
47. SIIAOS Harness target
48. SIIAOS Human Governance
49. SIIAOS Mission Factory Foundation v3
50. SIIAOS Model Gateway
51. SIIAOS Office Factory
52. SIIAOS Stack Capacités ARAGORN
53. SIIAOS Unified System historique
54. `siiaos-bridge` SandY↔ChatGPT/Git
55. SIIAOS-KOS v0.4→v1.0.1
56. `siiaos-si-discovery`
57. SIL incubator SI
58. SwarmUI / Image Studio
59. VetBridge
60. France Fleurs n8n workflows

Le registre de **257 chantiers** reste le niveau fin d'exécution. Il ne doit pas être aplati dans ce document : il garde priorité, statut, maturité, responsable humain, team deck, paramètres de raisonnement, next action et Definition of Done.

---

# 9. Ton Root Professional Building — l'immeuble maître personnel

La cible v0.8 clarifie que ton identité professionnelle ne doit pas être absorbée par le Core technique. Le Core est infrastructure ; le **Root Professional Building** est ton environnement opérant.

## 9.1 Quatorze espaces fonctionnels

1. Human Hall & Direction
2. Economics & Business Development
3. Missions & Delivery
4. Architecture & Councils
5. Research & Hyperwatch
6. Knowledge & Methods
7. Creative / Deliverable Studio
8. Editorial & Reputation
9. Products / Software / SaaS
10. Platform Engineering
11. Skills / Consultant Network
12. Ambassador Circle
13. Administration & Rights
14. Prospectives & Long Time

Le dernier espace peut volontairement ne rien produire : le SIIAOS doit savoir **ne pas agir**.

## 9.2 Building instances actuellement visibles dans la projection v0.8

| ID | Instance | Rôle |
|---|---|---|
| `BLD-CORE` | Immeuble opérant Yannick · Core · SandY | lab/core node projection |
| `BLD-OPS` | Hall opérateur Yannick | operator projection |
| `BLD-CNS` | Cabinet DSI / conseil Yannick | consultant building |
| `BLD-CLI` | Client vierge | isolated Client Room template |
| `BLD-SAN` | La Ferme aux Fleurs / Sandrine | vertical |
| `BLD-IVT` | Innovet Tech | research/domain vertical |
| `BLD-AGO` | AgorIA | federated building |
| `BLD-PED` | Ingénierie pédagogique | commons/domain pack |

### Contradiction de version à conserver

`ARCHITECTURE_V0.8 alpha1` parle de **11 buildings**, tandis que la projection actuellement documentée expose **8 IDs**. Ce n'est pas résolu par recency. Le registre final doit distinguer :

- `DEFINED`
- `INSTANTIATED`
- `PROJECTED`
- `RUNTIME_VERIFIED`
- `ARCHIVED`

## 9.3 Templates de buildings récupérés

- Finance / DAF
- Patrimoine
- Commerce
- Rural
- Territoire
- Vétérinaire
- Pédagogie
- client generic

**Règle** : un Building est `Core commun + Domain/Compliance/Method Packs + tenant + maturity + activated capabilities + node placement + data classification + surface policies + evidence`. Il ne fork pas le Core.

---

# 10. Stack Admin / Factory pour déployer d'autres SIIAOS

C'est une lignée déjà conçue : **Mission Factory + Control Plane + Ephemeral Interface Factory + BuildingDefinition/Instance + Client Room**.

## 10.1 Cycle cible

```text
Need / Mission request
 -> MissionSpec
 -> classify risk / tenant / data / maturity
 -> resolve capabilities
 -> select BuildingDefinition + Domain/Compliance Packs
 -> compose team
 -> Mandate + AccessPolicy + budgets
 -> provision runtime
 -> compile ViewSpec / Client Room
 -> load authorised KnowledgePack
 -> run bounded mission
 -> OperationRecords + Evidence
 -> human gates
 -> deliverable / decision
 -> RETEX / candidate knowledge
 -> close
 -> destroy ephemeral runtime
 -> verify destruction
```

## 10.2 Contrats centraux

- `MissionSpec`
- `Mandate`
- `AccessPolicy`
- `BuildingDefinition`
- `BuildingInstance`
- `TeamDefinition`
- `HumanOperatingPosture`
- `CapabilitySpec`
- `ViewSpec`
- `EvidenceManifest`
- `RetentionPolicy`
- `OperationRecord`
- `HumanGate`
- `Lease`
- `KnowledgePack`
- `RETEX`

## 10.3 Stack de référence par maturité

| Plan | Brique cible |
|---|---|
| Control Plane | SIIAOS Mission Factory / Go API |
| Automation | Windmill ou Kestra ; Temporal plus tard si justifié |
| Identity | Keycloak |
| Relationship auth | OpenFGA |
| Context policy | OPA |
| Secrets | OpenBao |
| Runtime | Docker/Podman ; K3s seulement si besoin mesuré |
| Workflow runtime avancé | Argo Workflows après justification |
| Routing | Traefik |
| Structured data | PostgreSQL |
| Vector | pgvector par défaut ; Qdrant si besoin mesuré |
| Graph | projection/engine remplaçable ; Apache AGE candidat si besoin mesuré |
| RAG | adapter interne ; RAGFlow/AnythingLLM comme providers éventuels |
| Observability | OpenTelemetry + backend simple, puis HA/SIEM si besoin |
| UI | generic Client Room + modules + ViewSpec |
| Documents | Office Factory + exports signés + archive gouvernée |

## 10.4 Gates déjà spécifiés

- G1 automation
- G2 identity/policy
- G3 destruction vérifiée
- G4 federation
- et, côté Core, gates de succession/durabilité/tenancy/restore avant exécution élargie.

Cette Factory doit pouvoir déployer un SIIAOS **local SandY**, **partagé AgorIA** ou **hybride**, sans transférer l'autorité des données à l'infrastructure commune.

---

# 11. Teams : patrimoine actuel

Le backlog 257 contient **14 Team Decks** distincts :

| Team Deck | Finalité dominante |
|---|---|
| `TD-ARCH-001` | architecture / arbitrage systèmes |
| `TD-DEVOPS-001` | build, tests, staging, release, rollback |
| `TD-SEC-001` | sécurité, risque résiduel, obligations |
| `TD-DATAAI-001` | data fitness, model fitness, evaluation |
| `TD-KNOWLEDGE-001` | knowledge, provenance, retrieval, access |
| `TD-RESEARCH-001` | sources, reproduction, contradiction, qualification |
| `TD-PRODUCT-001` | problème utilisateur, valeur, opérabilité, adoption |
| `TD-CONTENT-001` | contenu, audience, preuve, publication |
| `TD-CHANGE-001` | adoption, résistances, formation, terrain |
| `TD-TERRITORY-001` | spatial, territoire, impact local, commons |
| `TD-OSS-001` | licence, maintenance, interop, benchmark OSS |
| `TD-FINOPS-001` | TCO, capacité, réversibilité, scénarios |
| `TD-TRANSVERSE-001` | vues indépendantes, conflits, synthèse responsable |
| `TD-VENDOR-001` | marché, lock-in, sécurité/légal, choix réversible |

### Contradiction de version

`ARCHITECTURE_V0.8 alpha1` décrit **13 équipes permanentes** ; le registre plus récent contient **14 templates de Team Decks**. La carte ne les fusionne pas artificiellement : un Team Deck est un **patron de composition**, pas nécessairement une équipe runtime permanente. Le registre Team doit formaliser la relation `TeamDefinition -> TeamDeck -> Runtime Team Instance`.

## 11.1 Positions responsables retrouvées

- `POS-ARCH-001`
- `POS-PROD-001`
- `POS-RESEARCH-001`
- `POS-KM-001`
- `POS-PLAT-001`
- `POS-CHANGE-001`
- `POS-COMMONS-001`
- `POS-DSI-001`
- `POS-OSS-001`
- `POS-SEC-001`
- `POS-AI-001`
- `POS-PROC-001`

Chaque mission doit avoir un accountable humain ou une escalade humaine explicite.

---

# 12. Rôles IA et société minimale de mission

Les travaux convergent vers des fonctions, pas des personnages permanents :

- Concierge / Situation Router
- Architecte
- Explorer / Researcher
- Analyste
- Contradicteur / adversarial reviewer
- Archiviste / documentaliste
- Opérateur
- Sécurité / immunité
- Qualité / audit
- Économiste / FinOps
- Producteur de livrable
- Médiateur humain
- spécialistes domaine à la demande

Une mission compose normalement **2 à 4 participants/capacités cognitives**. Dépasser 5 doit être justifié. On évite une armée d'agents toujours actifs.

## 12.1 Autonomie

- `A0` — lecture seule
- `A1` — proposition
- `A2` — sandbox réversible
- `A3` — écriture locale contrôlée
- `A4` — action sensible sous approbation
- `A5` — autonomie répétitive très bornée et explicitement préapprouvée

Aucune capacité ne démarre en A5.

---

# 13. Mission, temps de réflexion et débats multi-IA

La demande de pouvoir paramétrer les niveaux et le temps de réflexion **existe déjà dans les contrats/backlogs**, même si elle doit être normalisée dans une API commune.

## 13.1 Paramètres déjà retrouvés

- `goal_max_turns`
- `retries`
- `max_worker_subagents`
- `context_target` / budget de contexte
- `model_switch_policy`
- producer / reviewer / guardian
- `no_self_review`
- dependency gates
- decision protocol
- risk level
- autonomy level
- time budget
- money/cost budget
- token budget
- tool-call budget
- approved/denied tools
- allowed sources
- expected outputs
- success criteria
- rollback plan

Exemple architectural déjà utilisé :

```text
independent opinions
 -> disagreement matrix
 -> accountable synthesis
 -> policy gate if authority exceeded
```

## 13.2 Normalisation cible proposée

Sans inventer une nouvelle architecture, les champs existants devraient être regroupés sous un objet commun `DeliberationPolicy` :

```yaml
mode: quick | standard | deep | adversarial | council
max_turns: 10
max_duration: 20m
max_parallel_lenses: 4
max_subagents: 2
context_budget: 20000
model_policy: role-routed
require_independent_first_pass: true
require_contradictor: true
require_disagreement_matrix: true
require_distinct_reviewer: true
human_gate_on:
  - authority_boundary
  - external_write
  - publication
  - high_risk_decision
stop_conditions:
  - evidence_sufficient
  - budget_exhausted
  - unresolved_high_impact_conflict
  - human_stop
```

C'est une **normalisation à implémenter**, pas une prétention qu'un objet portant déjà exactement ce nom est canonique.

---

# 14. Human + IA in the SIIAOS loop

La boucle convergée issue des travaux existants est :

```text
Human Operating Posture
 -> Situation
 -> Qualification
 -> Problem / Need
 -> MissionSpec
 -> Risk + Autonomy + Reasoning budgets
 -> Situation/Capability Router
 -> authorised KnowledgePacks
 -> dynamic Team composition
 -> independent analyses
 -> PersonaContributions / Claims
 -> Contradictor / CounterClaims
 -> Evidence checks
 -> Disagreement matrix
 -> accountable synthesis
 -> Human Gate if boundary reached
 -> bounded execution
 -> OperationRecords / Events / Evidence
 -> distinct review
 -> Decision / Deliverable
 -> RETEX
 -> candidate Knowledge / publication
 -> human promotion
```

### Chaîne de Decision Room déjà définie

`Problem -> Hypothesis -> PersonaContribution -> Claim -> Evidence -> CounterClaim -> Disagreement -> Confidence -> NarrativeEvolution -> Decision`

Les lentilles peuvent inclure architecture, engineering, sécurité/légal, FinOps/GreenOps, data/AI, organisation/change/pédagogie, éthique/commons, scientifique et prospective.

Le rôle de la synthèse est de **préserver le désaccord utile**, pas de fabriquer un consensus artificiel.

---

# 15. Espaces de mémoire partagés : ce qui doit réellement être partagé

Le système ne doit pas donner à tous les agents une « mémoire globale » brute.

## 15.1 Répartition convergée

### Obsidian / Markdown / YAML

- notes lisibles humainement ;
- sources, décisions, méthodes, projets ;
- autorité documentaire par Vault ;
- Git/versioning ;
- propriétés et liens explicites.

### Graphify

- relations ;
- capacités ;
- acteurs / organisations ;
- cartographie ;
- visualisation et projection du graphe.

Graphify **ne devient pas la base canonique universelle**.

### AppFlowy

- opératif/collaboratif ;
- vues de travail ;
- coordination d'équipe lorsque pertinente.

### Knowledge Graph / Context Graph

- projections relationnelles ;
- lineage ;
- liens entre Mission/Team/Agents/Capabilities/Operations/Evidence ;
- reconstructible à partir de sources autorisées.

### Event Log append-only

- événements causaux ;
- actions ;
- validations ;
- failures/rollback ;
- temporalité.

### Vector/RAG

- recherche/récupération dérivée ;
- filtrer **avant** d'indexer ;
- indexes reconstructibles ;
- jamais source d'autorité.

### TeamRoom éphémère

Espace de coordination mission-owned où les IA peuvent s'échanger :

- tâches ;
- hypothèses ;
- résultats ;
- besoins d'information ;
- objections ;
- références ;
- status de travail.

Ce qui doit survivre est typé et promu :

`Task, Run, Inputs, KnowledgePack, Actions, ToolCalls, Artifacts, Claims, Evidence, Disagreement, Decision, RETEX`.

## 15.2 Graphe opératoire cible

```text
Mission
 -> Team
 -> AgentInstance
 -> AgentProfileRevision
 -> PersonaRevision
 -> SkillRevision
 -> Capability
 -> Tool
 -> Permission
 -> Operation
 -> Evidence
```

Ce graphe sert à savoir **qui a fait quoi, avec quel droit, à partir de quoi, dans quelle version, pour quelle mission et avec quelle preuve**.

---

# 16. Interop agents / outils

Les protocoles sont des adapters, pas des autorités :

- `AG-UI` : humain ↔ agent / surface ;
- `ACP` : IDE ↔ coding agent ;
- `A2A` : agent ↔ agent ;
- `MCP` : agent ↔ outils/données.

Le SIIAOS conserve ses objets : `Mission`, `WorkItem`, `Handoff`, `Policy`, `Mandate`, `Gate`, `Evidence`, `OperationRecord`.

Hermes, Codex, OpenClaw/PicoClaw, n8n, BrowserOS, modèles locaux/cloud et futurs harnesses restent des **providers remplaçables**.

---

# 17. Bridge Beta : passage du dessin à l'enforcement

Une instruction technique existante vise précisément la chaîne :

```text
request
 -> mandate
 -> routing
 -> lease
 -> execution
 -> proposed proof
 -> human review
 -> decision
 -> RETEX
 -> knowledge candidate
```

Les priorités P0 identifiées :

- auth/roles `observer/operator/validator/admin` ;
- worker identity/enrollment ;
- lease lié à worker/run/attempt ;
- state machines explicites ;
- vraie validation humaine ;
- cancellation/heartbeat ;
- audit causal ;
- interdiction d'une approbation simulée par le même agent qui agit.

C'est la pièce qui doit transformer le Human+AI loop en **contrôle techniquement imposé**, pas seulement en convention documentaire.

---

# 18. Nœuds et état machine

## 18.1 ARAGORN — patrimoine et preuve historique

L'inventaire forensique du 22/06 avait **55 354 entrées** sous l'ancien `D:\GITHUB`.

Objets physiquement attestés :

- `first`
- `mon_vault`
- `IrinA`
- `YanIA`
- `_siaos`
- `SIIAOS-v1`
- `si-local-admin`
- `knowledge-index-local`
- `hermes-agent`
- `jarvis-stack`
- `paperless-ngx-local`
- `syncthing-local`
- `skyvern`
- Direction artistique
- plateforme/site/easy herboristerie

Les deux Vaults possédaient notes, plugins et graph/workspace. Cela prouve l'existence historique et la structure, pas un runtime actuel.

## 18.2 SandY — nœud principal récent

Audit matériel du 13/08 : i7-14700KF, RTX 5080, 32 Go RAM, 2 To, Windows 11 ; audit read-only.

La lignée W35 documente ensuite :

- Knowledge Fabric PILOT ;
- Context Graph ;
- Mission Runtime ;
- Agent Model Runtime ;
- ModelOps local v0.1→0.2 ;
- Git Fabric ;
- Control Plane ;
- Machine File Ledger ;
- `siiaos-si-discovery` ;
- Resource Planner JSON-LD ;
- Machine Evidence ;
- Drift Guard ;
- Core QA.

Des captures terminal montrent aussi `/srv/siiaos`, Docker/NVIDIA, commits de bootstrap, Node/Capability Registry et state collector.

**Mais** le statut courant `running/healthy/authorised/mission-ready` doit encore être re-probé au moment du passage M3.

## 18.3 Modèle de vérité runtime

`declared -> discovered -> installed -> configured -> running -> healthy -> authorised -> mission-ready`

Un seul booléen `active=true` est interdit.

---

# 19. Hyperveille / Radar — chaîne unique

```text
external source / signal
 -> Resource Radar discovery
 -> source qualification
 -> Observation
 -> existing Hyperveille staging
 -> candidate resolution / claim
 -> evidence
 -> review
 -> human gate
 -> Registry / Knowledge / publication promotion
```

RC4 a déjà introduit des suggestions explicables `unresolved:* -> Resource candidates` sans mutation automatique.

**Règle physique** : ne pas créer une Hyperveille dans `D:\GITHUB\first\_siaos\hyperveille`. La lignée existante `_siiaos_hyperveille_staging` doit être comparée/consolidée avant promotion vers la cible `D:\SIIAOS\hyperveille`.

---

# 20. Git estate — disposition convergée

## KEEP

- `site`
- `twinSIIAOS`
- `plateforme`
- `mon_vault`
- `sandrine-loquet`
- `universite-libre`
- `siiaos-livre`

### `siiaos-livre`

`main` contient seulement README/.gitattributes ; le corpus candidat réel est sur `rewrite/v0.2-definitions`. Le manuscrit n'est pas « perdu » : il existe une **divergence de branche d'autorité éditoriale** à résoudre par review/promotion.

## SALVAGE / HERITAGE

- `IrinA` — rôle historique désormais prouvé ; protégé ; diff contrats/code vers Core actuel
- `YanIA` — gateway/workbench/control tower/evidence/provider patterns
- `AIfit` — lignée llmfit/model-fit ; vérifier patches uniques
- KOS / SIIAOS-v1 / anciens cockpits locaux

## EXTERNAL ANCHOR candidate

- `Handy`
- `n8n`
- `AppFlowy`
- `Perplexica`
- `n8n-workflows`
- `agentdojo`
- `odysseus`
- `searxng`

Conserver un fork personnel seulement si patchset, build, automation ou remote local en dépend réellement.

## REMOVE REPO candidate

- `myplace`
- `localsite`
- `appflowy-fullrest`
- `cockpit_d-velopement_territoriaux`

Pour le dernier, préserver la sémantique territoriale utile dans un `BuildingDefinition/Profile` avant retrait éventuel.

Aucun retrait sans dépendance search, local probe, backup/rollback et gate humain.

---

# 21. Réalité des projets — recoupement Gmail / Calendar

Le croisement des courriels envoyés et des traces projet permet de ne plus confondre statut commercial et patrimoine technique :

| Sujet | Statut probatoire |
|---|---|
| Neurocampus/CNRS Phase 0 | `CLIENT_VALIDATED / DEVIS+MISSION_SENT` |
| France Fleurs | `MISSION_STARTED / FIRST_DAY_DELIVERED+BILLED` |
| VOOLUME | `REAL CLIENT ENGAGEMENT / JULY AUDIT + AUGUST REFRAME` |
| Artisans Décapeurs | `PROPOSAL_SENT / ACCEPTANCE_NOT_PROVED HERE` |
| AgorIA | `FEDERATION/COLLECTIVE / SHARED CAPABILITIES` |
| Sandrine | `PERSONAL/DOMAIN VERTICAL` |

Calendar fournit en plus une séquence hebdomadaire W09→W35 cohérente, mais ces RÉTRO étant reconstruites, elles sont utilisées comme **index temporel** et non comme seconde preuve indépendante.

---

# 22. Contradictions et évolutions à conserver visibles

| ID | Tension | Résolution / état |
|---|---|---|
| C-01 | alpha9 plus récente vs 0.7.2-C authority contracts | `RESOLVED`: OPTION-C, contributions objet par objet |
| C-02 | `first` présenté parfois comme canon universel | `REQUALIFIED`: autorité technique/knowledge scoped, pas tout le Core/runtime |
| C-03 | `mon_vault` GitHub vs vault local | `RESOLVED BOUNDARY`: Git = projection/handoff, local vault = corpus pro scoped |
| C-04 | IrinA remote vide vs système réel | `RESOLVED ROLE`: archive Codex prouve foundry/runtime historique ; binding actuel ouvert |
| C-05 | 13 équipes alpha1 vs 14 Team Decks backlog | `OPEN MAPPING`: team permanente != template deck à confirmer |
| C-06 | 11 buildings alpha1 vs 8 IDs projection | `OPEN MAPPING`: defined/instantiated/projected à normaliser |
| C-07 | Resource Radar vs Hyperveille | `RESOLVED`: Radar ingestion/projection ; chaîne Hyperveille unique |
| C-08 | Graphify/graph store comme possible backbone | `RESOLVED`: projection relationnelle ; engine remplaçable/ADR |
| C-09 | plusieurs cockpits historiques | `RESOLVED DIRECTION`: une famille de projections sur contrats communs |
| C-10 | agents nombreux vs autonomie réelle | `OPEN OPERATIONAL`: 47 spawns historiques, boucle de clôture/intégration à normaliser |

---

# 23. Dette d'agents et de clôture

Les bases Codex contiennent **47 relations de création de sous-agents** : seulement 6 étaient explicitement fermées dans la trace consolidée ; 41 restaient marquées ouvertes. Cela ne signifie pas 41 processus actifs : cela signifie que **l'intégration/abandon/review/archivage n'a pas toujours été enregistré**.

La Mission Factory doit donc imposer :

`spawn -> mandate -> work -> result -> independent review -> integrate/reject -> evidence -> close`.

Une équipe n'est jamais « terminée » parce qu'elle a simplement produit un fichier.

---

# 24. Niveau de maturité : où nous sommes réellement

Échelle :

- `M0` ponctuel
- `M1` templatable
- `M2` automatisé
- `M3` gouverné
- `M4` fédéré
- `M5` composable

La cible immédiate reste **M2 → M3** du Root Professional Building.

De nombreuses briques sont :

- spécifiées : M1/M2 ;
- construites ponctuellement : M2 ;
- parfois testées historiquement : M2 ;
- mais pas encore toutes reliées à identity/tenant/gates/restore/evidence de façon à revendiquer M3 sur la chaîne entière.

---

# 25. Golden Journey qui doit fermer le chantier d'intégration

Premier scénario de référence : **mission consultant complète**.

```text
1. Demande / document entrant
2. Qualification et classification
3. MissionSpec dans le Control Plane
4. KnowledgePack autorisé depuis first/mon_vault/sources externes
5. DeliberationPolicy choisie (quick/standard/deep/adversarial/council)
6. Composition dynamique de 2–4 rôles/IA
7. Analyses indépendantes
8. Contradiction / disagreement matrix
9. Synthèse accountable
10. Human Gate
11. Actions déterministes / outils bornés
12. OperationRecords + preuves
13. Reviewer distinct
14. Livrable Office Factory
15. Décision de publication éventuelle
16. RETEX
17. Candidate Knowledge
18. fermeture mission / ressources éphémères
19. restore/rollback démontrable
```

Ce golden journey doit être décliné au minimum sur :

- audit ;
- veille/recherche ;
- production de livrable ;
- puis une verticale client.

---

# 26. Gates restant avant « complètement opérant »

1. **Core binding actuel** : identifier repo/path/commit/manifests qui matérialisent les contrats retenus après OPTION-C.
2. **Fresh SandY probe** : runtime/health/authorisation/mission-ready, sans confondre snapshot août et état septembre.
3. **first snapshot/successor map** : objet par objet, ce qui reste autorité et ce qui a un successeur.
4. **IrinA salvage diff** : graph/timeline/event/contracts/runtime contre Core actuel.
5. **Team registry normalization** : 13 permanent teams vs 14 team decks + positions + runtime instances.
6. **Building registry normalization** : 11 conceptual vs 8 projected + templates/instances.
7. **Bridge Beta enforcement** : auth, worker identity, lease, state machines, vraie HumanGate, cancellation.
8. **Mission durability** : DB migrations, backup/restore, retry/idempotency, evidence continuity.
9. **Knowledge boundary tests** : cross-tenant negative tests, filter-before-index, citations/provenance.
10. **Agent closure discipline** : intégrer/fermer la dette des spawns historiques et automatiser le lifecycle.
11. **Interface Factory proof** : create→ready→use→close→destroy→verify sur au moins deux clients/tenants isolés.
12. **External-anchor audit** : patches locaux et dépendances avant retrait des forks.
13. **Book promotion** : décider branche canonique de `siiaos-livre`.
14. **Restore Day** : reconstruction d'un Building depuis manifests/registries/evidence.
15. **Golden journeys** : audit, veille, livrable, client vertical.

---

# 27. Décision BOOT-001 mise à jour

BOOT-001 ne doit plus chercher « quel repo est le SIIAOS ? ».

Il doit vérifier :

- les bindings physiques des autorités déjà définies ;
- les versions uniques à salvager ;
- les dépendances ;
- les états live ;
- la possibilité de retirer sans perte ;
- la capacité de restaurer.

La sonde SandY ne choisit donc **pas** l'architecture. Elle fournit la preuve nécessaire à l'urbanisation et au nettoyage.

---

# 28. Carte cible synthétique

```text
                         YANNICK / HUMAN AUTHORITY
                                   |
                     ROOT PROFESSIONAL BUILDING
                                   |
          +------------------------+------------------------+
          |                        |                        |
   CONTROL/POLICY              KNOWLEDGE              BUSINESS/MISSIONS
   0.7.2-C+ contracts          first + mon_vault      clients/projects
   Mission/Gate/Lease          scoped Vaults          economics/delivery
          |                        |                        |
          +-------------+----------+------------------------+
                        |
                 SITUATION ROUTER
                        |
               DYNAMIC TEAM FACTORY
       humans + roles + models + skills + tools
                        |
                DELIBERATION POLICY
     turns · time · context · lenses · contradiction
                        |
                   HUMAN GATE
                        |
                 EXECUTION ADAPTERS
      Hermes/Codex/n8n/Browser/MCP/A2A/providers
                        |
             SANDY / ARAGORN / OTHER NODES
                        |
                OPERATION + EVIDENCE
                        |
              DECISION / DELIVERABLE / RETEX
                        |
       KNOWLEDGE / PUBLICATION PROMOTION IF APPROVED

PROJECTIONS:
plateforme · Building/Godot · Client Rooms · Graphify · Radar · site · livre · academy
```

---

# 29. Sources structurantes mobilisées

## Sources primaires / proches de l'exécution

- quatre volumes d'archives Codex + `state_5.sqlite` / `memories_1.sqlite` ;
- analyses Codex parties 1–4 et analyse globale du 20/07 ;
- audits machine ARAGORN juin + recovery manifest août ;
- SandY Deep Audit V2 + captures/bootstrap `/srv/siiaos` ;
- GitHub live et PRs au 08/09 ;
- branches courantes `plateforme`, `mon_vault`, `siiaos-livre`, `site`, `twinSIIAOS` ;
- courriels envoyés/mission/client ;
- artefacts versionnés Library.

## Sources normatives / décisionnelles

- cahier des charges maître ;
- Delta Spec 0.7.2-C ;
- G0 Heritage Admission / OPTION-C ;
- `ARCHITECTURE_V0.8.md` ;
- Knowledge Fabric PILOT ;
- Mission Factory Foundation ;
- Ephemeral Interface Factory ;
- Bridge Beta instructions ;
- registre 257 chantiers + Team Decks.

## Index temporel dérivé

- RÉTRO Google Calendar W09→W35 + reprise début septembre, utilisées comme index de continuité, non comme confirmation indépendante.

---

# 30. Conclusion

La « carte incontestable » n'est pas un dessin affirmant que tout tourne. C'est une carte où **chaque chose sait ce qu'elle est, ce qu'elle n'est pas, d'où elle vient, qui fait foi, dans quelle version, sur quelle preuve et ce qu'il reste à démontrer**.

À ce stade :

- les grandes frontières d'autorité peuvent être gelées ;
- les prototypes peuvent être reclassés en lignées et versions ;
- l'ensemble des programmes/projets/systèmes/interfaces connus est réintégré ;
- la stack Admin/Factory est explicite ;
- ton Root Professional Building, ses buildings, teams, rôles et missions sont raccordés ;
- le mécanisme de réflexion/débat multi-IA existe déjà dans le backlog et peut être normalisé ;
- Obsidian, Graphify, AppFlowy, graphes, RAG et event logs ont chacun une place sans devenir une mémoire universelle ;
- le Human+AI loop a un modèle contractuel cohérent ;
- l'effort restant est désormais un **programme de vérification/intégration/industrialisation**, pas une nouvelle phase d'imagination architecturale.
