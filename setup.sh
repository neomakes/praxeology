#!/usr/bin/env bash
# =============================================================================
# Praxeology Framework Setup Wizard
# =============================================================================
# Interactive onboarding script. Generates a full governance directory.
# Usage: bash setup.sh
# =============================================================================

set -euo pipefail

# ─── Bash version check ──────────────────────────────────────────────────────
if ((BASH_VERSINFO[0] < 4)); then
  echo "Error: Requires bash 4+. macOS users: brew install bash"
  exit 1
fi

# ─── Colors ──────────────────────────────────────────────────────────────────
BOLD="\033[1m"
DIM="\033[2m"
CYAN="\033[36m"
GREEN="\033[32m"
YELLOW="\033[33m"
RED="\033[31m"
RESET="\033[0m"

# ─── Helpers ─────────────────────────────────────────────────────────────────
print_header() {
  echo ""
  echo -e "${CYAN}${BOLD}╔══════════════════════════════════════════════════════════╗${RESET}"
  echo -e "${CYAN}${BOLD}║           Praxeology Framework Setup Wizard              ║${RESET}"
  echo -e "${CYAN}${BOLD}║      Standard-based Hierarchical Governance              ║${RESET}"
  echo -e "${CYAN}${BOLD}╚══════════════════════════════════════════════════════════╝${RESET}"
  echo ""
}

print_section() {
  echo ""
  echo -e "${BOLD}── $1 $( printf '─%.0s' $(seq 1 $((50 - ${#1}))) )${RESET}"
  echo ""
}

prompt() {
  local label="$1"
  local default="${2:-}"
  local var_name="$3"
  if [ -n "$default" ]; then
    echo -ne "${BOLD}${label}${RESET} ${DIM}[${default}]${RESET}: "
  else
    echo -ne "${BOLD}${label}${RESET}: "
  fi
  read -r input
  if [ -z "$input" ] && [ -n "$default" ]; then
    input="$default"
  fi
  printf -v "$var_name" '%s' "$input"
}

confirm() {
  local label="$1"
  local default="${2:-y}"
  echo -ne "${BOLD}${label}${RESET} ${DIM}[${default}]${RESET}: "
  read -r input
  input="${input:-$default}"
  [[ "$input" =~ ^[Yy] ]]
}

# ─── Script root ─────────────────────────────────────────────────────────────
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# =============================================================================
# STEP 0 — Welcome
# =============================================================================
print_header

echo -e "This wizard creates a complete governance system based on the Praxeology"
echo -e "4+1 tier framework: ${CYAN}Strategy → Doctrine → Procedure → Playbook → Execution${RESET}"
echo ""
echo -e "${DIM}Press Enter to accept defaults. Ctrl+C to cancel at any time.${RESET}"

# =============================================================================
# STEP 1 — Organization basics
# =============================================================================
print_section "Organization"

prompt "Organization name" "MyOrg" ORG_NAME
prompt "One-line mission" "Build excellent things" ORG_MISSION
prompt "Organization type (company/lab/team/personal)" "company" ORG_TYPE
prompt "Governance version" "1.0.0" GOV_VERSION
ENACTED_DATE=$(date +%Y-%m-%d)

prompt "Target directory (absolute or relative)" "./${ORG_NAME,,}" TARGET_DIR

# Resolve to absolute
if [[ "$TARGET_DIR" != /* ]]; then
  TARGET_DIR="$(pwd)/${TARGET_DIR}"
fi

echo ""
echo -e "  Name    : ${CYAN}${ORG_NAME}${RESET}"
echo -e "  Mission : ${CYAN}${ORG_MISSION}${RESET}"
echo -e "  Type    : ${CYAN}${ORG_TYPE}${RESET}"
echo -e "  Path    : ${CYAN}${TARGET_DIR}${RESET}"

echo ""
if ! confirm "Looks good? Proceed with these values? (y/n)" "y"; then
  echo -e "${YELLOW}Aborted.${RESET}"
  exit 0
fi

# =============================================================================
# STEP 2 — Departments
# =============================================================================
print_section "Departments"

echo -e "Select departments to enable. Press Enter to accept default (all 7)."
echo ""

DEPT_CODES=(ceo coo cfo cto cdo chro ciso)
DEPT_NAMES=("CEO — Strategy & Vision (1xx)"
            "COO — Operations & Execution (2xx)"
            "CFO — Finance & Resources (3xx)"
            "CTO — Technology & R\&D (4xx)"
            "CDO — Diplomacy & Network (5xx)"
            "CHRO — HR & Wellbeing (6xx)"
            "CISO — Intelligence & Security (7xx)")

ENABLED_DEPTS=()

for i in "${!DEPT_CODES[@]}"; do
  echo -ne "  Enable ${BOLD}${DEPT_NAMES[$i]}${RESET}? ${DIM}[y]${RESET}: "
  read -r choice
  choice="${choice:-y}"
  if [[ "$choice" =~ ^[Yy] ]]; then
    ENABLED_DEPTS+=("${DEPT_CODES[$i]}")
    echo -e "    ${GREEN}✓ enabled${RESET}"
  else
    echo -e "    ${DIM}skipped${RESET}"
  fi
done

echo ""
echo -e "  Enabled: ${CYAN}${ENABLED_DEPTS[*]}${RESET}"

# =============================================================================
# STEP 3 — Agents / Crew members
# =============================================================================
print_section "Agents / Crew"

prompt "Number of agents to register" "0" AGENT_COUNT

declare -a AGENT_NAMES=()
declare -a AGENT_DEPTS=()
declare -a AGENT_ROLES=()

if [ "$AGENT_COUNT" -gt 0 ] 2>/dev/null; then
  for (( i=1; i<=AGENT_COUNT; i++ )); do
    echo ""
    echo -e "  ${BOLD}Agent $i${RESET}"
    prompt "    Name (slug, no spaces)" "agent${i}" _aname
    prompt "    Department code (${ENABLED_DEPTS[*]})" "${ENABLED_DEPTS[0]:-ceo}" _adept
    prompt "    Role / title" "Specialist" _arole
    AGENT_NAMES+=("$_aname")
    AGENT_DEPTS+=("$_adept")
    AGENT_ROLES+=("$_arole")
  done
fi

# =============================================================================
# STEP 4 — Projects
# =============================================================================
print_section "Projects"

prompt "Project names to register (comma-separated, or leave blank)" "" RAW_PROJECTS

PROJECTS=()
if [ -n "$RAW_PROJECTS" ]; then
  IFS=',' read -ra PROJECTS <<< "$RAW_PROJECTS"
fi

# =============================================================================
# STEP 5 — Language preference
# =============================================================================
print_section "Language"

echo -e "  en — English (default)"
echo -e "  ko — Korean"
echo ""
prompt "Language preference" "en" LANG_PREF

# =============================================================================
# STEP 6 — Telegram integration
# =============================================================================
print_section "Integrations"

TELEGRAM_ENABLED=false
if confirm "Enable Telegram bot integration? (y/n)" "n"; then
  TELEGRAM_ENABLED=true
  prompt "Telegram bot token (or leave blank to set later)" "" TG_BOT_TOKEN
  prompt "Telegram chat ID (or leave blank to set later)" "" TG_CHAT_ID
fi

# =============================================================================
# STEP 7 — Confirm and generate
# =============================================================================
print_section "Summary"

echo -e "  Organization : ${CYAN}${ORG_NAME}${RESET}"
echo -e "  Mission      : ${CYAN}${ORG_MISSION}${RESET}"
echo -e "  Type         : ${CYAN}${ORG_TYPE}${RESET}"
echo -e "  Version      : ${CYAN}${GOV_VERSION}${RESET}"
echo -e "  Enacted      : ${CYAN}${ENACTED_DATE}${RESET}"
echo -e "  Path         : ${CYAN}${TARGET_DIR}${RESET}"
echo -e "  Departments  : ${CYAN}${ENABLED_DEPTS[*]}${RESET}"
echo -e "  Agents       : ${CYAN}${AGENT_COUNT}${RESET}"
echo -e "  Projects     : ${CYAN}${PROJECTS[*]:-none}${RESET}"
echo -e "  Language     : ${CYAN}${LANG_PREF}${RESET}"
echo -e "  Telegram     : ${CYAN}${TELEGRAM_ENABLED}${RESET}"
echo ""

if ! confirm "Generate governance system at ${TARGET_DIR}? (y/n)" "y"; then
  echo -e "${YELLOW}Aborted.${RESET}"
  exit 0
fi

# =============================================================================
# GENERATION
# =============================================================================
print_section "Generating"

# Department metadata
dept_title() {
  case "$1" in
    ceo)  echo "Strategy & Vision" ;;
    coo)  echo "Operations & Execution" ;;
    cfo)  echo "Finance & Resources" ;;
    cto)  echo "Technology & R&D" ;;
    cdo)  echo "Diplomacy & Network" ;;
    chro) echo "HR & Wellbeing" ;;
    ciso) echo "Intelligence & Security" ;;
    *)    echo "General" ;;
  esac
}

dept_code_range() {
  case "$1" in
    ceo)  echo "1xx" ;;
    coo)  echo "2xx" ;;
    cfo)  echo "3xx" ;;
    cto)  echo "4xx" ;;
    cdo)  echo "5xx" ;;
    chro) echo "6xx" ;;
    ciso) echo "7xx" ;;
    *)    echo "0xx" ;;
  esac
}

dept_clevel() {
  case "$1" in
    ceo)  echo "Chief Executive Officer" ;;
    coo)  echo "Chief Operating Officer" ;;
    cfo)  echo "Chief Financial Officer" ;;
    cto)  echo "Chief Technology Officer" ;;
    cdo)  echo "Chief Diplomacy Officer" ;;
    chro) echo "Chief HR Officer" ;;
    ciso) echo "Chief Intelligence & Security Officer" ;;
    *)    echo "Director" ;;
  esac
}

# ─── Create directory skeleton ────────────────────────────────────────────────
echo -ne "  Creating directories... "
mkdir -p "${TARGET_DIR}/_standard"
mkdir -p "${TARGET_DIR}/_crew"
mkdir -p "${TARGET_DIR}/_project/.praxe"
mkdir -p "${TARGET_DIR}/_setting"
mkdir -p "${TARGET_DIR}/docs"
echo -e "${GREEN}done${RESET}"

# ─── Department documents ────────────────────────────────────────────────────
echo -ne "  Generating department governance... "
for dept in "${ENABLED_DEPTS[@]}"; do
  dept_dir="${TARGET_DIR}/_standard/${dept}"
  mkdir -p "$dept_dir"
  dt=$(dept_title "$dept")
  dc=$(dept_code_range "$dept")
  cl=$(dept_clevel "$dept")
  UPPER_DEPT="${dept^^}"

  # strategy.md
  cat > "${dept_dir}/strategy.md" << EOF
# ${UPPER_DEPT} Strategy — ${dt} (${dc})

> Tier 1 | WHY | ${ORG_NAME} | v${GOV_VERSION} | Enacted ${ENACTED_DATE}

## Mission

${ORG_MISSION}

## Strategic Objectives

1. [Define primary objective for ${dt}]
2. [Define secondary objective]
3. [Define tertiary objective]

## Core Values

- [Value 1]
- [Value 2]
- [Value 3]

## Long-Term Vision (3–5 years)

[Describe the desired end state for ${dt} over the next 3–5 years.]

---

_Authority: Founding-level. Requires full board ratification to amend._
EOF

  # doctrine.md
  cat > "${dept_dir}/doctrine.md" << EOF
# ${UPPER_DEPT} Doctrine — ${dt} (${dc})

> Tier 2 | WHAT | ${ORG_NAME} | v${GOV_VERSION} | Enacted ${ENACTED_DATE}

## Governing Principles

These principles define what ${UPPER_DEPT} will and will not do.

### Will Do

1. [Commitment 1]
2. [Commitment 2]
3. [Commitment 3]

### Will Not Do

1. [Hard limit 1 — SafetyGate]
2. [Hard limit 2]

## Scope & Boundaries

- **In scope**: [What falls within ${UPPER_DEPT}'s authority]
- **Out of scope**: [What is explicitly excluded]

## Relationship to Other Departments

| Department | Relationship |
|-----------|-------------|
| [Dept] | [Nature of coordination] |

---

_Authority: Board-level. Requires executive approval to amend._
EOF

  # procedure.md
  cat > "${dept_dir}/procedure.md" << EOF
# ${UPPER_DEPT} Procedure — ${dt} (${dc})

> Tier 3 | HOW | ${ORG_NAME} | v${GOV_VERSION} | Enacted ${ENACTED_DATE}

## Resource Allocation

### Budget

[Describe budget authority and allocation process for ${UPPER_DEPT}.]

### People

[Describe staffing and delegation for ${UPPER_DEPT}.]

### Time

[Describe time allocation and scheduling norms for ${UPPER_DEPT}.]

## Core Processes

### Process 1: [Name]

1. Trigger: [What initiates this process]
2. Steps: [Step-by-step]
3. Output: [What is produced]
4. Owner: [Role responsible]

### Process 2: [Name]

1. Trigger:
2. Steps:
3. Output:
4. Owner:

## Review Cadence

| Review | Frequency | Owner |
|--------|-----------|-------|
| Procedure review | Quarterly | ${cl} |
| Metrics review | Monthly | ${cl} |

---

_Authority: Executive-level. Quarterly review cycle._
EOF

  # playbook.md
  cat > "${dept_dir}/playbook.md" << EOF
# ${UPPER_DEPT} Playbook — ${dt} (${dc})

> Tier 4 | PATTERNS | ${ORG_NAME} | v${GOV_VERSION} | Enacted ${ENACTED_DATE}

## Pattern Library

Patterns are proven approaches that have worked in practice. They are not mandated — they are recommended starting points.

### Pattern 1: [Name]

**Context**: [When this pattern applies]
**Approach**: [What to do]
**Outcome**: [What to expect]
**Variants**: [Known adaptations]

### Pattern 2: [Name]

**Context**:
**Approach**:
**Outcome**:
**Variants**:

## Anti-Patterns

| Anti-Pattern | Why to Avoid | Better Alternative |
|-------------|-------------|-------------------|
| [Name] | [Reason] | [Alternative] |

## Playbook Evolution

New patterns are proposed via the Proposal process, trialed for 30 days, then ratified or discarded.

---

_Authority: Team-level. Monthly review cycle._
EOF

  # dept README.md
  cat > "${dept_dir}/README.md" << EOF
# ${UPPER_DEPT} — ${dt} (${dc})

> ${ORG_NAME} | ${cl}

## Governance Index

| ID | Tier | Document | Status |
|----|------|----------|--------|
| STR-${dc} | Strategy | [strategy.md](strategy.md) | draft |
| DOC-${dc} | Doctrine | [doctrine.md](doctrine.md) | draft |
| PRC-${dc} | Procedure | [procedure.md](procedure.md) | draft |
| PLY-${dc} | Playbook | [playbook.md](playbook.md) | draft |

## Amendment Log

| Date | Author | Change | Tier |
|------|--------|--------|------|
| ${ENACTED_DATE} | setup.sh | Initial generation | All |
EOF

done
echo -e "${GREEN}done${RESET}"

# ─── _standard/README.md (master index) ──────────────────────────────────────
echo -ne "  Generating governance master index... "
{
  echo "# ${ORG_NAME} — Governance Index"
  echo ""
  echo "> Praxeology Framework | 4+1 Tier System | v${GOV_VERSION}"
  echo ""
  echo "This document is the master index for all governance artifacts in **${ORG_NAME}**."
  echo ""
  echo "---"
  echo ""
  echo "## How to Read This System"
  echo ""
  echo "Governance tiers cascade downward. Higher tiers take precedence over lower ones."
  echo "A Procedure cannot contradict its Doctrine. A Playbook cannot contradict its Procedure."
  echo ""
  echo '```'
  echo "Tier 1 STRATEGY  — WHY we exist (founding-level, rarely changes)"
  echo "Tier 2 DOCTRINE  — WHAT we will/will not do (board-level, changes with major pivots)"
  echo "Tier 3 PROCEDURE — HOW we allocate resources (executive-level, quarterly review)"
  echo "Tier 4 PLAYBOOK  — PATTERNS we repeat (team-level, monthly review)"
  echo "Exec   WORK PLAN — NOW what we are doing (individual, daily/weekly)"
  echo '```'
  echo ""
  echo "---"
  echo ""
  echo "## Department Index"
  echo ""
  for dept in "${ENABLED_DEPTS[@]}"; do
    dt=$(dept_title "$dept")
    dc=$(dept_code_range "$dept")
    cl=$(dept_clevel "$dept")
    UPPER_DEPT="${dept^^}"
    echo "### ${UPPER_DEPT} — ${dt} (${dc})"
    echo ""
    echo "| ID | Tier | Document | Status |"
    echo "|----|------|----------|--------|"
    echo "| STR-${dc} | Strategy | [${dept}/strategy.md](${dept}/strategy.md) | draft |"
    echo "| DOC-${dc} | Doctrine | [${dept}/doctrine.md](${dept}/doctrine.md) | draft |"
    echo "| PRC-${dc} | Procedure | [${dept}/procedure.md](${dept}/procedure.md) | draft |"
    echo "| PLY-${dc} | Playbook | [${dept}/playbook.md](${dept}/playbook.md) | draft |"
    echo ""
    echo "See: [${dept}/README.md](${dept}/README.md)"
    echo ""
    echo "---"
    echo ""
  done
  echo "## Amendment Log"
  echo ""
  echo "| Date | Author | Change | Tier Affected |"
  echo "|------|--------|--------|---------------|"
  echo "| ${ENACTED_DATE} | setup.sh | Initial setup | All |"
} > "${TARGET_DIR}/_standard/README.md"
echo -e "${GREEN}done${RESET}"

# ─── _crew/CLAUDE.md (shared crew rules) ────────────────────────────────────
echo -ne "  Generating crew shared rules... "
cat > "${TARGET_DIR}/_crew/CLAUDE.md" << EOF
# ${ORG_NAME} — Crew Rules

> Praxeology Framework | Shared Crew Context | v${GOV_VERSION}

These rules apply to ALL agents operating within **${ORG_NAME}**.

---

## Cascade Principle

Tier 1 (Strategy) always overrides Tier 2 (Doctrine).
Tier 2 always overrides Tier 3 (Procedure).
Tier 3 always overrides Tier 4 (Playbook).
No lower-tier document may contradict a higher-tier document.

## Communication Standards

- Respond in ${LANG_PREF} unless the task explicitly requires another language.
- Be direct and accurate. Do not pad responses.
- Cite the relevant governance document when making rule-based decisions.

## Escalation Protocol

If a situation is not covered by existing governance, escalate to the relevant C-level before acting.

## SafetyGate

The following are hard limits that no agent may override under any circumstances:

1. Do not act outside your assigned department scope without explicit authorization.
2. Do not modify Tier 1 or Tier 2 documents without formal ratification.
3. Do not share _setting/access.json or .env contents with any external party.

---

_See _standard/README.md for full governance index._
EOF
echo -e "${GREEN}done${RESET}"

# ─── Per-agent crew files ────────────────────────────────────────────────────
if [ "${#AGENT_NAMES[@]}" -gt 0 ]; then
  echo -ne "  Generating agent files (${#AGENT_NAMES[@]})... "
  for i in "${!AGENT_NAMES[@]}"; do
    aname="${AGENT_NAMES[$i]}"
    adept="${AGENT_DEPTS[$i]}"
    arole="${AGENT_ROLES[$i]}"
    dt=$(dept_title "$adept")
    cl=$(dept_clevel "$adept")
    UPPER_DEPT="${adept^^}"

    mkdir -p "${TARGET_DIR}/_crew/${aname}"
    cat > "${TARGET_DIR}/_crew/${aname}/CLAUDE.md" << EOF
# ${aname} — Agent Context

> ${ORG_NAME} | ${arole} | ${UPPER_DEPT} (${dt}) | v${GOV_VERSION}

## Identity

- **Name**: ${aname}
- **Role**: ${arole}
- **Department**: ${UPPER_DEPT} — ${dt}
- **Reports to**: ${cl}

## Authority

- Read access: all governance documents
- Write access: _project/, own work plan
- Proposal rights: yes (via Proposal process)
- Amendment rights: no (escalate to ${cl})

## Primary Responsibilities

1. [Define primary responsibility]
2. [Define secondary responsibility]
3. [Define tertiary responsibility]

## Governance References

- Department strategy: [_standard/${adept}/strategy.md](../_standard/${adept}/strategy.md)
- Department doctrine: [_standard/${adept}/doctrine.md](../_standard/${adept}/doctrine.md)
- Department procedure: [_standard/${adept}/procedure.md](../_standard/${adept}/procedure.md)
- Department playbook: [_standard/${adept}/playbook.md](../_standard/${adept}/playbook.md)
- Crew rules: [_crew/CLAUDE.md](../CLAUDE.md)

---

_Higher-tier documents always override this file._
EOF

    cat > "${TARGET_DIR}/_crew/${aname}/sop.md" << EOF
# ${aname} — Standard Operating Procedures

> ${ORG_NAME} | ${arole} | ${UPPER_DEPT} | v${GOV_VERSION}

## Daily Routine

1. Review active work plan
2. Check for new assignments or escalations
3. Execute tasks in priority order
4. Log outcomes and blockers

## Task Handling

1. Receive task or identify task from work plan
2. Check relevant governance tier (Procedure → Playbook)
3. Execute
4. Report outcome

## Escalation

- Block or ambiguity → escalate to ${cl}
- Governance conflict → cite both documents, escalate
- SafetyGate trigger → halt and report immediately

---

_SOPs may not contradict department Procedure (Tier 3)._
EOF

  done
  echo -e "${GREEN}done${RESET}"
fi

# ─── Projects ────────────────────────────────────────────────────────────────
if [ "${#PROJECTS[@]}" -gt 0 ]; then
  echo -ne "  Creating project directories... "
  for proj in "${PROJECTS[@]}"; do
    proj_slug="${proj// /-}"
    proj_slug="${proj_slug,,}"
    mkdir -p "${TARGET_DIR}/_project/${proj_slug}"
    cat > "${TARGET_DIR}/_project/${proj_slug}/README.md" << EOF
# Project: ${proj}

> ${ORG_NAME} | Registered ${ENACTED_DATE}

## Objective

[Describe the project objective.]

## Owner

[Department / Agent]

## Status

draft

## Governance Reference

[Link to relevant department governance documents.]
EOF
  done
  echo -e "${GREEN}done${RESET}"
fi

# ─── _setting/ ───────────────────────────────────────────────────────────────
echo -ne "  Generating settings... "
cat > "${TARGET_DIR}/_setting/permissions.md" << EOF
# Permissions & Access Control

> ${ORG_NAME} | v${GOV_VERSION} | ${ENACTED_DATE}

## Access Matrix

| Role | _standard/ | _crew/ | _project/ | _setting/ |
|------|-----------|--------|-----------|-----------|
| C-Level | read/write | read/write | read/write | read/write |
| Agent | read | read (own) | read/write | read |
| External | — | — | read (shared) | — |

## SafetyGate Rules

1. _setting/access.json — never expose to external parties
2. .env files — never commit to version control
3. Tier 1 documents — require C-level + ratification to amend

## Audit Log

| Date | Actor | Action | Resource |
|------|-------|--------|----------|
| ${ENACTED_DATE} | setup.sh | Initial setup | All |
EOF

cat > "${TARGET_DIR}/_setting/integrations.md" << EOF
# Integrations

> ${ORG_NAME} | v${GOV_VERSION} | ${ENACTED_DATE}

## Configured Integrations

EOF

if [ "$TELEGRAM_ENABLED" = true ]; then
  cat >> "${TARGET_DIR}/_setting/integrations.md" << EOF
### Telegram

- Bot token: configured (see .env)
- Chat ID: ${TG_CHAT_ID:-not set}
- Status: enabled

EOF
fi

cat >> "${TARGET_DIR}/_setting/integrations.md" << EOF
## Adding New Integrations

1. Add credentials to .env (never commit)
2. Document integration here
3. Update permissions.md if new access is required
4. Notify relevant C-level
EOF
echo -e "${GREEN}done${RESET}"

# ─── .env template ───────────────────────────────────────────────────────────
echo -ne "  Generating .env.example... "
{
  echo "# ${ORG_NAME} — Environment Variables"
  echo "# Copy to .env and fill in values. Never commit .env."
  echo ""
  echo "ORG_NAME=\"${ORG_NAME}\""
  echo "GOV_VERSION=\"${GOV_VERSION}\""
  echo ""
  if [ "$TELEGRAM_ENABLED" = true ]; then
    echo "TELEGRAM_BOT_TOKEN=\"your-bot-token\""
    echo "TELEGRAM_CHAT_ID=\"your-chat-id\""
    echo ""
  fi
  echo "# Add additional secrets below"
} > "${TARGET_DIR}/.env.example"
echo -e "${GREEN}done${RESET}"

# ─── Root CLAUDE.md ──────────────────────────────────────────────────────────
echo -ne "  Generating root CLAUDE.md... "
{
  echo "# ${ORG_NAME} — Governance System"
  echo ""
  echo "> Praxeology Framework | Version ${GOV_VERSION} | Enacted ${ENACTED_DATE}"
  echo ""
  echo "You are operating within **${ORG_NAME}**, a ${ORG_TYPE} governed by the Praxeology Framework."
  echo ""
  echo "---"
  echo ""
  echo "## Identity"
  echo ""
  echo "- **Organization**: ${ORG_NAME}"
  echo "- **Mission**: ${ORG_MISSION}"
  echo "- **Type**: ${ORG_TYPE}"
  echo "- **Governance Version**: ${GOV_VERSION}"
  echo ""
  echo "---"
  echo ""
  echo "## Framework Overview"
  echo ""
  echo "This organization uses the universal 4+1 tier governance system:"
  echo ""
  echo "| Tier | Name | Question | Authority |"
  echo "|------|------|----------|-----------|"
  echo "| 1 | Strategy | WHY | Founding-level |"
  echo "| 2 | Doctrine | WHAT | Board-level |"
  echo "| 3 | Procedure | HOW | Executive-level |"
  echo "| 4 | Playbook | PATTERNS | Team-level |"
  echo "| Exec | Work Plan | NOW | Individual-level |"
  echo ""
  echo "---"
  echo ""
  echo "## Department Structure"
  echo ""
  echo "| Code | Department | Role | Domain |"
  echo "|------|-----------|------|--------|"
  for dept in "${ENABLED_DEPTS[@]}"; do
    dt=$(dept_title "$dept")
    dc=$(dept_code_range "$dept")
    cl=$(dept_clevel "$dept")
    UPPER_DEPT="${dept^^}"
    echo "| ${dc} | ${UPPER_DEPT} | ${cl} | ${dt} |"
  done
  echo ""
  echo "---"
  echo ""
  echo "## Core Directives"
  echo ""
  echo "1. Higher-tier governance documents always override lower-tier documents."
  echo "2. Do not act outside your assigned department scope without explicit authorization."
  echo "3. Escalate unresolved governance conflicts to the relevant C-level."
  echo ""
  echo "---"
  echo ""
  echo "## Governance Index"
  echo ""
  echo "Full governance documents: [\`_standard/README.md\`](_standard/README.md)"
  echo "Crew rules: [\`_crew/CLAUDE.md\`](_crew/CLAUDE.md)"
  if [ "${#AGENT_NAMES[@]}" -gt 0 ]; then
    echo ""
    echo "Agent contexts:"
    for aname in "${AGENT_NAMES[@]}"; do
      echo "- [\`_crew/${aname}/CLAUDE.md\`](_crew/${aname}/CLAUDE.md)"
    done
  fi
  echo ""
  echo "---"
  echo ""
  echo "## Active Focus"
  echo ""
  echo "Current focus: [Update with current priorities]"
  echo "Active cycle: ${ENACTED_DATE}"
} > "${TARGET_DIR}/CLAUDE.md"
echo -e "${GREEN}done${RESET}"

# ─── launch.sh ───────────────────────────────────────────────────────────────
echo -ne "  Generating launch.sh... "
cat > "${TARGET_DIR}/launch.sh" << 'LAUNCH_EOF'
#!/usr/bin/env bash
# =============================================================================
# Launch Script — Daily governance system startup
# =============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_FILE="${SCRIPT_DIR}/CLAUDE.md"
STANDARD_INDEX="${SCRIPT_DIR}/_standard/README.md"

echo ""
echo "======================================================"
echo "  Governance System — $(date +%Y-%m-%d)"
echo "======================================================"
echo ""

# Load .env if present
if [ -f "${SCRIPT_DIR}/.env" ]; then
  set -a
  # shellcheck disable=SC1090
  source "${SCRIPT_DIR}/.env"
  set +a
  echo "  .env loaded"
fi

echo "  Root context : ${CLAUDE_FILE}"
echo "  Governance   : ${STANDARD_INDEX}"
echo ""
echo "  Active departments:"
for dir in "${SCRIPT_DIR}/_standard"/*/; do
  if [ -d "$dir" ]; then
    dept=$(basename "$dir")
    echo "    - ${dept}"
  fi
done

echo ""
echo "  Active agents:"
for dir in "${SCRIPT_DIR}/_crew"/*/; do
  if [ -d "$dir" ]; then
    agent=$(basename "$dir")
    echo "    - ${agent}"
  fi
done

echo ""
echo "  Active projects:"
for dir in "${SCRIPT_DIR}/_project"/*/; do
  if [ -d "$dir" ]; then
    proj=$(basename "$dir")
    echo "    - ${proj}"
  fi
done

echo ""
echo "======================================================"
echo "  Ready. Pass CLAUDE.md to your AI agent to begin."
echo "======================================================"
echo ""
LAUNCH_EOF
chmod +x "${TARGET_DIR}/launch.sh"
echo -e "${GREEN}done${RESET}"

# ─── .gitignore ──────────────────────────────────────────────────────────────
echo -ne "  Generating .gitignore... "
cat > "${TARGET_DIR}/.gitignore" << 'EOF'
# Environment & secrets
.env
_setting/access.json

# OS
.DS_Store
Thumbs.db

# OMC / Claude Code
.omc/

# Local overrides
*.local.*

# Reports & archives
reports/

# Dependencies
node_modules/

# Build output
dist/
build/
EOF
echo -e "${GREEN}done${RESET}"

# ─── docs/concepts.md ────────────────────────────────────────────────────────
echo -ne "  Generating docs... "
mkdir -p "${TARGET_DIR}/docs"
cat > "${TARGET_DIR}/docs/concepts.md" << EOF
# Core Concepts

> Praxeology Framework | Conceptual Reference

## The 4+1 Tier Model

All purposeful action follows the same structural pattern:

| Tier | Name | Question | Scope | Change Frequency |
|------|------|----------|-------|-----------------|
| 1 | Strategy | WHY | Founding | Years |
| 2 | Doctrine | WHAT | Board | Major pivots |
| 3 | Procedure | HOW | Executive | Quarterly |
| 4 | Playbook | PATTERNS | Team | Monthly |
| Exec | Work Plan | NOW | Individual | Daily/Weekly |

## Cascade Rule

Higher tiers always override lower tiers. This is unconditional.

A Procedure that contradicts its parent Doctrine is invalid and must be amended.
A Playbook that contradicts its parent Procedure is invalid and must be amended.

## SafetyGate

A SafetyGate is a hard limit declared in Tier 1 or Tier 2 that no lower-tier document may override. SafetyGates are marked explicitly in governance documents.

## Proposal Process

Any member may propose an amendment to any tier document by submitting a Proposal:
1. Identify the document and tier
2. State the proposed change and rationale
3. Submit to the relevant C-level for review
4. C-level approves, rejects, or escalates to full ratification
5. Approved changes are enacted with a version bump

## Review Cascade

When a Tier N document changes, all Tier N+1 documents under it are flagged for review. This ensures consistency propagates downward.

## Reverse Flow

When a Tier N document is reviewed, it may surface a need to amend Tier N-1. This is the reverse flow — it propagates upward only as a recommendation, not an override.
EOF
echo -e "${GREEN}done${RESET}"

# =============================================================================
# DONE
# =============================================================================
echo ""
echo -e "${GREEN}${BOLD}======================================================"
echo -e "  Governance system generated successfully."
echo -e "======================================================${RESET}"
echo ""
echo -e "  Location: ${CYAN}${TARGET_DIR}${RESET}"
echo ""
echo -e "  Next steps:"
echo -e ""
echo -e "  1. ${BOLD}Review and customize governance documents:${RESET}"
echo -e "     ${DIM}${TARGET_DIR}/_standard/${RESET}"
echo -e ""
echo -e "  2. ${BOLD}Set up your environment:${RESET}"
echo -e "     ${DIM}cp ${TARGET_DIR}/.env.example ${TARGET_DIR}/.env${RESET}"
echo -e "     ${DIM}# then edit .env with your values${RESET}"
echo -e ""
echo -e "  3. ${BOLD}Launch the governance system:${RESET}"
echo -e "     ${DIM}bash ${TARGET_DIR}/launch.sh${RESET}"
echo -e ""
echo -e "  4. ${BOLD}Pass CLAUDE.md to your AI agent:${RESET}"
echo -e "     ${DIM}${TARGET_DIR}/CLAUDE.md${RESET}"
echo ""
echo -e "  ${DIM}Built with Praxeology by NeoMakes — https://neomakes.com${RESET}"
echo ""
