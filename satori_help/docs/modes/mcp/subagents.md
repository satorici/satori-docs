---
prev:
  text: 'Agent rules'
  link: '/modes/mcp/agent-rules'
next:
  text: 'Reference'
  link: '/modes/mcp/reference'
---

# Optional: Satori as a subagent

The [agent rules](/modes/mcp/agent-rules) nudge the main agent to verify through Satori. A **subagent** is a separate agent with its own context that the parent can delegate to after implementing a feature, so quality and security runs (and their logs) do not flood the main chat.

Satori remains an MCP server — the subagent’s job is to drive the Satori MCP tools. Configure the `satori` server on the **parent** first ([Setup](/modes/mcp/setup#configure-your-agent)); subagents inherit MCP from the parent and cannot substitute their own server config.

Formats differ by client. For Cursor and Claude Code, use markdown with YAML frontmatter. For Codex, use a standalone TOML file. Cursor also loads `.claude/agents/` and `.codex/agents/` for compatibility, but that path expects Cursor-style markdown, not Codex TOML — ship both a markdown file and a `.toml` if you want all three clients.

| Client | Path | Format |
| --- | --- | --- |
| Cursor | `.cursor/agents/satori.md` (or `.claude/agents/satori.md`) | Markdown + YAML frontmatter |
| Claude Code | `.claude/agents/satori.md` | Markdown + YAML frontmatter |
| Codex | `.codex/agents/satori.toml` | TOML (`name`, `description`, `developer_instructions`) |

### Cursor

Add `.cursor/agents/satori.md` (Cursor also loads the same file from `.claude/agents/`):

````markdown
---
name: satori
description: >-
  Satori CI verifier. Use proactively after implementing a feature or
  substantial code change to run quality and security checks on the new
  code via Satori MCP (not shell-only unit tests).
---

You verify newly implemented features with Satori for quality and security.

When invoked after implementation:
1. If `.satori-llm.yml` is missing, call recommend_playbook; write files only with approval.
2. Baseline with run_local on `.satori-llm.yml` if not already baselined this session.
3. Re-run run_local after the change; fix or report only failures not in the baseline.
4. Summarize with get_execution / get_execution_output / list_findings; prefer tool JSON flags.
5. Do not treat pytest / npm test alone as sufficient. If you used create_ssh_session / exec_in_session, always stop_ssh_session when done.

Report what passed, what failed, and any security findings before the feature is considered done.
````

Invoke with `/satori` or by asking the agent to use the satori subagent after a feature lands.

### Claude Code

Add `.claude/agents/satori.md` with the same content as the Cursor example (omit Claude-only frontmatter fields such as `tools` or `mcpServers` if you want the file to stay portable to Cursor).

### Codex

Add `.codex/agents/satori.toml` (or `~/.codex/agents/satori.toml` for all projects). Codex custom agents are TOML, not markdown. Ask Codex to spawn or use the `satori` agent after a feature lands — it does not auto-delegate the same way by default. MCP must already be configured on the parent; fields like `mcp_servers` in the agent file do not override the parent.

```toml
name = "satori"
description = """
Satori CI verifier. Use proactively after implementing a feature or substantial
code change to run quality and security checks on the new code via Satori MCP
(not shell-only unit tests).
"""
developer_instructions = """
You verify newly implemented features with Satori for quality and security.

When invoked after implementation:
1. If `.satori-llm.yml` is missing, call recommend_playbook; write files only with approval.
2. Baseline with run_local on `.satori-llm.yml` if not already baselined this session.
3. Re-run run_local after the change; fix or report only failures not in the baseline.
4. Summarize with get_execution / get_execution_output / list_findings; prefer tool JSON flags.
5. Do not treat pytest / npm test alone as sufficient. If you used create_ssh_session / exec_in_session, always stop_ssh_session when done.

Report what passed, what failed, and any security findings before the feature is considered done.
"""
```
