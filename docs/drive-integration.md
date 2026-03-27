# Google Drive Integration

This guide explains how to connect Praxeology to Google Drive as a shared document store. The pattern is based on NeoMakes' production setup and requires no third-party sync tooling — a single symlink bridges your local workspace to Drive.

---

## How It Works

Google Drive's desktop client mounts the drive as a local filesystem path. A symlink at `_drive/` inside your workspace points to that mount. Agents treat `_drive/` as a regular directory — reads and writes go directly to Drive with no intermediary.

```
workspace/
├── _crew/          ← local agent configs (authoritative)
├── _drive/         ← symlink → Google Drive mount
│   └── My Drive/
│       ├── system/
│       ├── projects/
│       └── company/
└── ...
```

---

## Prerequisites

- **Google Drive for Desktop** installed and signed in
  - macOS default mount: `/Users/{username}/Library/CloudStorage/GoogleDrive-{email}/`
  - Verify: `ls "$HOME/Library/CloudStorage/"` should show a `GoogleDrive-*` directory
- Drive client must be running whenever agents access `_drive/`

---

## Symlink Setup

Run once from your workspace root:

```bash
# macOS — adjust email and workspace path
ln -s "/Users/neo/Library/CloudStorage/GoogleDrive-neo@neomakes.com/My Drive" _drive
```

Verify:

```bash
ls _drive/
# should list your Drive root contents
```

Add to `.gitignore` so the symlink is not committed:

```
_drive/
```

> **Note**: The symlink target path includes the Google account email. If you rotate accounts or share the workspace setup script with others, parameterize the email:
> ```bash
> GDRIVE_EMAIL="your@email.com"
> ln -s "$HOME/Library/CloudStorage/GoogleDrive-${GDRIVE_EMAIL}/My Drive" _drive
> ```

---

## Directory Structure

All Praxeology-managed content lives under `_drive/My Drive/system/`. Projects and corporate documents live at sibling paths.

```
_drive/My Drive/
├── system/
│   ├── praxeology/          ← regulation files, one folder per department
│   │   ├── ceo/
│   │   ├── coo/
│   │   ├── cfo/
│   │   ├── cto/
│   │   ├── cdo/
│   │   ├── chro/
│   │   └── ciso/
│   ├── crew/                ← per-agent sync directories
│   │   ├── zoro/
│   │   ├── nami/
│   │   ├── usopp/
│   │   └── ...
│   └── room/                ← channel-based workspaces
│       ├── lounge/
│       ├── bridge/
│       ├── engine-room/
│       └── comms/
├── projects/                ← per-project documents and artifacts
│   ├── neoroger/
│   ├── neocog/
│   └── ...
└── company/                 ← corporate entity documents
    ├── incorporation/
    ├── governance/
    ├── equity/
    └── tax/
```

---

## system/praxeology/ — Regulation Files

Each department folder contains regulation files organized by tier. The naming convention is `{TIER}-{NNN}.md`.

```
system/praxeology/
├── ceo/
│   ├── STR-101.md           ← Strategy
│   ├── DOC-101.md           ← Doctrine
│   ├── DOC-102.md
│   ├── PRC-101.md           ← Procedure
│   └── PLY-101.md           ← Playbook
├── coo/
│   ├── STR-201.md
│   ├── DOC-201.md
│   ├── PRC-201.md
│   ├── PRC-202.md
│   ├── PLY-201.md
│   ├── PLY-202.md
│   └── PLY-203.md
├── cfo/
│   ├── STR-301.md
│   ├── DOC-301.md
│   └── PLY-301.md
├── cto/
│   └── ...                  ← 4xx series
├── cdo/
│   └── ...                  ← 5xx series
├── chro/
│   └── ...                  ← 6xx series
└── ciso/
    └── ...                  ← 7xx series
```

**Tier prefixes and numbering**:

| Prefix | Tier      | Authority to modify      |
|--------|-----------|--------------------------|
| STR    | Strategy  | Principal only           |
| DOC    | Doctrine  | Principal only           |
| PRC    | Procedure | Proposal → Principal     |
| PLY    | Playbook  | Proposal → Department    |

**Numbering series**: `{department-code}{01–99}`. CEO = 1xx, COO = 2xx, CFO = 3xx, CTO = 4xx, CDO = 5xx, CHRO = 6xx, CISO = 7xx.

Agents read regulation files by path. Example reference in `CLAUDE.md`:

```markdown
## Standard References
- Primary: `_drive/My Drive/system/praxeology/coo/` (2xx procedures)
- Safety: `_drive/My Drive/system/praxeology/ceo/DOC-102.md`
```

---

## system/crew/ — Per-Agent Sync Directories

Each agent has a subdirectory under `system/crew/` for documents that need to persist across sessions or be visible to other agents.

```
system/crew/
├── zoro/
│   ├── reports/             ← daily reports (YYYY-MM-DD.md)
│   ├── sop.md               ← agent's current standard operating procedures
│   ├── todo.json            ← daily task list
│   └── weekly.json          ← weekly work plan
├── nami/
│   └── ...
└── usopp/
    └── ...
```

**What goes here vs. `_crew/`**:

| Location | Content | Authoritative? |
|----------|---------|---------------|
| `_crew/{agent}/` | CLAUDE.md, persona, identity config | Yes — source of truth |
| `_drive/.../crew/{agent}/` | reports, sop, todo, weekly plans | Yes — shared/persistent |

The `sop.md` in Drive is the live, evolved version of each agent's procedures. The persona and identity in `_crew/` are fixed governance. When an agent updates its SOP (via PLY-203 Learn-Compress-Apply), it writes to the Drive path, not to `_crew/`.

---

## system/room/ — Channel Workspaces

Rooms map to communication channels. Each room holds thread-organized working documents.

```
system/room/
├── lounge/                  ← general coordination, async updates
│   └── threads/
├── bridge/                  ← principal-facing ops, decisions, escalations
│   └── threads/
├── engine-room/             ← technical execution, builds, deployments
│   └── threads/
└── comms/                   ← external communications drafts and logs
    └── threads/
```

Agents write working documents (drafts, analysis outputs, meeting notes) into the relevant room. The room structure mirrors Discord/Telegram channel layout so agents can reference shared context by channel name.

---

## projects/ — Per-Project Storage

```
projects/
└── neoroger/
    ├── docs/                ← specifications, PRDs, architecture notes
    ├── research/            ← research outputs, benchmarks
    └── assets/              ← designs, media, exports
```

Create a subdirectory per project using the project's canonical slug. Agents with RW project access write outputs here. Agents with R access read only.

---

## company/ — Corporate Entity Documents

```
company/
├── incorporation/           ← articles, registration certificates
├── governance/              ← board resolutions, operating agreements
├── equity/                  ← cap table, option agreements
└── tax/                     ← filings, receipts, correspondence
```

This is read-only for all agents. Only the principal modifies corporate documents. Agents referencing legal or financial details read from here.

---

## Naming Conventions

| Item | Convention | Example |
|------|-----------|---------|
| Directory names | English, lowercase, hyphen-separated | `engine-room/`, `praxeology/` |
| Regulation files | `{TIER}-{NNN}.md` uppercase prefix | `DOC-201.md`, `PLY-301.md` |
| Daily reports | `YYYY-MM-DD.md` | `2026-03-26.md` |
| Project slugs | lowercase, hyphen-separated | `neoroger/`, `neocog/` |
| Thread documents | descriptive, hyphen-separated | `weekly-sync-2026-W13.md` |

Do not use spaces in any path under `_drive/My Drive/system/`. Paths with spaces require quoting in every shell command and break naive agent file references.

---

## Sync Strategy

**`_crew/` is authoritative for agent identity and governance loading.** These files are version-controlled in git and define what an agent *is*.

**Drive is authoritative for shared operational state.** Reports, SOPs, work plans, research outputs, and project documents live in Drive because they need to be visible across agents and persist independently of any single agent's working directory.

```
_crew/{agent}/CLAUDE.md     ← identity, persona, authority tier (git)
_crew/{agent}/.env          ← secrets (git-ignored, local only)
_drive/.../crew/{agent}/sop.md       ← evolved procedures (Drive)
_drive/.../crew/{agent}/reports/     ← daily reports (Drive)
_drive/.../crew/{agent}/weekly.json  ← work plans (Drive)
```

**Conflict resolution rule**: If `_crew/` and Drive disagree about governance (CLAUDE.md content vs. sop.md procedures), `_crew/` wins for identity-level rules and Drive's `sop.md` wins for operational procedures. The two files cover different concerns and should not overlap.

---

## Access Control

Drive permissions mirror project access defined in each agent's `CLAUDE.md`:

| Access | Meaning |
|--------|---------|
| RW | Agent reads and writes to this project's Drive folder |
| R | Agent reads only; no writes |

Enforce this through CLAUDE.md `Boundaries` sections, not Drive folder permissions (which cannot be set per-agent when all agents run as the same OS user).

---

## Verifying the Setup

```bash
# Symlink resolves
ls _drive/

# Praxeology folder accessible
ls "_drive/My Drive/system/praxeology/"

# Regulation file readable
cat "_drive/My Drive/system/praxeology/coo/DOC-201.md"

# Agent crew directory exists
ls "_drive/My Drive/system/crew/zoro/"
```

If `_drive/` returns "No such file or directory", Google Drive for Desktop is not running or the mount path differs. Check:

```bash
ls "$HOME/Library/CloudStorage/"
# Adjust the symlink target to match the actual path shown
```
