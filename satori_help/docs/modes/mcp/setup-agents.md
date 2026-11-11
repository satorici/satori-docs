---
prev:
  text: 'Setup'
  link: '/modes/mcp/setup'
next:
  text: 'Tools'
  link: '/modes/mcp/tools'
---

# Setup (Agents)

This page is written for an AI agent (Claude Code, Codex or Cursor) that was asked to install the Satori MCP server. If you are a person, use [Setup](/modes/mcp/setup) instead, or paste this into your agent:

```text
Install the Satori MCP server by following https://docs-v2.satori.ci/modes/mcp/setup-agents.md
```

Agent: do the steps in order. Use only the section for the agent you are.

## 1. Check the prerequisites

1. Run `node --version`. The server needs Node.js 22 or later. If it is older or missing, stop and tell the user.
2. Check that Satori credentials exist: the `SATORI_TOKEN` environment variable is set, or the file `~/.satori_credentials.yml` exists. Check only that they exist. Do not print the token or the file.
3. If there are no credentials, stop and ask the user to run this in their own terminal. It asks for the API token from their profile at <https://satori.ci> and saves it:

   ```console
   npx -y github:satorici/satori-mcp login
   ```

   Do not run `login` yourself, do not ask the user to paste the token in the chat, and do not write a token to any file in the project.

## 2. Add the MCP server

Skip this step if a server named `satori` is already configured.

### Claude Code

```console
claude mcp list
claude mcp add --scope user satori -- npx -y github:satorici/satori-mcp
```

### Codex

```console
codex mcp list
codex mcp add satori -- npx -y github:satorici/satori-mcp
```

### Cursor

Add the `satori` entry to `mcpServers` in `.cursor/mcp.json`. Create the file if it does not exist. Keep every other server that is already there.

```json
{
  "mcpServers": {
    "satori": { "command": "npx", "args": ["-y", "github:satorici/satori-mcp"] }
  }
}
```

Do not run `npx -y github:satorici/satori-mcp` yourself to test it: the agent starts the server, and its stdout is the protocol channel.

## 3. Add the verification rule

Without a project rule, agents often run a familiar shell command (`pytest`, `npm test`) and skip the Satori tests. Add the rule to the project you are working in.

- If the file already has a `Satori verification` section, leave it as it is.
- Add the rule at the end of the file. Do not change or remove anything else in it.
- Create the file if it does not exist.

### Claude Code

Add this to `CLAUDE.md` at the root of the project:

<!--@include: ./agent-rules.md#markdown-rule-->

### Codex

Add the same block to `AGENTS.md` at the root of the project:

<!--@include: ./agent-rules.md#markdown-rule-->

### Cursor

Create `.cursor/rules/satori-verify.mdc` with this content:

<!--@include: ./agent-rules.md#cursor-rule-->

## 4. Verify

The agent loads a new MCP server when a session starts, so the Satori tools are not available in the session that installed them.

1. Tell the user to restart the agent, or to reload its MCP servers.
2. In the new session, call the `whoami` tool of the `satori` server. It returns the active profile when the server and the credentials work. The first start takes about 20 seconds because `npx` builds the package.

## 5. Report

Tell the user:

- Which MCP config you changed, and with which command or file.
- Which rule file you created or changed.
- That they must restart the agent before the Satori tools work.
- Anything you skipped, and why.
