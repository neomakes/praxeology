"""
Praxeology MCP — server entry point.

Sets up the FastMCP instance, initialises the database, and registers
all axis tool modules.
"""

from __future__ import annotations

import os

from mcp.server.fastmcp import FastMCP

from praxeology_mcp.db import init_db
from praxeology_mcp.heartbeat import Heartbeat

# ---------------------------------------------------------------------------
# FastMCP instance — shared across all axis modules
# ---------------------------------------------------------------------------

mcp = FastMCP("praxeology")

# ---------------------------------------------------------------------------
# DB initialisation
# ---------------------------------------------------------------------------

_DEFAULT_DB = os.path.expanduser("~/.claude/praxeology/praxeology.db")


def _ensure_db() -> None:
    db_path = os.environ.get("PRAXEOLOGY_DB", _DEFAULT_DB)
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    init_db(db_path)


# ---------------------------------------------------------------------------
# Register axis tools
# ---------------------------------------------------------------------------

from praxeology_mcp.axes import logical  # noqa: E402
from praxeology_mcp.axes import tactical  # noqa: E402
from praxeology_mcp.axes import contextual  # noqa: E402
from praxeology_mcp import cross  # noqa: E402

logical.register(mcp)
tactical.register(mcp)
contextual.register(mcp)
cross.register(mcp)

# ---------------------------------------------------------------------------
# Startup
# ---------------------------------------------------------------------------

_ensure_db()

_db_path = os.environ.get("PRAXEOLOGY_DB", _DEFAULT_DB)
_heartbeat = Heartbeat(_db_path)
_heartbeat.start()


def main() -> None:
    """Run the MCP server (called by __main__.py)."""
    mcp.run()
