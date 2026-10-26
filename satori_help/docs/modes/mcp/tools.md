---
prev:
  text: 'Setup'
  link: '/modes/mcp/setup'
next:
  text: 'Agent rules'
  link: '/modes/mcp/agent-rules'
---

# Tools

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
| `get_finding_ai_analysis` | Latest AI analysis for a finding (PENDING, COMPLETED or FAILED); 404 if none yet |
| `analyze_finding` | Queue AI analysis for one finding (account AI key; only when asked); optional `wait` |
| `analyze_execution` | Queue AI analysis for an execution's findings in one call (max 20); optional `finding_ids` / `wait` |
| `list_advisories` | External issues and security advisories already created from findings (optional `finding_id` / `execution_id`) |
| `get_advisory` | Details of one advisory (description capped) with `advisory_url` |
| `create_security_advisory` | Create a local security-advisory draft from a finding (PRO; only when asked); does not contact GitHub |
| `publish_security_advisory` | Publish an existing draft to GitHub by `finding_id` (needs GitHub PAT; only when asked) |
| `get_advisory_status` | Live remote GitHub advisory status for an `advisory_id` |
| `update_advisory_visibility` | Set advisory visibility (`PUBLIC` / `PRIVATE` / `UNLISTED`); only when asked |
| `list_playbooks` | Search the catalog of ready-made `satori://` playbooks |
| `get_playbook` | Details and YAML of a catalog playbook |
| `list_repos` | Repositories Satori can target, with their last execution |
| `recommend_playbook` | Inspect a repo and propose a lint/format/types/unit/security playbook for `.satori-llm.yml` (CI `.satori.yml` should import it) |
| `create_ssh_session` | Start a remote sandbox container (optional cpu/memory/image/regions/`timeout`/`save_files`); waits until READY with a host by default |
| `get_ssh_session` | Status (`PREPARING`, `READY` or `FINISHED`), region, host and settings of an SSH session |
| `list_ssh_sessions` | SSH sessions, newest first (paginated) |
| `exec_in_session` | Run a shell command in a READY session; returns capped stdout/stderr/`return_code` (fresh shell each call) |
| `stop_ssh_session` | Stop a session and release its container (async; poll with `get_ssh_session` until `FINISHED`) |
| `ssh_into_execution` | Short-lived (5 min) SSH credentials for a **RUNNING** execution; MCP cannot host a TTY — give them to the user (`satori-v2 shell <id>`) |

All responses are size-capped. Prefer `get_execution_output` with a `test` filter (for example `cmd.0`) instead of requesting full logs. Tools that change shared state (`update_finding_status`, `add_finding_comment`, `analyze_finding`, `analyze_execution`, `create_security_advisory`, `publish_security_advisory`, `update_advisory_visibility`) are meant to be used only when you ask for them. Always call `stop_ssh_session` when a sandbox is no longer needed.

### AI analysis notes

`analyze_finding` and `analyze_execution` queue analysis on Satori using the **account's configured AI provider and API key** (set in the dashboard Settings); they incur provider cost. With `wait` (default true), the tool polls until each queued row is `COMPLETED` or `FAILED`, or until `wait_seconds` (max 600). Read an existing row with `get_finding_ai_analysis`. `suggested_status` is **advisory only** — the agent must not call `update_finding_status` unless you asked to triage. A `409` usually means no provider or API key is configured.

### Security advisory notes

`create_security_advisory` builds a **local draft** from a finding (title/description/severity derived server-side; completed AI analysis may enrich the text). It requires a PRO or ENTERPRISE plan and does **not** call GitHub. Creating a draft can promote a `PRIVATE` execution to `UNLISTED`. If a draft already exists for that finding, the existing row is returned. `publish_security_advisory` submits that draft to GitHub using the account's GitHub PAT from Settings (`finding_id`, not advisory id). `get_advisory_status` is a live remote lookup. There is no delete tool in MCP.

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

### Remote sandbox (SSH) notes

Agents can open a short-lived remote container, run commands in it, then tear it down. Typical loop:

1. `create_ssh_session` (default `wait` true) — optional `cpu`, `memory`, `storage`, `image`, `os`, `environment_variables`, `regions`, `timeout` (session lifetime in seconds), `save_files`.
2. If the result is still starting (no `host` yet), call `get_ssh_session` until `status` is `READY` and `host` is set. The API may mark a session `READY` briefly before the public host is known; create and `exec_in_session` wait for a host — do not treat a null `host` as runnable.
3. `exec_in_session` with `session_id` and `command` (`timeout` 1–3600 seconds, default 60). Each call is a fresh shell (filesystem persists; env/cwd do not). Output is capped.
4. Always `stop_ssh_session` when done. Stopping is asynchronous; confirm with `get_ssh_session` until `FINISHED`.

Use a sandbox to explore; prefer a playbook once the command line is settled. `run_playbook` is for repeatable cloud runs with asserts and findings; `run_local` runs on the machine hosting the MCP server. For an interactive human shell, see [Shell](/modes/shell).

`ssh_into_execution` is separate: only when the user asks to debug a **RUNNING** execution. It returns `host`, `username` and a password token (about 5 minutes); it does not run commands itself. Have the user connect with `satori-v2 shell <execution_id>`.

**Use cases**

- Try commands and install deps before writing them into a playbook
- Isolated dry-runs of security tools (`trivy`, `semgrep`, `nuclei`, `gitleaks`, and similar) without installing them on the laptop
- Safe triage of samples or CVE reproductions in a throwaway container
- Inspect a hung or failing **RUNNING** execution (`ssh_into_execution`, or CLI `satori-v2 shell EXECUTION-ID`)
- Keep changed files after the session with `save_files` when you need artifacts
