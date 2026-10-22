---
prev:
  text: 'Subagents'
  link: '/modes/mcp/subagents'
next:
  text: 'Shell'
  link: '/modes/shell'
---

# Reference

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
