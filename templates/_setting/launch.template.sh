#!/usr/bin/env bash
# =============================================================================
# {ORGANIZATION_NAME} — Crew Launch Script
# =============================================================================
# Launch agents as independent tmux sessions with optional channel integrations.
# Usage:
#   ./launch.sh                     # Launch CORE crew
#   ./launch.sh all                 # Launch ALL crew
#   ./launch.sh stop                # Stop all crew sessions
#   ./launch.sh agent1 agent2 ...   # Launch specific agents
# =============================================================================

set -euo pipefail

# -----------------------------------------------------------------------------
# Configuration — fill in these values for your organization
# -----------------------------------------------------------------------------

ORG_ROOT="{ABSOLUTE_PATH_TO_PROJECT_ROOT}"
CREW_DIR="${ORG_ROOT}/_crew"

# Channel plugin (e.g., "plugin:telegram@claude-plugins-official")
# Leave empty to launch without channel integration.
CHANNEL_PLUGIN="{CHANNEL_PLUGIN}"

# Channel state base directory (per-agent state isolation)
CHANNELS_BASE="${HOME}/.claude/channels"

# Owner's Telegram user ID — used for auto-provisioning allowlist access.
# Find yours: message @userinfobot on Telegram, or check an existing access.json.
OWNER_ID="{OWNER_TELEGRAM_ID}"

# Core crew — minimal set for daily operations
CORE_CREW=({CORE_AGENT_NAMES})

# All crew
ALL_CREW=({ALL_AGENT_NAMES})

# -----------------------------------------------------------------------------
# Launch function
# -----------------------------------------------------------------------------

launch_agent() {
  local name=$1
  local session="crew_${name}"
  local agent_dir="${CREW_DIR}/${name}"
  local env_file="${agent_dir}/.env"
  local state_dir="${CHANNELS_BASE}/${name}"

  if tmux has-session -t "$session" 2>/dev/null; then
    echo "  [skip] $session already running"
    return
  fi

  if [[ ! -d "$agent_dir" ]]; then
    echo "  [skip] $name — directory not found: $agent_dir"
    return
  fi

  # If agent has .env and channel plugin is configured, launch with channel
  if [[ -n "${CHANNEL_PLUGIN}" && -f "$env_file" ]]; then
    mkdir -p "$state_dir"
    cp "$env_file" "$state_dir/.env"

    # Auto-provision access.json with allowlist policy if not exists.
    # KNOWN ISSUE: The /telegram:access skill hardcodes ~/.claude/channels/telegram/
    # and ignores TELEGRAM_STATE_DIR. This auto-provisioning bypasses that limitation
    # by writing access.json directly to the per-agent state directory.
    if [[ ! -f "$state_dir/access.json" && -n "${OWNER_ID}" ]]; then
      cat > "$state_dir/access.json" <<EOJSON
{
  "dmPolicy": "allowlist",
  "allowFrom": ["${OWNER_ID}"],
  "groups": {},
  "pending": {}
}
EOJSON
      chmod 600 "$state_dir/access.json"
      echo "  [init] $name access.json provisioned (owner: ${OWNER_ID})"
    fi

    tmux new-session -d -s "$session" \
      "cd $agent_dir && TELEGRAM_STATE_DIR=$state_dir claude --channels $CHANNEL_PLUGIN"
    echo "  [ok]   $session launched (channel: $name)"
  else
    tmux new-session -d -s "$session" \
      "cd $agent_dir && claude"
    echo "  [ok]   $session launched (no channel)"
  fi
}

# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

case "${1:-core}" in
  all)
    echo "Launching ALL crew (${#ALL_CREW[@]} members)..."
    for c in "${ALL_CREW[@]}"; do launch_agent "$c"; done
    ;;
  core)
    echo "Launching CORE crew (${#CORE_CREW[@]} members)..."
    for c in "${CORE_CREW[@]}"; do launch_agent "$c"; done
    ;;
  stop)
    echo "Stopping all crew sessions..."
    for c in "${ALL_CREW[@]}"; do
      tmux kill-session -t "crew_${c}" 2>/dev/null && echo "  [ok] crew_${c} stopped" || true
    done
    ;;
  *)
    echo "Launching crew: $*"
    for c in "$@"; do
      if [[ " ${ALL_CREW[*]} " =~ " $c " ]]; then
        launch_agent "$c"
      else
        echo "  [skip] Unknown: $c (available: ${ALL_CREW[*]})"
      fi
    done
    ;;
esac

echo ""
echo "Active crew sessions:"
tmux list-sessions 2>/dev/null | grep crew_ || echo "  (none)"

# =============================================================================
# TEMPLATE INSTRUCTIONS:
# 1. Replace {ABSOLUTE_PATH_TO_PROJECT_ROOT} with your org root path.
# 2. Replace {CHANNEL_PLUGIN} with your channel plugin string, or leave empty.
# 3. Replace {CORE_AGENT_NAMES} and {ALL_AGENT_NAMES} with agent names.
# 4. Each agent needs _crew/{name}/CLAUDE.md for persona.
# 5. For channel integration, add _crew/{name}/.env with the bot token.
# 6. Make executable: chmod +x launch.sh
# =============================================================================
