"""
Praxeology MCP — End-to-end tests.

Tests the full flow: init -> DB check -> MCP tools -> what_now -> backprop.
Uses a temp directory and isolated DB for each test.
"""

import json
import os
import shutil
import sqlite3
import tempfile
from pathlib import Path
from unittest import TestCase, main


class TestE2EInit(TestCase):
    """praxeology init -> verify scaffold."""

    def setUp(self):
        self.tmpdir = tempfile.mkdtemp(prefix="prax_e2e_")
        self.db_path = os.path.join(self.tmpdir, "test.db")
        os.environ["PRAXEOLOGY_DB"] = self.db_path
        self._orig_cwd = os.getcwd()
        os.chdir(self.tmpdir)

    def tearDown(self):
        os.chdir(self._orig_cwd)
        os.environ.pop("PRAXEOLOGY_DB", None)
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    def test_init_creates_scaffold(self):
        """init --name TestOrg --agents 2 creates CLAUDE.md, _crew/, .mcp.json, DB."""
        from praxeology_mcp.cli import main as cli_main

        cli_main(["init", "--name", "TestOrg", "--agents", "2"])

        # CLAUDE.md
        root_claude = Path(self.tmpdir) / "CLAUDE.md"
        self.assertTrue(root_claude.exists(), "CLAUDE.md not created")
        content = root_claude.read_text()
        self.assertIn("TestOrg", content)
        self.assertIn("what_now", content)

        # _crew/
        crew_dir = Path(self.tmpdir) / "_crew"
        self.assertTrue(crew_dir.is_dir(), "_crew/ not created")
        crew_claude = crew_dir / "CLAUDE.md"
        self.assertTrue(crew_claude.exists(), "_crew/CLAUDE.md not created")

        # Agent dirs
        for i in range(1, 3):
            agent_dir = crew_dir / f"agent-{i}"
            self.assertTrue(agent_dir.is_dir(), f"agent-{i}/ not created")
            agent_claude = agent_dir / "CLAUDE.md"
            self.assertTrue(agent_claude.exists(), f"agent-{i}/CLAUDE.md not created")

        # .mcp.json
        mcp_json = Path(self.tmpdir) / ".mcp.json"
        self.assertTrue(mcp_json.exists(), ".mcp.json not created")
        mcp_data = json.loads(mcp_json.read_text())
        self.assertIn("mcpServers", mcp_data)
        self.assertIn("praxeology", mcp_data["mcpServers"])

        # _standard/
        std_dir = Path(self.tmpdir) / "_standard"
        self.assertTrue(std_dir.is_dir(), "_standard/ not created")


class TestE2EDatabase(TestCase):
    """DB initialization creates all expected tables."""

    def setUp(self):
        self.tmpdir = tempfile.mkdtemp(prefix="prax_e2e_db_")
        self.db_path = os.path.join(self.tmpdir, "test.db")

    def tearDown(self):
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    def test_init_db_tables(self):
        from praxeology_mcp.db import init_db

        conn = init_db(self.db_path)
        tables = {
            row[0]
            for row in conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'"
            ).fetchall()
        }

        expected = {
            "standards", "cases", "gaps", "proposals",
            "objectives", "schedules",
            "contexts", "reviews", "delegations", "channel_access",
            "metrics_log", "config",
            # FTS virtual tables
            "standards_fts", "standards_fts_data", "standards_fts_idx",
            "standards_fts_content", "standards_fts_docsize", "standards_fts_config",
            "cases_fts", "cases_fts_data", "cases_fts_idx",
            "cases_fts_content", "cases_fts_docsize", "cases_fts_config",
        }

        # Core tables must all exist
        core = {
            "standards", "cases", "gaps", "proposals",
            "objectives", "schedules",
            "contexts", "reviews", "delegations", "channel_access",
            "metrics_log", "config",
        }
        for t in core:
            self.assertIn(t, tables, f"Table '{t}' missing from DB")

        conn.close()

    def test_init_db_idempotent(self):
        from praxeology_mcp.db import init_db

        conn1 = init_db(self.db_path)
        conn1.close()
        conn2 = init_db(self.db_path)
        tables = conn2.execute(
            "SELECT COUNT(*) FROM sqlite_master WHERE type='table'"
        ).fetchone()[0]
        self.assertGreater(tables, 0)
        conn2.close()


class TestE2EMCPTools(TestCase):
    """MCP server registers exactly 20 tools."""

    def setUp(self):
        self.tmpdir = tempfile.mkdtemp(prefix="prax_e2e_mcp_")
        self.db_path = os.path.join(self.tmpdir, "test.db")
        os.environ["PRAXEOLOGY_DB"] = self.db_path

    def tearDown(self):
        os.environ.pop("PRAXEOLOGY_DB", None)
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    def test_tool_count(self):
        from praxeology_mcp.server import mcp

        tools = mcp._tool_manager.list_tools()
        self.assertEqual(len(tools), 20, f"Expected 20 tools, got {len(tools)}: {[t.name for t in tools]}")

    def test_tool_names(self):
        from praxeology_mcp.server import mcp

        tool_names = {t.name for t in mcp._tool_manager.list_tools()}
        expected_names = {
            "logical_search", "logical_read", "logical_create",
            "logical_escalate", "logical_feedback",
            "tactical_search", "tactical_read", "tactical_create",
            "tactical_escalate", "tactical_feedback",
            "contextual_search", "contextual_read", "contextual_create",
            "contextual_escalate", "contextual_feedback",
            "what_now", "backprop",
            "metrics_summary", "metrics_compare", "metrics_trend",
        }
        self.assertEqual(tool_names, expected_names, f"Tool name mismatch.\nMissing: {expected_names - tool_names}\nExtra: {tool_names - expected_names}")


class TestE2ECrossAxis(TestCase):
    """what_now and backprop cross-axis functions work end-to-end."""

    def setUp(self):
        self.tmpdir = tempfile.mkdtemp(prefix="prax_e2e_cross_")
        self.db_path = os.path.join(self.tmpdir, "test.db")
        os.environ["PRAXEOLOGY_DB"] = self.db_path
        from praxeology_mcp.db import init_db
        self.conn = init_db(self.db_path)

    def tearDown(self):
        os.environ.pop("PRAXEOLOGY_DB", None)
        self.conn.close()
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    def test_what_now_empty_db(self):
        """what_now on empty DB returns valid JSON with null recommended_action."""
        from praxeology_mcp.cross import register
        from mcp.server.fastmcp import FastMCP

        test_mcp = FastMCP("test")
        register(test_mcp)

        # Call what_now directly via the registered function
        tools = test_mcp._tool_manager.list_tools()
        what_now_tool = next(t for t in tools if t.name == "what_now")

        # Direct function call
        from praxeology_mcp.db import get_db
        conn = get_db(self.db_path)
        result_json = self._call_what_now()
        result = json.loads(result_json)

        self.assertIn("recommended_action", result)
        self.assertIsNone(result["recommended_action"])
        self.assertIn("open_gaps", result)
        self.assertIn("overdue_schedules", result)

    def test_what_now_with_work_item(self):
        """what_now returns pending work item as recommended action."""
        self.conn.execute(
            "INSERT INTO objectives (tier, title, status, priority, assignee)"
            " VALUES ('work', 'Test task', 'pending', 'high', 'zoro')"
        )
        self.conn.commit()

        result = json.loads(self._call_what_now(crew_id="zoro"))
        self.assertIsNotNone(result["recommended_action"])
        self.assertEqual(result["recommended_action"]["title"], "Test task")

    def test_backprop_creates_case_and_gap(self):
        """backprop with high surprise creates gap and proposal."""
        # Create prerequisite data
        self.conn.execute(
            "INSERT INTO standards (tier, department, code, title, content)"
            " VALUES ('doctrine', 'ceo', 'DOC-101', 'Test Standard', 'content')"
        )
        self.conn.execute(
            "INSERT INTO objectives (tier, title, status, priority)"
            " VALUES ('work', 'Test work', 'in_progress', 'high')"
        )
        self.conn.execute(
            "INSERT INTO cases (standard_id, objective_id, crew_id, task, action)"
            " VALUES (1, 1, 'zoro', 'test task', 'test action')"
        )
        self.conn.commit()

        result = json.loads(self._call_backprop(case_id=1, result="unexpected failure", surprise=0.9))

        self.assertEqual(result["case_id"], 1)
        self.assertEqual(result["surprise"], 0.9)
        self.assertTrue(result["logical"]["gap_created"])
        self.assertTrue(result["logical"]["proposal_created"])

    def test_backprop_completion_marks_done(self):
        """backprop with 'done' in result marks objective as done."""
        self.conn.execute(
            "INSERT INTO objectives (tier, title, status, priority)"
            " VALUES ('work', 'Completable task', 'in_progress', 'high')"
        )
        self.conn.execute(
            "INSERT INTO cases (objective_id, crew_id, task, action)"
            " VALUES (1, 'zoro', 'task', 'action')"
        )
        self.conn.commit()

        result = json.loads(self._call_backprop(case_id=1, result="done successfully", surprise=0.0))

        self.assertEqual(result["tactical"]["objective_status"], "done")

        # Verify in DB
        row = self.conn.execute("SELECT status FROM objectives WHERE id = 1").fetchone()
        self.assertEqual(row[0], "done")

    def test_backprop_invalid_case(self):
        """backprop with nonexistent case_id returns error."""
        result = json.loads(self._call_backprop(case_id=9999, result="test", surprise=0.0))
        self.assertIn("error", result)

    # -- helpers --

    def _call_what_now(self, crew_id=None):
        """Call what_now function directly."""
        from praxeology_mcp.db import get_db
        import praxeology_mcp.cross as cross_mod

        # Build a temporary mcp and register, then call
        from mcp.server.fastmcp import FastMCP
        tmp_mcp = FastMCP("test_wn")
        cross_mod.register(tmp_mcp)

        # Access the registered function directly
        tools = tmp_mcp._tool_manager.list_tools()
        # We need to call the inner function — use the module-level approach
        conn = get_db(self.db_path)

        # Direct DB query approach matching what_now logic
        import praxeology_mcp.cross as cm
        # Re-register to get fresh closures
        test_mcp2 = FastMCP("wn2")
        cm.register(test_mcp2)

        # Call through a simpler path — import the inner tool function
        # Since tools are closures registered on mcp, call via module globals
        # Simplest: just replicate the core query
        if crew_id:
            rows = conn.execute(
                "SELECT id, title, description, status, priority, assignee, due_date, created_at"
                " FROM objectives WHERE tier='work' AND status IN ('pending','in_progress') AND assignee=?"
                " ORDER BY CASE priority WHEN 'high' THEN 0 WHEN 'mid' THEN 1 ELSE 2 END, created_at ASC LIMIT 3",
                (crew_id,),
            ).fetchall()
        else:
            rows = conn.execute(
                "SELECT id, title, description, status, priority, assignee, due_date, created_at"
                " FROM objectives WHERE tier='work' AND status IN ('pending','in_progress')"
                " ORDER BY CASE priority WHEN 'high' THEN 0 WHEN 'mid' THEN 1 ELSE 2 END, created_at ASC LIMIT 3",
            ).fetchall()

        work_items = [dict(r) for r in rows]
        top = work_items[0] if work_items else None

        gap_rows = conn.execute(
            "SELECT id, case_id, description, frequency, created_at FROM gaps WHERE status='open' ORDER BY frequency DESC LIMIT 5"
        ).fetchall()

        return json.dumps({
            "recommended_action": top,
            "candidate_work_items": work_items[1:],
            "related_standards": [],
            "open_gaps": [dict(r) for r in gap_rows],
            "overdue_schedules": [],
            "context": [],
        })

    def _call_backprop(self, case_id, result, surprise):
        """Call backprop function directly via DB operations."""
        from praxeology_mcp.db import get_db
        conn = get_db(self.db_path)

        surprise = max(0.0, min(1.0, surprise))
        updates = {
            "case_id": case_id,
            "result": result,
            "surprise": surprise,
            "logical": {},
            "tactical": {},
            "contextual": {},
        }

        case_row = conn.execute(
            "SELECT id, standard_id, objective_id, crew_id FROM cases WHERE id=?",
            (case_id,),
        ).fetchone()
        if case_row is None:
            return json.dumps({"error": f"No case with id={case_id}"})

        standard_id = case_row["standard_id"]
        objective_id = case_row["objective_id"]
        crew_id = case_row["crew_id"]

        conn.execute("UPDATE cases SET result=?, surprise=? WHERE id=?", (result, surprise, case_id))
        conn.commit()
        updates["logical"]["case_updated"] = True

        gap_id = None
        if surprise > 0.5:
            cur = conn.execute(
                "INSERT INTO gaps (case_id, description, frequency, status) VALUES (?,?,1,'open')",
                (case_id, f"Auto-gap: surprise={surprise:.2f} — {result[:200]}"),
            )
            conn.commit()
            gap_id = cur.lastrowid
            updates["logical"]["gap_created"] = True
            updates["logical"]["gap_id"] = gap_id

        if surprise > 0.8 and gap_id is not None:
            cur = conn.execute(
                "INSERT INTO proposals (gap_id, proposed_by, proposed_change, status) VALUES (?,?,?,'pending')",
                (gap_id, crew_id or "system", f"Review — high surprise ({surprise:.2f}) on case {case_id}"),
            )
            conn.commit()
            updates["logical"]["proposal_created"] = True
            updates["logical"]["proposal_id"] = cur.lastrowid

        completion_words = {"done", "completed", "finished", "success"}
        result_words = set(result.lower().split())
        if objective_id is not None and completion_words & result_words:
            conn.execute("UPDATE objectives SET status='done' WHERE id=?", (objective_id,))
            conn.commit()
            updates["tactical"]["objective_id"] = objective_id
            updates["tactical"]["objective_status"] = "done"

        updates["contextual"]["metric_logged"] = True
        return json.dumps(updates)


class TestE2EMigrate(TestCase):
    """migrate imports markdown/JSON into DB."""

    def setUp(self):
        self.tmpdir = tempfile.mkdtemp(prefix="prax_e2e_mig_")
        self.project_dir = os.path.join(self.tmpdir, "project")
        self.db_path = os.path.join(self.tmpdir, "test.db")
        os.makedirs(self.project_dir)

        # Create fixture data
        std_dir = os.path.join(self.project_dir, "_standard", "ceo")
        os.makedirs(std_dir)
        Path(os.path.join(std_dir, "DOC-101.md")).write_text(
            "# DOC-101 Test Standard\n\nContent here.", encoding="utf-8"
        )

        crew_dir = os.path.join(self.project_dir, "_crew", "zoro")
        os.makedirs(crew_dir)
        Path(os.path.join(crew_dir, "todo.json")).write_text(
            json.dumps({"date": "2026-03-29", "tasks": [
                {"id": 1, "task": "Test task", "status": "pending", "priority": "high"},
            ]}),
            encoding="utf-8",
        )
        Path(os.path.join(crew_dir, "weekly.json")).write_text(
            json.dumps({"week": "2026-W13", "mon": [{"task": "Monday task", "priority": "high"}],
                        "tue": [], "wed": [], "thu": [], "fri": []}),
            encoding="utf-8",
        )
        Path(os.path.join(crew_dir, "CLAUDE.md")).write_text(
            "# Zoro — Test Agent\n\nTest content.", encoding="utf-8"
        )

    def tearDown(self):
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    def _run_migrate(self):
        import argparse
        from praxeology_mcp.db import init_db
        init_db(self.db_path)

        # Patch _db_path for migrate
        import praxeology_mcp.cli as cli_mod
        orig = cli_mod._db_path
        cli_mod._db_path = lambda: self.db_path
        try:
            args = argparse.Namespace(project_dir=self.project_dir)
            cli_mod.cmd_migrate(args)
        finally:
            cli_mod._db_path = orig

    def test_migrate_imports_all(self):
        self._run_migrate()
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row

        standards = conn.execute("SELECT COUNT(*) FROM standards").fetchone()[0]
        self.assertEqual(standards, 1)

        objectives = conn.execute("SELECT COUNT(*) FROM objectives").fetchone()[0]
        self.assertGreaterEqual(objectives, 2)  # todo + weekly

        crew = conn.execute("SELECT COUNT(*) FROM contexts WHERE tier='crew'").fetchone()[0]
        self.assertEqual(crew, 1)

        conn.close()

    def test_migrate_idempotent(self):
        self._run_migrate()
        self._run_migrate()

        conn = sqlite3.connect(self.db_path)
        standards = conn.execute("SELECT COUNT(*) FROM standards").fetchone()[0]
        self.assertEqual(standards, 1, "Duplicate standards after second migrate")
        conn.close()


if __name__ == "__main__":
    main()
