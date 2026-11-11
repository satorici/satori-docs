---
next:
  text: 'Tools'
  link: '/modes/mcp/tools'
---

# MCP server

[`satori-mcp`](https://github.com/satorici/satori-mcp) is a local [Model Context Protocol](https://modelcontextprotocol.io) (MCP) server over stdio. AI agents such as Claude Code, Codex, and Cursor can use it to run playbooks, inspect executions, and read findings through your existing Satori credentials. It runs straight from GitHub with `npx` (Node.js 22 or later), so there is nothing to install:

```console
npx -y github:satorici/satori-mcp
```

Your agent reports "tests pass"; Satori shows you which tests it ran — every command, assertion and output — live in the web report:

![An AI agent says tests pass; the Satori report shows every test it ran](/mcp_visibility_loop.svg)

The server shares credentials with the CLI: it uses the token saved by `satori-v2 config token` (`~/.satori_credentials.yml`), or `SATORI_TOKEN` / `SATORI_PROFILE` from its environment (`SATORI_TOKEN` overrides the credentials file). Configure a token first — see [Installation](/getting-started/install.md) — or pass `SATORI_TOKEN` in the agent config (see [below](#ci-or-no-credentials-file)).

## Configure your agent

Add the server to your agent's MCP config. The agent launches it itself — stdout is the protocol channel, so do not pipe or redirect it. The first start builds the package from GitHub (about 20 seconds); later starts use the npm cache.

::: warning Your agent may skip the Satori tests
Connecting the MCP server does not make the agent use it. Agents often fall back to a familiar shell command (`pytest`, `npm test`) and skip the Satori checks. If that happens, add a project rule that tells the agent to verify through Satori: see [Agent rules](/modes/mcp/agent-rules).
:::

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

Next: add the [Claude Code rule](/modes/mcp/agent-rules#claude-code) so the agent does not skip the Satori tests.

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

Next: add the [Codex rule](/modes/mcp/agent-rules#codex) so the agent does not skip the Satori tests.

### Cursor

In `.cursor/mcp.json` or global MCP settings:

```json
{
  "mcpServers": {
    "satori": { "command": "npx", "args": ["-y", "github:satorici/satori-mcp"] }
  }
}
```

Next: add the [Cursor rule](/modes/mcp/agent-rules#cursor) so the agent does not skip the Satori tests.

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
