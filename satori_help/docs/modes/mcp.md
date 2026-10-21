---
next:
  text: 'Shell'
  link: '/modes/shell'
---

# MCP server

[`satori-mcp`](https://github.com/satorici/satori-mcp) is a local [Model Context Protocol](https://modelcontextprotocol.io) (MCP) server over stdio. AI agents such as Claude Code, Codex, and Cursor can use it to run playbooks, inspect executions, and read findings through your existing Satori credentials. It runs straight from GitHub with `npx` (Node.js 22 or later), so there is nothing to install:

```console
npx -y github:satorici/satori-mcp
```

The server shares credentials with the CLI: it uses the token saved by `satori-v2 config token` (`~/.satori_credentials.yml`), or `SATORI_TOKEN` / `SATORI_PROFILE` from its environment (`SATORI_TOKEN` overrides the credentials file). Configure a token first — see [Installation](/getting-started/install.md) — or pass `SATORI_TOKEN` in the agent config (see [below](#ci-or-no-credentials-file)).

## Configure your agent

Add the server to your agent's MCP config. The agent launches it itself — stdout is the protocol channel, so do not pipe or redirect it. The first start builds the package from GitHub (about 20 seconds); later starts use the npm cache.

### Claude Code

```console
claude mcp add --scope user satori -- npx -y github:satorici/satori-mcp
```

Or write a project `.mcp.json` (and commit it for the team):

```json
{
  "mcpServers": {
    "satori": { "command": "npx", "args": ["-y", "github:satorici/satori-mcp"] }
  }
}
```

### Codex

```console
codex mcp add satori -- npx -y github:satorici/satori-mcp
```

Or add to `~/.codex/config.toml` (or a trusted project's `.codex/config.toml`):

```toml
[mcp_servers.satori]
command = "npx"
args = ["-y", "github:satorici/satori-mcp"]
```

### Cursor

In `.cursor/mcp.json` or global MCP settings:

```json
{
  "mcpServers": {
    "satori": { "command": "npx", "args": ["-y", "github:satorici/satori-mcp"] }
  }
}
```

### CI or no credentials file

In CI, or on machines without the CLI, pass the token in the agent's `env` block.
Cursor, Claude Code (`.mcp.json`), and similar JSON configs:

```json
{
  "mcpServers": {
    "satori": {
      "command": "npx",
      "args": ["-y", "github:satorici/satori-mcp"],
      "env": {
        "SATORI_TOKEN": "YOUR_TOKEN"
      }
    }
  }
}
```

Codex (`~/.codex/config.toml` or a trusted project's `.codex/config.toml`):

```toml
[mcp_servers.satori]
command = "npx"
args = ["-y", "github:satorici/satori-mcp"]

[mcp_servers.satori.env]
SATORI_TOKEN = "YOUR_TOKEN"
```

### Versions and updates

`npx` caches git installs, so a config keeps running the version it first downloaded. Pin a release or commit with `github:satorici/satori-mcp#<tag-or-sha>`, and to pick up the latest `main` clear the cache (`npm cache clean --force`).

## Tools

| Tool | Description |
| --- | --- |
| `whoami` | Active profile, API endpoint, notify email, and whether a GitHub PAT is configured |
| `run_playbook` | Run a playbook on Satori (`playbook_path`, `playbook_yaml` or catalog `playbook_uri`) and optionally wait for the result |
| `run_local` | Run a playbook's commands on this machine, upload the results and return the execution |
| `scan_repository` | Start a scan of a GitHub repository (`owner/repo`, or `owner/*` for every repository of an owner) |
| `get_execution` | Status and assertion summary for an execution (no logs) |
| `get_execution_output` | Capped logs: without `test`, an index of tests; with `test`, the last lines of a stream |
| `get_execution_playbook` | The playbook YAML an execution ran (capped) |
| `list_executions` | Past executions (reports), newest first: filter by `job_id`, `status`, `report_status`, `job_type`, `from_`/`to`, `q`, `visibility`, `severity`, `playbook`, `tags`; paginated, max 25 |
| `list_reports` | Alias of `list_executions` (in Satori, reports = executions) |
| `stop_execution` | Cancel a running execution (no-op if it is not running) |
| `list_jobs` | Jobs, newest first (`type`: RUN, SCAN or MONITOR), to recover a `job_id` |
| `get_job` | A job and its 5 most recent executions |
| `list_scans` | Scan jobs (same as `list_jobs` with `type=SCAN`) |
| `list_monitors` | Monitor jobs with their schedule `expression` |
| `list_findings` | Findings, filtered by `execution_id`, severity (0-5 or names), `status`, `source` (ASSERT or TOOL) |
| `get_finding` | Details of one finding plus its recent timeline |
| `get_finding_timeline` | Status changes and comments for a finding |
| `update_finding_status` | Triage a finding (OPEN, INVESTIGATING, TP, FIXED, FP, ACCEPTED), optionally with a comment |
| `add_finding_comment` | Comment on a finding without changing its status |
| `list_advisories` | External issues and security advisories already created from findings |
| `list_playbooks` | Search the catalog of ready-made `satori://` playbooks |
| `get_playbook` | Details and YAML of a catalog playbook |
| `list_repos` | Repositories Satori can target, with their last execution |
| `recommend_playbook` | Inspect a repo and propose a lint/format/types/unit/security playbook for `.satori-llm.yml` (CI `.satori.yml` should import it) |

All responses are size-capped. Prefer `get_execution_output` with a `test` filter (for example `cmd.0`) instead of requesting full logs. Tools that change shared state (`update_finding_status`, `add_finding_comment`) are meant to be used only when you ask for them.

### `run_playbook` notes

Provide exactly one of `playbook_path` (local `.yml` / `.yaml` file), `playbook_yaml` (inline YAML) or `playbook_uri` (a catalog playbook such as `satori://code/python/pyspector_v2.yml`, see `list_playbooks`). Optional `repository` is an `owner/repo` from `list_repos`. With `wait` (default true), the tool polls until the job finishes or `wait_seconds` elapses (max 600); then call `get_execution` with the returned `execution_id`.

### `run_local` notes

`run_local` executes the playbook's commands on the machine running the MCP server, with your user's privileges, and uploads the results to Satori, so the agent should only run playbooks you asked for or that it wrote for you. The working directory is `directory` (an existing local directory), or `repository` (`owner/repo`, shallow-cloned to a temporary directory), defaulting to the server's working directory. `run` limits execution to test paths with those prefixes, and `timeout_seconds` (default 300, max 3600) cancels the run when it elapses. It returns the same shape as `run_playbook`; read logs with `get_execution_output` and findings with `list_findings`.

### `recommend_playbook` notes

Pass `directory` (default: the server's working directory). Supported stacks: Python, JS/TS, Go, Java, C#, Rust, Ruby, PHP, Swift, C/C++ (CMake) and Solidity (Foundry). Quality checks go in **`.satori-llm.yml`**; **`.satori.yml`** is reserved for CI/manual runs and should import the LLM file:

```yaml
import:
  - file://.satori-llm.yml
```

A new repo gets `playbook_yaml` (write to `.satori-llm.yml`) plus `ci_playbook_yaml` (thin importer for `.satori.yml`) and a `checks` list explaining each check. If `.satori-llm.yml` already exists, you get `changes` (missing or different checks with `suggested_yaml`) to merge by hand. If only a hand-written CI `.satori.yml` exists, you still get a full LLM playbook plus `needs_ci_import` / `ci_import_yaml` — add the import without overwriting CI checks. A legacy `.satori.yml` that already has `# satori:recommended` is treated as migrate-from-CI: merge into `.satori-llm.yml` and leave CI as the importer.

Checks for tools the repo already configures are blocking (`assertReturnCode: 0`); the rest are informational.

Only what the repo cannot settle comes back in `questions` (for example formatter, dead-code detection). Ask the user, then call again with `prefs`, e.g. `{"formatter": "black", "dead_code": false}`. Answers are stored in the first line of `.satori-llm.yml`, `# satori:recommended v2 python/uv prefs: formatter=black`, so later updates only ask about checks added since.

Suggested loop: write `.satori-llm.yml` (and the CI importer if needed) with the user's approval, `run_local` with `playbook_path=.satori-llm.yml` once as a baseline before editing code, and after each change fix only the failures that were not in the baseline. Prefer `.satori-llm.yml` over a heavy CI `.satori.yml` for that baseline.

The flow looks like this — an AI that only writes unit tests can miss type and security gaps outside the tested area; `recommend_playbook` builds a multi-lane playbook and closes the loop:

![AI asked for unit tests vs. AI powered by Satori](/playbook_generator.svg)

## Optional: keep agents on the full playbook

MCP server `instructions` are soft guidance. Agents often fall back to a familiar shell command (`pytest`, `npm test`, and similar) and skip lint, format, types, and security from `.satori-llm.yml`. Connecting the Satori MCP server is enough for many workflows; use the patterns below only if you want stronger, project-level pressure to verify through Satori.

Prerequisite: a committed `.satori-llm.yml` (create or refresh it with `recommend_playbook`). Prefer verifying with `run_local` on that file — baseline once before edits, then fix only failures that were not in the baseline.

### Cursor

Add `.cursor/rules/satori-verify.mdc`:

````markdown
---
description: Verify code changes with Satori MCP, not shell-only unit tests
alwaysApply: true
---

# Satori verification

After editing code, verify with the **satori** MCP server:

1. If `.satori-llm.yml` is missing, call `recommend_playbook` and write the playbook only with the user's approval.
2. Before the first edit in a session, call `run_local` with `playbook_path=.satori-llm.yml` as a baseline.
3. After changes, call `run_local` again and fix only failures that were not in the baseline.
4. Do not treat shell unit tests (`pytest`, `npm test`, `pnpm test:unit`, and similar) as sufficient verification on their own.
````

### Claude Code

Add a short block to `CLAUDE.md` (or project instructions):

```markdown
## Satori verification

After editing code, verify with the satori MCP tools — not shell-only unit tests.
If `.satori-llm.yml` is missing, call `recommend_playbook` (write files only with approval).
Baseline with `run_local` on `.satori-llm.yml` before edits; after changes, fix only
failures that were not in the baseline. Do not treat `pytest` / `npm test` alone as enough.
```

### Codex

Add the same guidance to `AGENTS.md` (or project instructions):

```markdown
## Satori verification

After editing code, verify with the satori MCP tools — not shell-only unit tests.
If `.satori-llm.yml` is missing, call `recommend_playbook` (write files only with approval).
Baseline with `run_local` on `.satori-llm.yml` before edits; after changes, fix only
failures that were not in the baseline. Do not treat `pytest` / `npm test` alone as enough.
```

### Session prompt (no committed rule)

Paste into a chat when you want the behavior for one session only:

```text
Verify with Satori MCP run_local on .satori-llm.yml; do not rely on shell unit tests alone.
```

## Playbook docs as resources

The server exposes playbook reference pages as MCP resources (fetched from `https://docs-v2.satori.ci`, override with `SATORI_DOCS_URL`):

| Resource URI | Content |
| --- | --- |
| `satori-docs://playbooks/language` | Playbook language |
| `satori-docs://playbooks/asserts` | Asserts |
| `satori-docs://playbooks/inputs` | Inputs |
| `satori-docs://playbooks/settings` | Settings |
| `satori-docs://playbooks/execution` | Execution |
| `satori-docs://playbooks/tool-output` | Prefer JSON tool stdout for `TOOL` findings |

Agents should read `satori-docs://playbooks/language` before writing or running a playbook. When the playbook runs a security/analysis tool, also read `satori-docs://playbooks/tool-output` and prefer that tool’s JSON flags.

## Prompt

`write_and_run_playbook` guides the agent to read the language docs (and tool-output when using scan tools), write YAML with preferred JSON tool flags, call `run_playbook`, then summarize with `get_execution` / `get_execution_output` / `list_findings` and include the `report_url`.

## Errors

Auth and API failures return small error objects instead of crashing the protocol. If you are not logged in, the response points you to `satori-v2 config token <token>`; alternatively set `SATORI_TOKEN` in the server's environment. A `403` includes a hint that the action may need a PRO or ENTERPRISE plan.

---

If you need any help, please reach out to us on [Discord](https://discord.gg/NJHQ4MwYtt) or via [Email](mailto:support@satori.ci)
