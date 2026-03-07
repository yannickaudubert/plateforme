from __future__ import annotations

from app.logging import ActionJournal, JournalEntry


def test_action_journal_sqlite_roundtrip(tmp_path) -> None:
    journal = ActionJournal(log_dir=str(tmp_path))
    journal.write(
        JournalEntry(
            timestamp="2026-03-07T10:00:00+00:00",
            tool="system",
            action="startup",
            status="ok",
            details={"environment": "test"},
        )
    )
    journal.write(
        JournalEntry(
            timestamp="2026-03-07T10:01:00+00:00",
            tool="nocodb",
            action="list_bases",
            status="ok",
            details={"result_count": 2},
        )
    )

    entries = journal.read_recent(limit=10)
    assert len(entries) == 2
    assert entries[0].action == "startup"
    assert entries[1].tool == "nocodb"
    assert entries[1].details["result_count"] == 2
    assert (tmp_path / "actions.sqlite3").exists()
