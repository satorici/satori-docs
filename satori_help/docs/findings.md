# Findings & Issues

Executions and their reports are immutable: once a playbook has run, its output and its pass/fail result never change. **Findings** (also called **issues** in the CLI) are the mutable layer on top of them. A finding is an assert failure or a tool hit (semgrep, pyspector, trufflehog, etc.) that has been promoted to something your team tracks: it has a status, a severity, an assignee and a timeline of comments and events.

Findings are created from the web dashboard (the *Triage* button of a report) and can be listed, inspected and turned into GitHub security advisories from the CLI.

| Command | Description |
| --- | --- |
| `satori-v2 issues` | List issues across all your executions (sorted by severity) |
| `satori-v2 issues EXECUTION-ID` | List the issues of one execution |
| `satori-v2 report EXECUTION-ID issues` | Same as `issues EXECUTION-ID` |
| `satori-v2 issue FINDING-ID` | Show one issue |
| `satori-v2 issue FINDING-ID status STATUS` | Set the issue status |
| `satori-v2 issue FINDING-ID advisory` | Create a GitHub security advisory from an issue |
| `satori-v2 advisories` | List external issues (e.g. GitHub security advisories) you created |
| `satori-v2 advisory ADVISORY-ID` | Show one external issue |
| `satori-v2 advisory ADVISORY-ID visibility VISIBILITY` | Set the external issue visibility |

## Listing issues

```sh
satori-v2 issues
satori-v2 issues --status OPEN --severity 4
satori-v2 issues --execution-id 5678 --source TOOL --json
satori-v2 issues 5678
satori-v2 report 5678 issues
```

`issues` without an execution ID lists issues across all your executions. Pass an optional `EXECUTION-ID` argument (or `--execution-id`) to limit the list to one report. By default the list is sorted from highest severity to lowest; use `--order` to override that.

| Flag | Description |
| --- | --- |
| `EXECUTION-ID` | Optional positional argument; only issues of this execution |
| `--execution-id ID` | Same as the positional `EXECUTION-ID` (cannot conflict with it) |
| `--status STATUS` | One of `OPEN`, `INVESTIGATING`, `CONFIRMED`, `FIXED`, `FALSE_POSITIVE`, `ACCEPTED_RISK` |
| `--source {ASSERT\|TOOL}` | `ASSERT` for failed playbook asserts, `TOOL` for hits reported by a tool |
| `--severity {0-5}` | Severity level |
| `--order {ASC\|DESC}` | Sort order (disables the default severity sort) |
| `--json` | Print the list as JSON |
| `--page N` | Page number (default 1) |
| `-q, --quantity N` | Results per page (default 10, alias `-l/--limit`) |

Each row shows the finding ID, which you then pass to `issue`.

### Issue statuses

| Status | Meaning |
| --- | --- |
| `OPEN` | Newly triaged, nobody has looked at it yet |
| `INVESTIGATING` | Someone is checking whether it is real |
| `CONFIRMED` | Verified as a real problem |
| `FIXED` | The underlying problem was solved |
| `FALSE_POSITIVE` | The tool or assert was wrong |
| `ACCEPTED_RISK` | Real, but the team decided not to act on it |

Statuses can be changed from the dashboard or from the CLI with `issue FINDING-ID status`:

```sh
satori-v2 issue 42 status investigating
satori-v2 issue 42 status fixed
satori-v2 issue 42 status false_positive --json
```

There is no fixed transition order.

## Inspecting an issue

```sh
satori-v2 issue 42
satori-v2 issue 42 --json
```

Shows the issue details: source, title, severity, status, the execution it belongs to and the identity of the assert or tool hit (test path and assert name, or tool, check ID, file and line).

## GitHub security advisories

`issue FINDING-ID advisory` creates an **external issue** for the finding and publishes it as a GitHub security advisory in the repository of the execution, through the Satori [GitHub Application](https://github.com/apps/satorici). The command prints the advisory URL (the `GHSA-...` identifier if no URL is available):

```sh
satori-v2 issue 42 advisory
satori-v2 issue 42 advisory --json
```

Requirements:

- The execution must belong to a `run --repo owner/repo` or to a scan of a single `owner/repo` repository. Executions that span several repositories are rejected.
- The Satori GitHub Application must be installed and active on that repository.
- Only one external issue can exist per execution. Running the command again for a finding whose advisory was already sent returns the existing advisory instead of creating a second one.

```sh
satori-v2 run satori://code/trufflehog.yml --repo satorici/satori-cli --sync --report
satori-v2 issues 5678
satori-v2 issue 42 advisory
```

### Listing advisories

`satori-v2 advisories` lists the external issues you have already created (GitHub security advisories and related issues):

```sh
satori-v2 advisories
satori-v2 advisories --execution-id 5678
satori-v2 advisories --kind SECURITY_ADVISORY --provider GITHUB --order DESC
satori-v2 advisories --json
```

| Flag | Description |
| --- | --- |
| `--execution-id ID` | Only external issues for this execution |
| `--kind {SECURITY_ADVISORY\|ISSUE}` | Filter by kind |
| `--provider GITHUB` | Filter by provider |
| `--order {ASC\|DESC}` | Sort order |
| `--json` | Print the list as JSON |
| `--page N` | Page number (default 1) |
| `-q, --quantity N` | Results per page (default 10, alias `-l/--limit`) |

Each row shows the advisory ID, which you then pass to `advisory`.

### Inspecting and updating an advisory

```sh
satori-v2 advisory 1
satori-v2 advisory 1 --json
```

Shows the advisory details: title, kind, provider, severity, visibility, the related execution and finding, and the external ID/URL on GitHub.

To change who can see the advisory in Satori, set its visibility:

```sh
satori-v2 advisory 1 visibility public
satori-v2 advisory 1 visibility private
satori-v2 advisory 1 visibility unlisted
```

| Visibility | Meaning |
| --- | --- |
| `PUBLIC` | Visible to everyone |
| `PRIVATE` | Visible only to you |
| `UNLISTED` | Accessible by link, not listed publicly |

See [Results](getting-started/execution-data.md) for the report commands and [Jobs, Executions & Output](modes/executions.md) for the job and execution model.
