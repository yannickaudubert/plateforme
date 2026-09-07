# BOOT-001 — Git Estate Truth / runbook SandY

Status: `OBSERVE_ONLY`

Authority: this runbook is an audit procedure. It does not authorize deletion, archive, remote mutation, repository creation, merge, deployment, service restart or runtime configuration.

## Goal

Build a dated, reproducible inventory of the Git estate actually present on SandY before reorganising GitHub or deciding which repositories survive.

The inventory separates:

- what exists locally;
- what Git locally declares about remotes and tracking refs;
- what GitHub currently exposes;
- what is only historical or proposed;
- what still needs a fresh runtime or dependency probe.

A GitHub repository that is empty is not evidence that the local project is empty. A local directory is not evidence that a service is running.

## Probe

Script:

`./scripts/audit-sandy-git-estate.ps1`

Default roots:

- `C:\GitHub`
- `C:\first`
- `C:\SIIAOS`

Default maximum traversal depth: `8`.

Example from PowerShell:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\scripts\audit-sandy-git-estate.ps1 -OutputDirectory C:\SIIAOS\SandY\reports\git-estate\2026-09-07
```

For additional roots:

```powershell
.\scripts\audit-sandy-git-estate.ps1 `
  -Roots @('C:\GitHub','C:\first','C:\SIIAOS','D:\GITHUB','D:\SIIAOS') `
  -OutputDirectory C:\SIIAOS\SandY\reports\git-estate\2026-09-07
```

## Read-only guarantee

The observer may execute only local Git inspection commands such as:

- `git rev-parse`
- `git branch --show-current`
- `git status --porcelain=v1 --branch`
- `git remote -v`
- `git worktree list --porcelain`
- `git log -1`
- `git rev-list --left-right --count` against an already-present local tracking ref
- `git submodule status --recursive`
- `git count-objects -vH`

It intentionally does not execute:

- `fetch`
- `pull`
- `push`
- `checkout` / `switch`
- `reset`
- `clean`
- `prune`
- branch deletion
- worktree removal
- submodule update
- LFS pulls
- package installation
- service or container commands

Consequently, `ahead` / `behind` are relative to the remote-tracking ref already present locally. They are not proof of the current remote state.

## Outputs

The script emits:

- `repo_inventory.json` — canonical observation payload for this probe;
- `repo_inventory.csv` — flat review/export surface;
- `repo_inventory.md` — human review projection.

Each record carries a timestamp, machine, path, head, branch, upstream when locally known, local ahead/behind counts, dirty state, worktrees, remotes, submodules and last commit.

The following are deliberately labelled as not probed:

- live remote reachability;
- current GitHub branch equality beyond a subsequent connected comparison;
- Vercel dependency;
- CI dependency;
- local service/runtime state;
- canonical authority;
- secrets suitability for publication.

## Phase 2 — remote/local reconciliation

After the local observation is captured, compare each local repository to connected GitHub without changing either side.

Disposition vocabulary:

- `KEEP`
- `SALVAGE`
- `EXTERNAL_ANCHOR`
- `ARCHIVE`
- `REMOVE_CANDIDATE`
- `NEEDS_EVIDENCE`

Do not use `REMOVE` until all removal gates in BOOT-001 are satisfied.

For each repository, reconcile:

1. local absolute path(s);
2. local HEAD and unique branches;
3. GitHub repository and default branch;
4. unpublished commits or worktrees;
5. Vercel / GitHub Actions / scripts / service references;
6. original purpose recovered from conversation/history where available;
7. unique semantics/assets worth preserving;
8. future architectural owner plane;
9. rollback/export strategy.

## Phase 3 — dependency probe

Before retiring a fork or empty remote, search at minimum:

- `.git/config` and worktree metadata;
- scripts and environment templates;
- Docker Compose and container definitions;
- CI/workflows;
- Vercel project repository bindings;
- documentation/runbooks invoking clone URLs;
- local launchers and scheduled tasks;
- package/submodule dependencies;
- SIIAOS Registry / Radar records.

A local software instance may remain active even if its personal GitHub fork is retired. In that case preserve its upstream reference, exact revision/version, licence, local instance/probe and any local patch set as an `ExternalAnchor` / provider record.

## Phase 4 — removal decision

A repository becomes eligible for human removal decision only if all are true:

- no unique local commit is unsaved;
- no required branch/worktree exists only there;
- no runtime/deployment/script depends on its personal GitHub URL;
- any upstream resource is registered independently;
- any historical value is retained with manifest/hash where appropriate;
- rollback is explicit;
- a human decision authorizes the removal.

## Known anomalies before the live probe

- `IrinA`: GitHub appears empty but available local archive contains a substantial project. Protect until live reconciliation.
- `siiaos-livre`: README declares a canonical manuscript that is absent from the current GitHub tree. Repair authority or restore the verified corpus.
- `plateforme` and `mon_vault`: GitHub is only a partial/proposal projection relative to the local corpus.
- `cockpit_d-velopement_territoriaux`: remote and available local snapshot are essentially empty; likely a Building/Profile candidate rather than an autonomous repository.
- multiple OSS forks expose no Yannick-authored commits on GitHub; each must still be checked for local unpublished patches and URL dependencies before reclassification as `EXTERNAL_ANCHOR`.

## Evidence rule

Every final statement should answer:

- observed where?
- observed when?
- by which read-only method?
- is this a fact, derived conclusion, proposal, or unknown?

If a live SandY execution has not happened, write `NOT_PROBED`, never `healthy`, `installed`, `synchronised` or `unused`.
