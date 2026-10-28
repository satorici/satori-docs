---
prev:
  text: 'Tools'
  link: '/modes/mcp/tools'
next:
  text: 'Subagents'
  link: '/modes/mcp/subagents'
---

# Optional: keep agents on the full playbook

MCP server `instructions` are soft guidance. Agents often fall back to a familiar shell command (`pytest`, `npm test`, and similar) and skip lint, format, types, and security from `.satori-llm.yml`. Connecting the Satori MCP server is enough for many workflows; use the patterns below only if you want stronger, project-level pressure to verify through Satori.

Prerequisite: a committed `.satori-llm.yml` (create or refresh it with `recommend_playbook`; checks only — install lives on CI `.satori.yml`). Prefer verifying with `run_local` on that file — baseline once before edits, then fix only failures that were not in the baseline. If a check fails because a tool or deps are missing, install on the host and re-run; do not add `install:` to `.satori-llm.yml`.

### Cursor

Add `.cursor/rules/satori-verify.mdc`:

````markdown
---
description: Verify code changes with Satori MCP, not shell-only unit tests
alwaysApply: true
---

# Satori verification

After editing code, verify with the **satori** MCP server:

1. If `.satori-llm.yml` is missing, call `recommend_playbook` and write the playbook only with the user's approval (no `install:` in the LLM file).
2. Before the first edit in a session, call `run_local` with `playbook_path=.satori-llm.yml` as a baseline. If a tool/deps is missing, install on the host and re-run.
3. After changes, call `run_local` again and fix only failures that were not in the baseline.
4. Do not treat shell unit tests (`pytest`, `npm test`, `pnpm test:unit`, and similar) as sufficient verification on their own.
````

### Claude Code

Add a short block to `CLAUDE.md` (or project instructions):

```markdown
## Satori verification

After editing code, verify with the satori MCP tools — not shell-only unit tests.
If `.satori-llm.yml` is missing, call `recommend_playbook` (write files only with approval;
checks only — install belongs on CI `.satori.yml`).
Baseline with `run_local` on `.satori-llm.yml` before edits; if a tool/deps is missing,
install on the host and re-run. After changes, fix only failures that were not in the
baseline. Do not treat `pytest` / `npm test` alone as enough.
```

### Codex

Add the same guidance to `AGENTS.md` (or project instructions):

```markdown
## Satori verification

After editing code, verify with the satori MCP tools — not shell-only unit tests.
If `.satori-llm.yml` is missing, call `recommend_playbook` (write files only with approval;
checks only — install belongs on CI `.satori.yml`).
Baseline with `run_local` on `.satori-llm.yml` before edits; if a tool/deps is missing,
install on the host and re-run. After changes, fix only failures that were not in the
baseline. Do not treat `pytest` / `npm test` alone as enough.
```

### Session prompt (no committed rule)

Paste into a chat when you want the behavior for one session only:

```text
Verify with Satori MCP run_local on .satori-llm.yml; do not rely on shell unit tests alone.
```
