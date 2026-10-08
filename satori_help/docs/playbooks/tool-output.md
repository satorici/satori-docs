---
next:
  text: 'Issues'
  link: '/issues'
---

# Tool output

When a playbook runs a security or analysis tool, prefer that tool’s **JSON (or JSON Lines) stdout** over its default human-readable text whenever the tool supports it.

Satori’s findings parser reads tool stdout after the run. Structured JSON becomes triageable [issues](../issues.md) with source `TOOL`. Plain text usually cannot — you still get assert pass/fail, but no parsed tool hits.

## Rule

1. If the tool has a JSON / JSONL / structured-report flag, **use it**.
2. Keep install and setup commands separate from the scan command so install logs do not mix into the scan stdout.
3. Use [asserts](asserts.md) for pass/fail checks; rely on JSON stdout for finding extraction.

## Preferred invocations

These match the formats Satori’s dedicated parsers recognize:

| Tool | Prefer |
| --- | --- |
| semgrep | `semgrep --json …` |
| bandit | `bandit -f json …` |
| gosec | `gosec -fmt=json …` |
| eslint | `eslint -f json …` |
| pyspector | `pyspector scan -f json …` (or `--format json`) |
| ruff | `ruff check --output-format=json …` |
| basedpyright / pyright | `basedpyright --outputjson …` |
| checkov | `checkov -o json …` |
| gitleaks | `gitleaks … --report-format json` |
| trufflehog | `trufflehog … --json` |
| trivy | `trivy … --format json` |
| nuclei | `nuclei … -jsonl` |

Example:

```yml
settings:
  name: Semgrep secrets scan

install:
- pip install semgrep

semgrep:
- semgrep --config 'p/secrets' --json .
```

Without `--json`, the same scan may finish successfully but produce no `TOOL` findings.

## Other tools

Tools without a dedicated parser can still yield findings when their stdout is JSON or JSON Lines — Satori’s `dynamic` fallback extracts records from recognizable shapes (for example shellcheck, hadolint, grype, npm audit). Prefer each tool’s JSON flag so that fallback can run.

If a tool only emits text, use asserts on stdout/stderr; do not expect `TOOL` issues from that command.

---
If you need any help, please reach out to us on [Discord](https://discord.gg/NJHQ4MwYtt) or via [Email](mailto:support@satori.ci)
