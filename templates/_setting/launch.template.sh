#!/usr/bin/env bash
# =============================================================================
# {ORGANIZATION_NAME} — Launch Script
# =============================================================================
# Purpose: Initialize the governance environment for a session or deployment.
# Usage:   ./launch.sh [--env {dev|prod}] [--agent {AGENT_NAME}]
# Version: {VERSION}
# =============================================================================

set -euo pipefail

# -----------------------------------------------------------------------------
# Configuration — fill in these values for your organization
# -----------------------------------------------------------------------------

ORG_NAME="{ORGANIZATION_NAME}"
ORG_ROOT="{ABSOLUTE_PATH_TO_PROJECT_ROOT}"
GOVERNANCE_DIR="${ORG_ROOT}/_standard"
CREW_DIR="${ORG_ROOT}/_crew"
LOG_DIR="${ORG_ROOT}/{LOG_DIRECTORY}"
LOG_FILE="${LOG_DIR}/launch-$(date +%Y%m%d-%H%M%S).log"

# Default environment (override with --env flag)
ENV="${LAUNCH_ENV:-dev}"

# Default agent (override with --agent flag)
AGENT="{DEFAULT_AGENT_NAME}"

# Required tools — add any tools your environment depends on
REQUIRED_TOOLS=("{TOOL_1}" "{TOOL_2}")

# Environment-specific settings
DEV_BASE_URL="{DEV_BASE_URL}"
PROD_BASE_URL="{PROD_BASE_URL}"

# -----------------------------------------------------------------------------
# Argument parsing
# -----------------------------------------------------------------------------

while [[ $# -gt 0 ]]; do
  case "$1" in
    --env)
      ENV="$2"
      shift 2
      ;;
    --agent)
      AGENT="$2"
      shift 2
      ;;
    --help|-h)
      echo "Usage: $0 [--env dev|prod] [--agent AGENT_NAME]"
      exit 0
      ;;
    *)
      echo "Unknown argument: $1"
      exit 1
      ;;
  esac
done

# -----------------------------------------------------------------------------
# Logging
# -----------------------------------------------------------------------------

mkdir -p "${LOG_DIR}"

log() {
  local level="$1"
  shift
  local message="$*"
  local timestamp
  timestamp="$(date +%Y-%m-%dT%H:%M:%S)"
  echo "[${timestamp}] [${level}] ${message}" | tee -a "${LOG_FILE}"
}

log INFO "Starting ${ORG_NAME} launch sequence"
log INFO "Environment: ${ENV} | Agent: ${AGENT}"

# -----------------------------------------------------------------------------
# Preflight checks
# -----------------------------------------------------------------------------

log INFO "Running preflight checks..."

# Check required tools
for tool in "${REQUIRED_TOOLS[@]}"; do
  if ! command -v "${tool}" &>/dev/null; then
    log ERROR "Required tool not found: ${tool}"
    exit 1
  fi
  log INFO "  [ok] ${tool}"
done

# Check governance directory
if [[ ! -d "${GOVERNANCE_DIR}" ]]; then
  log ERROR "Governance directory not found: ${GOVERNANCE_DIR}"
  exit 1
fi
log INFO "  [ok] Governance directory exists"

# Check crew directory
if [[ ! -d "${CREW_DIR}" ]]; then
  log ERROR "Crew directory not found: ${CREW_DIR}"
  exit 1
fi
log INFO "  [ok] Crew directory exists"

# Check agent config
AGENT_CONFIG="${CREW_DIR}/${AGENT}.CLAUDE.md"
if [[ ! -f "${AGENT_CONFIG}" ]]; then
  log WARN "Agent config not found: ${AGENT_CONFIG} — using shared crew rules only"
fi

log INFO "Preflight checks passed"

# -----------------------------------------------------------------------------
# Environment setup
# -----------------------------------------------------------------------------

log INFO "Configuring environment: ${ENV}"

case "${ENV}" in
  dev)
    BASE_URL="${DEV_BASE_URL}"
    # Add any dev-specific setup here
    log INFO "  [dev] Base URL: ${BASE_URL}"
    ;;
  prod)
    BASE_URL="${PROD_BASE_URL}"
    # Add any prod-specific setup here
    log INFO "  [prod] Base URL: ${BASE_URL}"
    ;;
  *)
    log ERROR "Unknown environment: ${ENV}. Use 'dev' or 'prod'."
    exit 1
    ;;
esac

export BASE_URL
export ORG_NAME
export ENV

# -----------------------------------------------------------------------------
# Custom initialization steps
# -----------------------------------------------------------------------------
# Add your organization-specific initialization here.
# Examples:
#   - Load secrets from a vault
#   - Authenticate to external services
#   - Seed a database
#   - Start background services

log INFO "Running custom initialization..."

# {CUSTOM_INIT_STEP_1}
# Example: source "${ORG_ROOT}/.env.${ENV}"

# {CUSTOM_INIT_STEP_2}
# Example: ./scripts/seed-data.sh --env "${ENV}"

# {CUSTOM_INIT_STEP_3}

log INFO "Custom initialization complete"

# -----------------------------------------------------------------------------
# Launch
# -----------------------------------------------------------------------------

log INFO "Launching ${ORG_NAME} (env=${ENV}, agent=${AGENT})..."

# Replace the line below with your actual launch command:
# Examples:
#   claude --model {MODEL} --system-prompt "${AGENT_CONFIG}"
#   python main.py --agent "${AGENT}" --env "${ENV}"
#   docker-compose up -d

{LAUNCH_COMMAND}

log INFO "Launch complete. Log: ${LOG_FILE}"

# =============================================================================
# TEMPLATE INSTRUCTIONS:
# 1. Replace all {PLACEHOLDER} values with your actual configuration.
# 2. Fill in REQUIRED_TOOLS with tools your environment actually needs.
# 3. Replace {LAUNCH_COMMAND} with the command that starts your system.
# 4. Add custom initialization steps relevant to your setup.
# 5. Make executable: chmod +x launch.sh
# =============================================================================
