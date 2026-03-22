#!/usr/bin/env bash
# One Piece Crew — Launch Script (example)
# Usage:
#   ./launch.sh                   # Launch core crew (zoro, nami, robin)
#   ./launch.sh all               # Launch all crew
#   ./launch.sh stop              # Stop all crew sessions
#   ./launch.sh zoro nami         # Launch specific agents

set -euo pipefail

ORG_ROOT="$(cd "$(dirname "$0")" && pwd)"
CREW_DIR="${ORG_ROOT}/_crew"
CHANNEL_PLUGIN=""
CHANNELS_BASE="${HOME}/.claude/channels"
OWNER_ID=""  # Your Telegram user ID (find via @userinfobot)

CORE_CREW=(zoro nami robin)
ALL_CREW=(zoro nami robin)

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

  if [[ -n "${CHANNEL_PLUGIN}" && -f "$env_file" ]]; then
    mkdir -p "$state_dir"
    cp "$env_file" "$state_dir/.env"

    # Auto-provision access.json (bypasses /telegram:access hardcoded path issue)
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
