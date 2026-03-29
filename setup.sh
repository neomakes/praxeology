#!/usr/bin/env bash
set -euo pipefail

# ─────────────────────────────────────────────────────
# Praxeology — One-command setup
# git clone https://github.com/neomakes/praxeology.git
# cd praxeology && ./setup.sh
# ─────────────────────────────────────────────────────

PRAX_DIR="$(cd "$(dirname "$0")" && pwd)"
VENV_DIR="$PRAX_DIR/.venv"
MIN_PYTHON="3.10"

echo ""
echo "  ╔═══════════════════════════════════════╗"
echo "  ║   Praxeology — Setup                  ║"
echo "  ║   Model-Agnostic Governance OS        ║"
echo "  ╚═══════════════════════════════════════╝"
echo ""

# ── Step 1: Find Python 3.10+ ──
find_python() {
    for cmd in python3.12 python3.11 python3.10 python3; do
        if command -v "$cmd" &>/dev/null; then
            if "$cmd" -c "import sys; sys.exit(0 if sys.version_info >= (3, 10) else 1)" 2>/dev/null; then
                echo "$cmd"
                return 0
            fi
        fi
    done
    return 1
}

echo "[1/5] Checking Python..."
PYTHON=$(find_python) || {
    echo ""
    echo "  ✗ Python $MIN_PYTHON+ required but not found."
    echo ""
    echo "  Install with:"
    echo "    macOS:   brew install python@3.12"
    echo "    Ubuntu:  sudo apt install python3.12"
    echo "    Windows: https://python.org/downloads/"
    echo ""
    exit 1
}
echo "  ✓ Found: $PYTHON ($($PYTHON --version))"

# ── Step 2: Create venv ──
echo "[2/5] Creating virtual environment..."
if [ -d "$VENV_DIR" ]; then
    echo "  ✓ .venv already exists"
else
    "$PYTHON" -m venv "$VENV_DIR"
    echo "  ✓ Created .venv"
fi

# ── Step 3: Install dependencies ──
echo "[3/5] Installing dependencies..."
"$VENV_DIR/bin/pip" install --upgrade pip -q
"$VENV_DIR/bin/pip" install -e "$PRAX_DIR" -q
echo "  ✓ Installed praxeology-mcp + dependencies"

# ── Step 4: Verify installation ──
echo "[4/5] Verifying..."
"$VENV_DIR/bin/python" -c "from praxeology_mcp.server import mcp; tools = mcp._tool_manager.list_tools(); print(f'  ✓ MCP server: {len(tools)} tools registered')"
"$VENV_DIR/bin/python" -c "from praxeology_mcp.db import init_db; print('  ✓ Database module OK')"

# ── Step 5: Add CLI to PATH ──
echo "[5/5] Setting up CLI..."

# Determine shell config file
SHELL_RC=""
if [ -f "$HOME/.zshrc" ]; then
    SHELL_RC="$HOME/.zshrc"
elif [ -f "$HOME/.bashrc" ]; then
    SHELL_RC="$HOME/.bashrc"
elif [ -f "$HOME/.bash_profile" ]; then
    SHELL_RC="$HOME/.bash_profile"
fi

# Add .venv/bin to PATH (not alias — works even if dir moves)
VENV_BIN="$VENV_DIR/bin"
if [ -n "$SHELL_RC" ]; then
    if ! grep -q "praxeology" "$SHELL_RC" 2>/dev/null; then
        echo "" >> "$SHELL_RC"
        echo "# Praxeology CLI" >> "$SHELL_RC"
        echo "export PATH=\"$VENV_BIN:\$PATH\"" >> "$SHELL_RC"
        echo "  ✓ Added to PATH in $SHELL_RC"
        echo "    Run: source $SHELL_RC (or open new terminal)"
    else
        echo "  ✓ Already in $SHELL_RC"
    fi
else
    echo "  ⚠ Could not detect shell config. Add manually:"
    echo "    export PATH=\"$VENV_BIN:\$PATH\""
fi

# ── Done ──
echo ""
echo "  ╔═══════════════════════════════════════╗"
echo "  ║   ✓ Setup complete!                   ║"
echo "  ╚═══════════════════════════════════════╝"
echo ""
echo "  Next steps:"
echo ""
echo "    # Initialize a new project:"
echo "    praxeology init --name MyOrg --agents 3"
echo ""
echo "    # Or migrate existing Praxeology v1 files:"
echo "    praxeology migrate --project-dir ."
echo ""
echo "    # Claude Code auto-loads .mcp.json — your agents"
echo "    # immediately get 20 governance tools."
echo "    # Ask any agent: what_now()"
echo ""
