# SIIAOS Admin — cible « ville industrielle » multi-cockpits

**Statut :** PROPOSAL  
**Objet :** transformer les lignées existantes en système de production quotidien pour Yannick, sans créer un monolithe ni dupliquer les SI métiers.

## 1. Principe

Le SIIAOS Admin est le **backoffice opérateur transversal**. Les « immeubles » et cockpits sont des projections spécialisées d'un même système de registres, de politiques, de connaissances, de tâches, d'agents et de providers.

Un `Building` n'est donc pas une application isolée. Il référence :

`profile + tenant + missions + métiers + datasets + knowledge + processes + capabilities + providers + agent teams + tools + interfaces + policies + evidence`.

L'utilisateur peut entrer par le Hall global, un cockpit métier, une salle d'équipe agentique ou l'interface native d'un outil. Toutes ces surfaces partagent les mêmes identités, règles et preuves.

## 2. Districts fonctionnels

### Hall / Command Center

Vue de situation globale : projets, alertes, décisions, missions, ressources, agents, clients, machines, changements, preuves et priorités. C'est la page opérateur quotidienne, pas un dashboard décoratif.

### Registry & Authority District

Asset Registry, Node Registry, Service Registry, Capability Registry, Provider/Adapter Registry, Model Registry, Agent/Team Registry, Skill/Tool Registry, Experience Registry, External Anchor Registry, Port/Endpoint Registry, VersionLineage, Evidence Registry et Decision/ADR Registry.

### Work / Mission / Project Factory

Portefeuille projets, tâches, dépendances, roadmaps, kanban, missions, mandats, priorités, charge, calendrier, preuves d'avancement, Definition of Done, rétrospectives et amélioration continue. Les 120 tâches canoniques et 257 OPEN historiques servent de patrimoine, jamais de doubles autorités.

### Client & Engagement District

Clients, organisations, contacts, canaux, dossiers, engagements, livrables, SI/infrastructures clientes, risques, décisions, accès, échéances et preuves. Segmentation stricte `organisation → client → project → dataset → secret`.

### Agent Organization District

Rôles, personas, AgentProfiles, instances, équipes, TeamDecks, compétences, outils, modèles, coûts, permissions et lifecycle. Les pôles virtuels peuvent être **dormants** et activés par mission après résolution des préconditions.

Chaque équipe expose : mandat, objectifs, savoirs autorisés, outils, providers, niveau d'autonomie, budget, contexte, critères d'arrêt, human gates et livrables.

### Tool / Experience District

Chaque outil peut être ouvert selon le meilleur mode : native UI, embed, reverse proxy, deep-link, API-native mini-view, MCP/action, CLI contrôlée ou workflow sans UI. Le backoffice ne remplace pas artificiellement les bonnes interfaces natives.

### AI / ModelOps District

LiteLLM/model gateway, runtimes locaux, modèles, embeddings, ASR/TTS, génération image/vidéo, context windows, coûts, VRAM/RAM, benchmark, provenance, licences, disponibilité et routing. Le Capability Router choisit provider + opérateur + nœud selon mission et politique.

### Infrastructure & Node District

SandY, ARAGORN, Galaxy, mobiles et futurs nœuds : identité, santé, ressources, services, stockage, réseaux, GPU/CPU, énergie si mesurable, software footprint, mises à jour, drift, backups et capability advertisements.

### External Compute Commons

Catalogue des ressources externes : HPC académique/public, GPU/CPU communautaire ou gratuit, stockage ouvert, cloud autorisé, notebooks distants et quantique accessible à distance. Chaque offre est un provider avec éligibilité, quotas, coût, données acceptées, juridiction, latence, queue, API, expiration et preuve d'usage.

### Knowledge / Data District

Vaults, Git, bases structurées, fichiers, index, graphes, ingestion documentaire, datasets locaux, open data, catalogues, data lineage, droits-before-index, ContextPacks et exports. Les index restent reconstruisibles à partir du canon.

### Science & Open Science District

Projets scientifiques, questions, protocoles, littérature, auteurs/labos, datasets, hypothèses, claims/counterclaims, controverses, expérimentations, reproductibilité, niveaux de preuve et publications. Connecteurs prévus vers arXiv, HAL, OpenAlex, Crossref, PubMed et autres sources selon domaine.

### OSINT / Research District

Recherche Web, SearXNG/Odysseus, sources publiques, entités, chronologies, relations, géodata, médias et dossiers d'enquête. Politique explicite de provenance, légalité, minimisation, contradiction et séparation fait/inférence.

### Radar & Admission District

Resource Radar, Radar OSS, Radar Python, Radar modèles/datasets, Radar science, Radar compute/HPC/quantum, Radar APIs/MCP et Radar interfaces. Pipeline commun :

`source → découverte → qualification → provenance → licence → sécurité → compatibilité → benchmark → décision candidate → expérience bornée → admission/rejet/archive`.

### Governance / Regulatory / Safety District

Politiques, exigences, contrôles, obligations, risques, licences, données, rétention, accès, approvals, exceptions, incidents, audit findings, Human Gates, secrets, rollback et preuves de conformité. Les règles réglementaires deviennent des objets versionnés et testables, pas seulement des documents.

### Improvement & Experimentation District

Backlog d'amélioration, drift, régressions, dette, alternative radar, A/B ou feature flags lorsque pertinent, benchmark, expérimentation isolée, promotion d'environnement, post-mortem et mesure de valeur.

### Office / Production District

Production et transformation de DOCX/ODT/PDF/XLSX/CSV/PPTX/HTML, modèles, assemblage de dossiers, édition, publication, signature/validation, extraction et archivage. Cette Factory est transverse aux clients, à la recherche et aux projets internes.

## 3. Immeubles/cockpits spécialisés

La première famille cible comprend au minimum :

- **DSI / Innovation / IA / Open Source / GitOps** : architecture, audits, SI, gouvernance, delivery, sécurité, data, IA et adoption ;
- **Cabinet de conseil / missions** : clients, rendez-vous, diagnostics, propositions, livrables, décisions, facturation à interfacer ;
- **Science / recherche** : littérature, protocoles, preuves, expériences, publications et open science ;
- **Territoires / politiques publiques / communs** : SIG, acteurs, ressources, projets, données publiques, budgets, gouvernance ;
- **OSINT** : dossiers, sources, graphes, chronologies, contradictions, preuves ;
- **Data / Open Data** : datasets, qualité, transformations, lineage, APIs, publication ;
- **Dev / DevOps / AgentOps** : repos, branches, CI/CD, releases, services, agents, tests, incidents ;
- **Infrastructure / Compute** : nœuds locaux, stockage, GPU/CPU, HPC, cloud/edge et quantum ;
- **Création multimodale / Audio** : image, vidéo, audio, transcription, traduction, diarisation, TTS et studios ;
- **Knowledge / ArchiveOps** : Vaults, Library, ingestion, archivage, déduplication, restauration et recherche.

Les cockpits métiers Sandrine/La Ferme aux Fleurs, AgorIA, territoires, Neurocampus, PASS/éducation, France Fleurs et autres projets restent des `BuildingProfiles` distincts, réutilisant les fabrics transversaux.

## 4. Objets canoniques minimaux du backoffice

`Tenant`, `Organization`, `Client`, `Project`, `Mission`, `Task`, `Mandate`, `Role`, `Persona`, `AgentProfile`, `AgentInstance`, `Team`, `Skill`, `Tool`, `Model`, `Node`, `Service`, `Capability`, `Provider`, `Adapter`, `Dataset`, `KnowledgeObject`, `Evidence`, `Decision`, `Policy`, `Requirement`, `Control`, `Risk`, `ExternalAnchor`, `Environment`, `Deployment`, `VersionLineage`, `Experience`, `ViewSpec`, `Alert`, `Incident`, `Experiment`, `ImprovementProposal`.

## 5. Base réglementaire à coder

La base de gouvernance/réglementation doit pouvoir représenter :

- texte/source d'autorité et juridiction ;
- version, dates d'entrée en vigueur et supersession ;
- périmètre d'applicabilité ;
- obligation/interdiction/permission ;
- données et traitements concernés ;
- rôle responsable ;
- contrôle technique/organisationnel ;
- test de contrôle ;
- preuve attendue et fraîcheur ;
- exception/dérogation et approbation ;
- risque associé ;
- décision et historique ;
- statut `UNKNOWN/APPLICABLE/NOT_APPLICABLE/COMPLIANT/PARTIAL/NON_COMPLIANT`.

La couche réglementaire ne doit pas confondre résumé juridique, règle machine et preuve de conformité. Toute règle machine doit référencer sa source et son interprétation validée.

## 6. Projection locale et Vercel

La source, les schémas et les politiques restent versionnés dans Git/GitHub. Les surfaces locales accèdent aux données et actions privées. Vercel sert uniquement les projections explicitement publiables : démos, portails publics, documentation, Resource Radar ou UI sans secrets.

Aucune UI Vercel ne doit recevoir directement une capacité shell libre ou des secrets locaux. Les ponts vers le local utilisent un connecteur borné, authentifié et traçable.

## 7. Réutilisation prioritaire de `plateforme`

Le dépôt `plateforme` contient déjà un cockpit opérateur React/TypeScript + FastAPI, des adapters Obsidian/NocoDB/n8n/Perplexica/Open WebUI, des safe writes, un journal SQLite, une page setup et des endpoints admin. Il doit être audité comme **salvage base** du SIIAOS Admin avant toute réécriture.

Cible : porter ses patterns derrière les contrats récents d'autorité, de tenancy, de capability routing, de version lineage et d'evidence, plutôt que reconstruire un cockpit depuis zéro.

## 8. Definition of Done de la première tranche

La première tranche n'est terminée que lorsqu'un utilisateur peut : ouvrir le Hall ; voir l'état de SandY et des services ; sélectionner un projet ; ouvrir son cockpit ; voir tâches/missions/décisions ; convoquer une équipe agentique dormante avec mandat borné ; accéder à un outil natif ; obtenir une preuve d'action ; et revenir au Hall sans dupliquer les données ni contourner les droits.
