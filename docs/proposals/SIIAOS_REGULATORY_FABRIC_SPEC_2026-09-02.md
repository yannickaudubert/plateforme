# SIIAOS Regulatory / Governance Fabric — spécification v0.1

**Date :** 2026-09-02  
**Statut :** PROPOSAL / seed metadata  
**Règle :** versionner sources, analyses, exigences, contrôles et preuves sans transformer une synthèse IA en droit ni une guidance en texte contraignant.

## 1. Trois niveaux obligatoires

### Authority Source
Texte officiel, acte, loi/règlement, processus législatif, standard ou guidance avec juridiction, émetteur, version, dates, amendements, URL officielle et fraîcheur.

### Interpretation / Applicability
Analyse contextualisée : rôle de l'organisation, secteur, finalité, type de système, données, personnes affectées, juridiction, dates. Elle porte auteur/reviewer, hypothèses, confiance, désaccords et peut produire `LEGAL_REVIEW_REQUIRED`.

### Machine Control
Policy, contrôle ou test interne traçable vers une Interpretation validée puis vers les sources. Le contrôle machine ne se présente jamais comme le texte juridique lui-même.

## 2. Objets

- `AuthoritySource` : id, titre, publisher, authority_type, jurisdiction, official URL, langue, version courante, supersession, last_checked_at.
- `AuthorityVersion` : consolidation/version, publication/effective/application dates, changements et amendements.
- `Requirement` : source/article/section, sujet, condition, exception, dates, éléments nécessaires pour établir l'applicabilité.
- `ApplicabilityRule` : prédicats sur juridiction, acteur, secteur, purpose, AI role, data class, scale, employment/product impact, contrat.
- `Interpretation` : contexte, analyse, hypothèses, reviewer, confiance, contre-interprétations, approbation éventuelle pour machine policy.
- `Policy` / `Control` / `ControlTest` : objectif, owner, mesure, méthode de test, fréquence, evidence attendue, sévérité, remediation.
- `ComplianceAssessment` : applicability, implementation, test, evidence freshness, residual risk et review status séparés.
- `Exception` : scope, raison, approbateur, durée, compensating controls, review date.
- `RegulatoryImpactCandidate` : impact possible d'un changement sur policies, controls, projets, clients, services, artifacts et Buildings. Il ne mute rien automatiquement.

## 3. États d'applicabilité

`APPLICABLE`, `NOT_APPLICABLE`, `POSSIBLY_APPLICABLE`, `UNKNOWN`, `EXTERNAL_REVIEW_REQUIRED`.

Ne jamais réduire la conformité à un score opaque unique. Les axes restent consultables et reliés aux preuves.

## 4. Hiérarchie des sources

1. éditeur juridique officiel : EUR-Lex, Legifrance, dossiers parlementaires officiels ;
2. autorité compétente : CNIL, ANSSI et équivalents ;
3. standards officiels selon droits d'accès/licence ;
4. frameworks reconnus NIST/OWASP comme méthodes/contrôles, pas comme droit contraignant sauf incorporation explicite ;
5. commentaires secondaires comme evidence de recherche uniquement.

## 5. Seed EU/France

Le seed du registre contient notamment AI Act, GDPR, Data Act, Cyber Resilience Act, état de la transposition française NIS2 et guidance CNIL IA. Il sert à tester le modèle source/version/fraîcheur. **Il ne constitue pas un avis juridique et ne conclut pas automatiquement à l'applicabilité.**

Le système doit explicitement distinguer : publication vs date d'application ; règlement vs guidance ; projet de loi vs loi promulguée ; obligation générique vs obligation conditionnelle à un rôle, produit, donnée ou finalité.

## 6. Regulatory Freshness Radar

```text
official source discovery/check
→ new version/amendment/guidance candidate
→ metadata/hash/reference
→ semantic diff candidate
→ status classifier
→ Requirement impact candidates
→ Policy/Control/Project impact candidates
→ human/legal review
→ version/supersession decision
→ update proposal
```

Règles : confirmation par source officielle avant promotion ; conservation de l'historique ; aucune mise à jour automatique d'une policy de production ; une traduction/résumé ne remplace jamais la référence exacte ; `UNKNOWN` reste valide.

## 7. Regulatory cockpit

Vues : timeline des sources/amendements ; matrice d'applicabilité client/projet/mission ; graphe Requirement→Control→Test→Evidence ; evidence manquante/stale ; dates à venir ; exceptions ; questions juridiques ouvertes ; impact candidates ; Compliance Packs par BuildingProfile.

Actions proposal-first : `review`, `request legal review`, `create control proposal`, `schedule test`, `link evidence`, `approve interpretation`.

## 8. Intégration au routage

Une Mission référence des Domain/Compliance Packs. Capability Router reçoit les contraintes **approuvées** : confidentialité, résidence, human oversight, logging, sécurité, réversibilité, etc. Le routeur n'exécute pas directement du texte juridique brut.

## 9. Versionnement

Source, version de source, requirement, interpretation, policy, control et test ont leurs versions propres. Une supersession ne supprime jamais l'evidence historique. Chaque assessment mémorise les versions exactes utilisées.

## 10. Definition of Done v0.1

- sources officielles/régulateur représentées avec type et fraîcheur ;
- aucun projet de loi présenté comme loi ;
- aucune guidance présentée comme règlement contraignant ;
- séparation source / interprétation / policy / contrôle / test / evidence ;
- un changement crée un `RegulatoryImpactCandidate` sans mutation de production ;
- une mission pilote peut expliquer pourquoi un contrôle est demandé et à quelle source/version l'analyse se rattache ;
- `UNKNOWN` et `EXTERNAL_REVIEW_REQUIRED` fonctionnent de bout en bout.
