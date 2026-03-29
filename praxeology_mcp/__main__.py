"""
Praxeology MCP — entry point.

Dispatch:
    python3 -m praxeology_mcp init ...    → CLI (init command)
    python3 -m praxeology_mcp connect ... → CLI (connect command)
    python3 -m praxeology_mcp            → MCP server
"""

from __future__ import annotations

import sys

_CLI_COMMANDS = {"init", "connect", "migrate", "heartbeat", "dashboard", "status"}


def main() -> None:
    # Route to CLI if first positional argument is a known CLI command.
    args = sys.argv[1:]
    if args and args[0] in _CLI_COMMANDS:
        from praxeology_mcp.cli import main as cli_main
        cli_main()
    else:
        # Fall through to MCP server.
        try:
            from praxeology_mcp.server import main as server_main  # type: ignore[import]
            server_main()
        except ImportError:
            print(
                "MCP server module not found. "
                "Run 'python3 -m praxeology_mcp init --help' for CLI usage.",
                file=sys.stderr,
            )
            sys.exit(1)


if __name__ == "__main__":
    main()
