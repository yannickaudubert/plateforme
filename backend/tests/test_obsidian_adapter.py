from __future__ import annotations

from pathlib import Path

import pytest

from app.adapters.obsidian import (
    ObsidianAdapter,
    ObsidianConflictError,
    ObsidianPathError,
    ObsidianPreconditionError,
)


def _make_adapter(vault: Path) -> ObsidianAdapter:
    vault.mkdir(parents=True, exist_ok=True)
    return ObsidianAdapter(vault_path=str(vault), allowed_roots=[str(vault)])


def test_path_guardrails_block_internal_and_traversal_paths(tmp_path: Path) -> None:
    adapter = _make_adapter(tmp_path / "vault")

    with pytest.raises(ObsidianPathError):
        adapter.create_note(".obsidian/config.md", "x")

    with pytest.raises(ObsidianPathError):
        adapter.create_note(".cockpit-backups/dump.md", "x")

    with pytest.raises(ObsidianPathError):
        adapter.create_note("../escape.md", "x")


def test_create_read_update_with_precondition_and_backup(tmp_path: Path) -> None:
    adapter = _make_adapter(tmp_path / "vault")
    path = "projects/mission.md"

    created = adapter.create_note(note_path=path, content="initial")
    assert created.status == "created"

    with pytest.raises(ObsidianConflictError):
        adapter.create_note(note_path=path, content="duplicate")

    read = adapter.read_note(path)
    assert read.path == path
    assert read.content == "initial"
    assert read.modified_at

    with pytest.raises(ObsidianPreconditionError):
        adapter.update_note(
            note_path=path,
            content="new-content",
            expected_modified_at="1970-01-01T00:00:00+00:00",
            create_backup=True,
        )

    updated = adapter.update_note(
        note_path=path,
        content="new-content",
        expected_modified_at=read.modified_at,
        create_backup=True,
    )
    assert updated.status == "updated"
    assert updated.modified_at != read.modified_at

    updated_read = adapter.read_note(path)
    assert updated_read.content == "new-content"

    backup_files = list((adapter.vault_path / ".cockpit-backups").rglob("*.bak.md"))
    assert backup_files
