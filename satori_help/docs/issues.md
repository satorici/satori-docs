# Issues

Executions and their reports are immutable: once a playbook has run, its output and its pass/fail result never change. **Issues** are the mutable layer on top of them. An issue is an assert failure or a tool hit (semgrep, pyspector, trufflehog, etc.) that has been promoted to something your team tracks: it has a status, a severity, an assignee and a timeline of comments and events.

Issues are created from the web dashboard (the *Triage* button of a report) and can be listed, inspected, commented on and turned into GitHub security advisories from the CLI.

| Command | Description |
| --- | --- |
| `satori-v2 issues` | List issues across all your executions (sorted by severity) |
| `satori-v2 issues EXECUTION-ID` | List the issues of one execution |
| `satori-v2 report EXECUTION-ID issues` | Same as `issues EXECUTION-ID` |
| `satori-v2 issue FINDING-ID` | Show one issue |
| `satori-v2 issue FINDING-ID status STATUS` | Set the issue status |
| `satori-v2 issue FINDING-ID comment BODY` | Add a comment to the issue |
| `satori-v2 issue FINDING-ID advisory` | Create a draft GitHub security advisory from an issue |
| `satori-v2 issue FINDING-ID advisory --publish` | Publish the draft advisory to GitHub |
| `satori-v2 issue FINDING-ID advisory --delete` | Delete the advisory |
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

Each row shows the issue ID, which you then pass to `issue`.

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

## Comments

Add a comment to an issue's timeline:

```sh
satori-v2 issue 42 comment "Investigating this further"
satori-v2 issue 42 comment "Looks like a false positive" --json
```

Without `--json`, the CLI prints `Comment {id} added to issue {FINDING-ID}`. With `--json`, it prints the created comment object.

## GitHub security advisories

`issue FINDING-ID advisory` creates a **draft** external issue for the issue, through the Satori [GitHub Application](https://github.com/apps/satorici). It does **not** publish to GitHub yet. The command prints the draft details, a dashboard link (`View on web: …/advisories/{id}`), and a warning with the publish recipe.

```sh
satori-v2 issue 42 advisory
satori-v2 issue 42 advisory --json
```

To publish the draft to GitHub as a security advisory in the repository of the execution, use `--publish`. The command prints the advisory URL (the `GHSA-...` identifier if no URL is available):

```sh
satori-v2 issue 42 advisory --publish
satori-v2 issue 42 advisory --publish --json
```

To delete the advisory (draft or published), use `--delete`:

```sh
satori-v2 issue 42 advisory --delete
```

`--publish` and `--delete` are mutually exclusive.

Requirements:

- The execution must belong to a `run --repo owner/repo` or to a scan of a single `owner/repo` repository. Executions that span several repositories are rejected.
- The Satori GitHub Application must be installed and active on that repository.
- Only one external issue can exist per execution. Running `advisory` again for an issue that already has a draft returns the existing draft instead of creating a second one.

```sh
satori-v2 run satori://code/trufflehog.yml --repo satorici/satori-cli --sync --report
satori-v2 issues 5678
satori-v2 issue 42 advisory
satori-v2 issue 42 advisory --publish
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

Shows the advisory details: title, kind, provider, severity, visibility, the related execution and issue, and the external ID/URL on GitHub.

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
