# Codex / SandY - mission de réconciliation locale - 2026-10-09

**Dépôt :** `yannickaudubert/plateforme`  
**Branche de référence GitHub examinée :** `main`  
**Priorité :** P0 - cartographie du patrimoine et prévention des collisions  
**Statut :** INSTRUCTIONS / NON EXÉCUTÉES - état distant inspecté le 2026-10-09.

> Ce fichier missionne Codex installé localement sur SandY. Sa présence sur GitHub ne lance pas Codex, ne prouve pas qu'un clone est présent et n'autorise aucune mutation sur SandY. Respecter d'abord les directives AGENTS.md du dépôt, les décisions humaines applicables et les permissions effectivement accordées.

## 0 bis. Relais et garde-fous Ops (ajout 2026-10-09)
Lire `IrinA/docs/SANDY_LOCAL_MODEL_DELEGATION_2026-10-09.md` et `IrinA/docs/SANDY_RELAY_AND_CONTINUITY_2026-10-09.md` (documents prives, ne pas recopier dans ce depot PUBLIC). Auditer la securite des anciens adapters, les ACL, ports Docker, secrets, journalisation, back-ups et possibilites de retrait. Reporter les faits d'execution uniquement dans le relais local prive, sans inventer de nouveau control plane ni imprimer les variables .env. Aucune migration/mutation par defaut.

## 1. Rôle confirmé ou déclaré du dépôt
Patrimoine technique Cockpit OS DSI Transverse : adapters, probes, UX opérateur et scripts historiques à qualifier pour réemploi, PAS un control-plane SIIAOS concurrent.

## 2. Sources de référence GitHub
- [AGENTS.md](AGENTS.md)
- [README.fr.md](README.fr.md)
- [SPEC.md](SPEC.md)
- [Compose historique](docker-compose.full.yml)
- [Scripts](scripts/)

## 3. Constats à date - GitHub ≠ SandY
- **Référence constatée ou documentée :** Le README décrit Obsidian, NocoDB, n8n, Perplexica et Open WebUI avec backend FastAPI/frontend React et scripts PowerShell.
- **Référence constatée ou documentée :** `docker-compose.full.yml` expose 8000 (backend), 3000 (Open WebUI), 5173, 8080, 5678 ; YanIA utilise aussi 8000/3000 : collision probable si stacks côte à côte sans remapping.
- **Référence constatée ou documentée :** Les images `:latest`/`:main`, valeurs de secrets par défaut et une authentification Open WebUI désactivée existent dans le Compose historique ; ce n'est pas une configuration à déployer telle quelle.
- **Référence constatée ou documentée :** AGENTS.md historique décrit Obsidian/NocoDB/n8n comme sources/plan principal ; ne pas confondre ces instructions patrimoniales avec une décision d'architecture plus récente.

## 4. Mission Codex - inspection locale et écarts
1. Établir la réalité des installations sur SandY : clone, branche, services Docker, volumes, bind mounts, chemins Obsidian, stockage et coûts de migration.
2. Qualifier chaque adapter, endpoint, script, test et surface UX : réutilisable, obsolète, contradictoire, non testé ; associer aux contrats du cœur SIIAOS avant admission.
3. Effectuer un diff fonctionnel entre plateforme et YanIA/IrinA ; proposer quels patterns de contrôle et de journalisation sont à SALVAGER, sans dupliquer un backend.
4. Produire une matrice des ports et identités de services 8000/3000/8080/5173/5678, secrets, accès localhost et volumes ; ne pas imprimer les valeurs des `.env`.
5. Évaluer les scripts `bootstrap.ps1`, `up.ps1`, `status.ps1` et `down.ps1` sans les lancer à l'aveugle ; définir rollback, tests et chemins de restauration.
6. Identifier l'autorité réelle du Vault local en la mesurant ; le défaut historique `D:/Yannick` n'est PAS une preuve de chemin sur SandY.

## 5. Tronc commun de reconnaissance
1. Chercher le dépôt local par URL de remote et identité Git ; ne jamais supposer que les chemins d'une autre machine valent pour SandY.
2. En cas de clone présent : relever sans modifier `git status --porcelain=v1`, branche, HEAD, remotes expurgés de tokens, worktrees, commits non poussés, différences avec références distantes, sous-modules et fichiers ignorés importants (noms seulement).
3. Si le dépôt est absent : noter `ABSENT_LOCAL`, ses conséquences et les options ; NE PAS cloner d'office et ne pas interpréter absence locale comme abandon de projet.
4. Vérifier l'existant local : services/processus, Docker/Compose/WSL, montages, volumes, ports, logs synthétisés et dépendances seulement si concernés, sans déclencher ni redémarrer de services.
5. Classer chaque objet `DÉCLARÉ / CODÉ / TESTÉ / DÉPLOYÉ / OBSERVÉ / PROUVÉ / INCONNU`, dater les preuves et préciser leur emplacement. Distinguer `DesiredState` de `ObservedState`.
6. Évaluer architecture, dépendances, risques, rollback, critères d'acceptation et preuves attendues avant toute proposition de modification opératoire.

## 6. Gel opératoire et garde-fous spécifiques
- Sur SandY, seules la documentation, l'inspection en lecture seule et les vérifications non destructives compatibles avec l'environnement sont autorisées par défaut ; aucune installation, mise à jour, migration ni reconfiguration de service avant validation de l'état et des gates.
- Aucun `git reset --hard`, `git clean -fd`, merge/rebase automatique, `docker compose up/down`, `docker system prune`, écrasement de .env/volumes/données, exposition réseau ou publication par simple lecture de cette mission.
- Ne jamais copier de secrets, valeurs .env, données clients, identité d'utilisateur final ni journaux sensibles dans GitHub ; produire un rapport privé et expurgé.
- Ne pas utiliser `scripts/up.ps1`, `docker compose up --build`, `pull`, `down -v` ou autre action de maintenance avant un inventaire des dépendances et données.
- Ne pas promouvoir les secrets de démonstration ni désactiver une authentification en production.
- Ne pas ériger ce dépôt en nouveau cœur du SIIAOS ni créer une deuxième source de vérité.
- Les fichiers AGENTS locaux restent applicables à l'héritage du dépôt, mais relever toute contradiction avec les décisions humaines du 2026-09-26 pour arbitrage.

## 7. Livrable local attendu de Codex
Créer dans un espace de rapports **local privé** (hors commit automatique) un dossier daté pour ce dépôt avec :
- `inventory.md` : chemins réels observés sur SandY, branche/HEAD, composants trouvés, services et données, sources et preuves.
- `gap-matrix.md` : `attendu / déclaré GitHub / observé SandY / contradiction / criticité / propriétaire`.
- `plan.md` : corrections ordonnées P0-P3, prérequis, tests, risques, rollback, gate humaine.
- `evidence.json` : métadonnées expurgées (date, commande de lecture/test, code retour, identifiants de version, lien vers trace locale sécurisée).
- `handoff.md` : prochain ordre opératoire, blockers, éléments à ne pas toucher et décision humaine attendue.
Ne déclarer `READY` qu'après résultats de tests et preuve de reprise ; ne jamais affirmer qu'une consigne écrite équivaut à un test. Si rien n'est exécutable, renseigner `NON_OBSERVÉ` et les causes.

## 8. Commande de reprise pour l'opérateur
Depuis Codex sur SandY : « Lis `CODEX_SANDY_2026-10-09.md` dans ce dépôt (ou sur sa branche `main` si nécessaire), effectue l'inventaire read-only et écris le rapport privé. N'installe ni ne déploie rien sans la gate définie. »
