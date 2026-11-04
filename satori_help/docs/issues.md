# Issues

Executions and their reports are immutable: once a playbook has run, its output and its pass/fail result never change. **Issues** are the mutable layer on top of them. An issue is an assert failure or a tool hit (semgrep, pyspector, trufflehog, etc.) that has been promoted to something your team tracks: it has a status, a severity, an assignee and a timeline of comments and events.

Tool hits come from structured JSON stdout. When writing playbooks, prefer each tool’s JSON flags — see [Tool output](playbooks/tool-output.md).

Issues are created from the web dashboard (the *Triage* button of a report) and can be listed, inspected, commented on and turned into GitHub security advisories from the CLI.

| Command | Description |
| --- | --- |
| `satori-v2 issues` | List issues across all your executions (sorted by severity) |
| `satori-v2 issues EXECUTION-ID` | List the issues of one execution |
| `satori-v2 report EXECUTION-ID issues` | Same as `issues EXECUTION-ID` |
| `satori-v2 issue ISSUE-ID` | Show one issue |
| `satori-v2 issue ISSUE-ID status STATUS` | Set the issue status |
| `satori-v2 issue ISSUE-ID exploitability VALUE --reason TEXT` | Set whether the issue is exploitable |
| `satori-v2 issue ISSUE-ID comment BODY` | Add a comment to the issue |
| `satori-v2 issue ISSUE-ID verify` | Verify the issue with Claude Code (TP/FP) |
| `satori-v2 run PLAYBOOK --repo owner/repo --verify` | After a run finishes, verify every finding the same way |
| `satori-v2 local PLAYBOOK --repo owner/repo --verify` | Run locally against a cloned repo, then verify every finding |
| `satori-v2 issue ISSUE-ID advisory` | Create a draft GitHub security advisory from an issue |
| `satori-v2 issue ISSUE-ID advisory --publish` | Publish the draft advisory to GitHub |
| `satori-v2 issue ISSUE-ID advisory --status` | Fetch the live GitHub advisory status |
| `satori-v2 issue ISSUE-ID advisory --delete` | Delete the advisory |
| `satori-v2 advisories` | List external issues (e.g. GitHub security advisories) you created |
| `satori-v2 advisory ADVISORY-ID` | Show one external issue |
| `satori-v2 advisory ADVISORY-ID edit` | Edit a draft advisory's title or description |
| `satori-v2 advisory ADVISORY-ID visibility VISIBILITY` | Set the external issue visibility |

## Listing issues

```sh
satori-v2 issues
satori-v2 issues --status OPEN --severity high,critical
satori-v2 issues --exploitability EXPLOITABLE
satori-v2 issues --execution-id V1StGXR8Z5jdHi6BmyT2k --source TOOL --json
satori-v2 issues V1StGXR8Z5jdHi6BmyT2k
satori-v2 report V1StGXR8Z5jdHi6BmyT2k issues
```

`issues` without an execution ID lists issues across all your executions. Pass an optional `EXECUTION-ID` argument (or `--execution-id`) to limit the list to one report. By default the list is sorted from highest severity to lowest; use `--order` to override that.

| Flag | Description |
| --- | --- |
| `EXECUTION-ID` | Optional positional argument; only issues of this execution |
| `--execution-id ID` | Same as the positional `EXECUTION-ID` (cannot conflict with it) |
| `--status STATUS` | One of `OPEN`, `INVESTIGATING`, `TP`, `FIXED`, `FP`, `ACCEPTED` |
| `--exploitability VALUE` | One of `UNKNOWN`, `EXPLOITABLE`, `NOT_EXPLOITABLE`, `INCONCLUSIVE` |
| `--source {ASSERT\|TOOL}` | `ASSERT` for failed playbook asserts, `TOOL` for hits reported by a tool |
| `--severity LEVELS` | Comma-separated severities: `BLOCKER`, `CRITICAL`, `HIGH`, `MEDIUM`, `LOW`, `INFO` (e.g. `high,critical`) |
| `--order {ASC\|DESC}` | Sort order (disables the default severity sort) |
| `--json` | Print the list as JSON |
| `--page N` | Page number (default 1) |
| `-q, --quantity N` | Results per page (default 10, alias `-l/--limit`) |

`report EXECUTION-ID issues` accepts the same flags except `--execution-id` and `--exploitability`.

Each row shows the issue ID, which you then pass to `issue`.

### Issue statuses

| Status | Meaning |
| --- | --- |
| `OPEN` | Newly triaged, nobody has looked at it yet |
| `INVESTIGATING` | Someone is checking whether it is real |
| `TP` | Verified as a real problem (true positive) |
| `FIXED` | The underlying problem was solved |
| `FP` | The tool or assert was wrong (false positive) |
| `ACCEPTED` | Real, but the team decided not to act on it |

Statuses can be changed from the dashboard or from the CLI with `issue ISSUE-ID status`:

```sh
satori-v2 issue Xk3pR9sT2vWq7LmN4bH8j status investigating
satori-v2 issue Xk3pR9sT2vWq7LmN4bH8j status fixed
satori-v2 issue Xk3pR9sT2vWq7LmN4bH8j status fp --json
```

There is no fixed transition order.

### Exploitability

Independently of its status, an issue records whether it can actually be exploited:

| Value | Meaning |
| --- | --- |
| `UNKNOWN` | Not assessed yet (default) |
| `EXPLOITABLE` | It can be exploited |
| `NOT_EXPLOITABLE` | It cannot be exploited (for example, the code is unreachable) |
| `INCONCLUSIVE` | It was assessed, but the result is not clear |

Set it with `issue ISSUE-ID exploitability`. `--reason` is required for every value except `UNKNOWN`, and is recorded in the issue's timeline:

```sh
satori-v2 issue Xk3pR9sT2vWq7LmN4bH8j exploitability EXPLOITABLE --reason "User input reaches os.system"
satori-v2 issue Xk3pR9sT2vWq7LmN4bH8j exploitability NOT_EXPLOITABLE --reason "Only called from tests" --json
satori-v2 issue Xk3pR9sT2vWq7LmN4bH8j exploitability UNKNOWN
```

Without `--json`, the CLI prints `Issue {ISSUE-ID} exploitability set to {VALUE}`. With `--json`, it prints the updated issue. Filter the list with `satori-v2 issues --exploitability VALUE`.

## Inspecting an issue

```sh
satori-v2 issue Xk3pR9sT2vWq7LmN4bH8j
satori-v2 issue Xk3pR9sT2vWq7LmN4bH8j --json
```

Shows the issue details: source, title, severity, status, the execution it belongs to and the identity of the assert or tool hit (test path and assert name, or tool, check ID, file and line). Without `--json`, it also prints a **History** timeline of status changes, comments and other events, with actor display names when available.

## Comments

Add a comment to an issue's timeline:

```sh
satori-v2 issue Xk3pR9sT2vWq7LmN4bH8j comment "Investigating this further"
satori-v2 issue Xk3pR9sT2vWq7LmN4bH8j comment "Looks like a false positive" --json
```

Without `--json`, the CLI prints `Comment {id} added to issue {ISSUE-ID}`. With `--json`, it prints the created comment object.

## Verifying an issue

`issue ISSUE-ID verify` uses [Claude Code](https://docs.anthropic.com/en/docs/claude-code) to decide whether the issue is a true positive (`TP`) or a false positive (`FP`):

```sh
satori-v2 issue Xk3pR9sT2vWq7LmN4bH8j verify
```

The command clones the repository tied to the issue's execution and judges the issue with two Claude Code agents that read the code: an analyst and an adversary that argues the issue is a false positive. If they disagree, a third agent breaks the tie. The command then sets the issue status to `TP` or `FP`.

The agents can only read files (`Read`, `Grep`, `Glob`). Before they start, the clone's own agent configuration (`.claude`, `.mcp.json`, `CLAUDE.md`, `AGENTS.md`, `.cursorrules`) is renamed to `*.bak`, so a repository cannot run commands or change the instructions of the review.

Requirements:

- `git` and `claude` must be available on your `PATH`.
- The execution must belong to a `run --repo owner/repo`, a `local --repo owner/repo`, or to a scan of a single `owner/repo` repository (same repository constraint as advisories).

To verify every finding after a run finishes, use `--verify` on `run` or `local` (same Claude flow, one clone for the whole batch):

```sh
satori-v2 run PLAYBOOK --repo owner/repo --verify
satori-v2 local PLAYBOOK --repo owner/repo --verify
```

Add `--min-severity LEVEL` (`Blocker`, `Critical`, `High`, `Medium`, `Low`, `Info`) to verify only the findings at or above that severity:

```sh
satori-v2 run PLAYBOOK --repo owner/repo --verify --min-severity High
```

## GitHub security advisories

`issue ISSUE-ID advisory` creates a **draft** external issue for the issue, through the Satori [GitHub Application](https://github.com/apps/satorici). It does **not** publish to GitHub yet. The command prints the draft details, a dashboard link (`View on web: …/advisories/{id}`), and a warning with the publish recipe.

If the issue's execution is `PRIVATE`, creating the draft promotes it to `UNLISTED` so the report link embedded in the advisory is reachable by anyone who can open the advisory.

```sh
satori-v2 issue Xk3pR9sT2vWq7LmN4bH8j advisory
satori-v2 issue Xk3pR9sT2vWq7LmN4bH8j advisory --json
```

To publish the draft to GitHub as a security advisory in the repository of the execution, use `--publish`. The command prints the advisory URL (the `GHSA-...` identifier if no URL is available):

```sh
satori-v2 issue Xk3pR9sT2vWq7LmN4bH8j advisory --publish
satori-v2 issue Xk3pR9sT2vWq7LmN4bH8j advisory --publish --json
```

To delete the advisory (draft or published), use `--delete`:

```sh
satori-v2 issue Xk3pR9sT2vWq7LmN4bH8j advisory --delete
```

To check the advisory's current state on GitHub (for example `triage`, `draft`, or `published`), use `--status`. This is a live lookup against GitHub; the advisory must already be published (have a remote `GHSA-…` id), and you need a GitHub personal access token configured via settings:

```sh
satori-v2 issue Xk3pR9sT2vWq7LmN4bH8j advisory --status
satori-v2 issue Xk3pR9sT2vWq7LmN4bH8j advisory --status --json
```

Without `--json`, the CLI prints the status string. With `--json`, it prints `{"status": "…"}`.

`--publish`, `--status`, and `--delete` are mutually exclusive.

Requirements:

- The execution must belong to a `run --repo owner/repo`, a `local --repo owner/repo`, or to a scan of a single `owner/repo` repository. Executions that span several repositories are rejected.
- The Satori GitHub Application must be installed and active on that repository.
- Only one external issue can exist per finding. Running `advisory` again for an issue that already has a draft or published advisory returns the existing one instead of creating a second one.

```sh
satori-v2 run satori://code/trufflehog.yml --repo satorici/satori-cli --sync --report
satori-v2 issues V1StGXR8Z5jdHi6BmyT2k
satori-v2 issue Xk3pR9sT2vWq7LmN4bH8j advisory
satori-v2 issue Xk3pR9sT2vWq7LmN4bH8j advisory --publish
```

### Listing advisories

`satori-v2 advisories` lists the external issues you have already created (GitHub security advisories and related issues):

```sh
satori-v2 advisories
satori-v2 advisories --execution-id V1StGXR8Z5jdHi6BmyT2k
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
satori-v2 advisory 9aJ2kL5mN8pQ3rS6tU1vW
satori-v2 advisory 9aJ2kL5mN8pQ3rS6tU1vW --json
```

Shows the advisory details: title, kind, provider, severity, visibility, the related execution and issue, and the external ID/URL on GitHub.

To edit a draft before you publish it (for example, to rewrite the generated text), use `edit`. Pass `--title`, the description (`--body` or `--description`, in Markdown), or both. `--body-file FILE` reads the description from a file and takes precedence over `--body`:

```sh
satori-v2 advisory 9aJ2kL5mN8pQ3rS6tU1vW edit --title "SQL injection in the search endpoint"
satori-v2 advisory 9aJ2kL5mN8pQ3rS6tU1vW edit --body-file advisory.md
```

The CLI prints `Advisory updated`. You can only edit a draft: after the advisory is published to GitHub, its text cannot change.

To change who can see the advisory in Satori, set its visibility:

```sh
satori-v2 advisory 9aJ2kL5mN8pQ3rS6tU1vW visibility public
satori-v2 advisory 9aJ2kL5mN8pQ3rS6tU1vW visibility private
satori-v2 advisory 9aJ2kL5mN8pQ3rS6tU1vW visibility unlisted
```

| Visibility | Meaning |
| --- | --- |
| `PUBLIC` | Visible to everyone |
| `PRIVATE` | Visible only to you |
| `UNLISTED` | Accessible by link after login, not listed publicly |

An unlisted advisory's link contains its random 21-character ID, so it can't be guessed or found by trying IDs in sequence. Share it only with the people who should see the advisory.

See [Results](getting-started/execution-data.md) for the report commands and [Jobs, Executions & Output](modes/executions.md) for the job and execution model.
