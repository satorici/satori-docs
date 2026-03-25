---
next:
  text: 'Shell'
  link: '/modes/shell'
---

# AI

Satori AI lets you describe what you want to test in plain language and generates a ready-to-run playbook for you. Whether you are a developer, a pentester, a QA engineer, or a CTO, you can tell it what to check and it will produce the right playbook for your role.

Watch it in action:

<iframe width="100%" height="400" src="https://www.youtube.com/embed/HUv82qwX4Ls" title="Satori AI - Generate Testing Playbooks" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

[Watch on YouTube](https://youtu.be/HUv82qwX4Ls)

## Requirements

Satori AI requires the Claude Code CLI to be installed on your machine:

```console
npm install -g @anthropic-ai/claude-code
```

You also need a valid Anthropic API key configured for Claude Code. See the [Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code) for setup instructions.

## Usage

Satori AI works in two modes: interactive and one-shot.

### Interactive Mode

Launch an interactive session where you can have a conversation about what you want to test. The AI will generate playbooks, explain them, and refine them based on your feedback:

```console
satori ai
```

This opens a conversation where you can say things like:

- "Test my Python app for SQL injection"
- "Check if our API returns the right headers for SOC2 compliance"
- "Scan this repo for hardcoded secrets"
- "Create a monitor that checks our website every hour"

The AI knows the full Satori playbook language, all public playbooks, and all assertion types. It will write a `.yml` file and give you the command to run it.

### One-Shot Mode

If you already know what you want, pass it directly as a prompt:

```console
satori ai "test my Django app for common security issues"
```

The AI will generate the playbook and provide the execution command without entering an interactive session.

## Playbooks for Every Role

Different people in an organization need different tests. Satori AI understands this and generates playbooks appropriate for each role:

**For the CEO or compliance officer** — verify SOC2 controls, check TLS configuration, security headers, and exposed ports. The result is a report that states which controls passed and which did not, with their severities:

```console
satori ai "verify SOC2 compliance for our website https://example.com"
```

**For the CTO** — run a web security audit that reviews server configuration, checks for common misconfigurations, and validates that infrastructure meets security standards:

```console
satori ai "run a security audit on our web server at https://example.com"
```

**For the development lead** — scan Docker images for known vulnerabilities before allowing them into production, or check that new code does not introduce regressions:

```console
satori ai "scan our Docker image myapp:latest for vulnerabilities"
```

**For the pentester** — launch network scans from ephemeral containers, detect open ports, enumerate services, and scan for known vulnerabilities at scale:

```console
satori ai "perform a network scan on 10.0.0.0/24 looking for exposed services"
```

**For CI engineers** — generate playbooks that run on every push to detect issues before code is merged:

```console
satori ai "create a CI playbook that runs semgrep and trufflehog on every push"
```

**For QA engineers** — create tests that verify application behavior matches expectations, track regressions, and keep a record of what was tested:

```console
satori ai "test that our API at https://api.example.com/health returns status 200"
```

## What the AI Knows

When you launch `satori ai`, it has access to:

- The complete Satori playbook syntax, including all assertion types, input formats, and settings
- All public playbooks in the [Satori playbook library](https://github.com/satorici/playbooks)
- The playbook validation rules from the playbook-validator
- All CLI commands and their options

It clones the Satori repositories to `~/.satori/` on first use to keep its knowledge base up to date.

## Examples

Generate a playbook and run it immediately:

```console
satori ai "check if port 443 is open on satori.ci and verify the TLS certificate is valid"
```

Generate a monitoring playbook that runs on a schedule:

```console
satori ai "monitor our API every 30 minutes and alert on Slack if it returns anything other than 200"
```

Generate a comprehensive security check for a repository:

```console
satori ai "create a full security playbook for a Python project: lint, secrets, SAST, and dependency audit"
```

---

If you need any help, please reach out to us on [Discord](https://discord.gg/NJHQ4MwYtt) or via [Email](mailto:support@satori.ci)
