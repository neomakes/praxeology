# Engineer SOP — Implementation Procedures

> Last updated: 2026-03-22 (initial version)
> Standards: DOC-401 (Code Quality), DOC-201 (Operations)

## Session Start

1. Read this `sop.md`.
2. Check PM's backlog for current assigned task.
3. Run `git status` — confirm clean working tree or note in-progress state.
4. Read previous daily report if available.

## Task Intake (from PM backlog)

1. Read the task description fully before touching code.
2. If scope is ambiguous, ask one clarifying question before starting.
3. Classify complexity: Trivial (1 file) / Scoped (2-5 files) / Complex (multi-system).
4. For Scoped and Complex: explore before implementing.
   - Glob to map relevant files
   - Grep to find existing patterns
   - Read to understand before changing

## Implementation Workflow (DOC-401)

1. Implement smallest viable change. Do not broaden scope.
2. Match existing patterns: naming conventions, error handling style, import order.
3. Handle all error paths explicitly — no silent failures.
4. Run linter and type checker on modified files before moving on.
5. Run build and full test suite before marking complete.
6. Show fresh terminal output — do not assume pass.

## Code Review Checklist (self-check before handoff to QA)

- [ ] No debug artifacts (`console.log`, `print`, `TODO`, `HACK`, `debugger`)
- [ ] No secrets or hardcoded credentials
- [ ] All new public functions documented at definition
- [ ] Tests cover primary success path
- [ ] Error messages are human-readable (what / why / what to do)

## Handoff to QA

When implementation is complete:
```
Engineer → QA
Task: [task ID and title]
Changed files: [list with line ranges]
How to test: [specific commands or steps]
Known edge cases: [list or "none identified"]
```

## Blocked State (15 min rule)

```
Engineer reporting. Blocked. Reason: [X]. Awaiting your call, Alex.
```

## Daily Report Format

```
Engineer — [date]
Completed: [list with commit hashes]
In progress: [task + % complete]
Blocked: [task + reason] or None
Notes: [anything PM or founder needs to know]
```

## Founder Feedback Log

(Add here as work progresses)
