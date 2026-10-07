---
next:
  text: 'Shell'
  link: '/modes/shell'
---

# MCP server

`satori-v2 mcp` starts a local [Model Context Protocol](https://modelcontextprotocol.io) (MCP) server over stdio. AI agents such as Claude Code, Codex, and Cursor can use it to run playbooks, inspect executions, and read findings through your existing Satori credentials.

The server uses the token from `satori-v2 config token` (or `SATORI_TOKEN` / `SATORI_PROFILE`). Configure a token first — see [Installation](/getting-started/install.md).

## Configure your agent

Add the server to your agent's MCP config. The agent launches `satori-v2 mcp` itself — stdout is the protocol channel, so do not pipe or redirect it.

### Claude Code

```console
claude mcp add --scope user satori -- satori-v2 mcp
```

Or write a project `.mcp.json` (and commit it for the team):

```json
{
  "mcpServers": {
    "satori": { "command": "satori-v2", "args": ["mcp"] }
  }
}
```

### Codex

```console
codex mcp add satori -- satori-v2 mcp
```

Or add to `~/.codex/config.toml` (or a trusted project's `.codex/config.toml`):

```toml
[mcp_servers.satori]
command = "satori-v2"
args = ["mcp"]
```

### Cursor

In `.cursor/mcp.json` or global MCP settings:

```json
{
  "mcpServers": {
    "satori": { "command": "satori-v2", "args": ["mcp"] }
  }
}
```

## Tools

| Tool | Description |
| --- | --- |
| `whoami` | Active profile, API endpoint, notify email, and whether a GitHub PAT is configured |
| `run_playbook` | Submit a playbook (`playbook_path` or `playbook_yaml`) and optionally wait for the result |
| `get_execution` | Status and assertion summary for an execution (no logs) |
| `get_execution_output` | Capped logs: without `test`, an index of tests; with `test`, the last lines of a stream |
| `list_findings` | List findings (optional `execution_id`, severity, status) |
| `get_finding` | Details of one finding |
| `list_repos` | Repositories Satori can target, with their last execution |
| `list_executions` | Past executions, newest first (filter by `job_id`, `status`, `report_status`, `job_type`, `from_`/`to`, `q`; paginated, max 25) |
| `stop_execution` | Cancel a running execution (no-op if it is not running) |
| `get_execution_playbook` | The playbook YAML an execution ran (capped) |

All responses are size-capped. Prefer `get_execution_output` with a `test` filter (for example `cmd.0`) instead of requesting full logs.

### `run_playbook` notes

Provide exactly one of `playbook_path` (local `.yml` / `.yaml` file) or `playbook_yaml` (inline YAML). Optional `repository` is an `owner/repo` from `list_repos`. With `wait` (default true), the tool polls until the job finishes or `wait_seconds` elapses (max 600); then call `get_execution` with the returned `execution_id`.

## Playbook docs as resources

The server exposes playbook reference pages as MCP resources (fetched from `https://docs-v2.satori.ci`, override with `SATORI_DOCS_URL`):

| Resource URI | Content |
| --- | --- |
| `satori-docs://playbooks/language` | Playbook language |
| `satori-docs://playbooks/asserts` | Asserts |
| `satori-docs://playbooks/inputs` | Inputs |
| `satori-docs://playbooks/settings` | Settings |
| `satori-docs://playbooks/execution` | Execution |

Agents should read `satori-docs://playbooks/language` before writing or running a playbook.

## Prompt

`write_and_run_playbook` guides the agent to read the language docs, write YAML, call `run_playbook`, then summarize with `get_execution` / `get_execution_output` / `list_findings` and include the `report_url`.

## Errors

Auth and API failures return small error objects instead of crashing the protocol. If you are not logged in, the response points you to `satori-v2 config token <token>`. A `403` includes a hint that the action may need a PRO or ENTERPRISE plan.

---

If you need any help, please reach out to us on [Discord](https://discord.gg/NJHQ4MwYtt) or via [Email](mailto:support@satori.ci)
