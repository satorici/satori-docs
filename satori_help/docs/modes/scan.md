# Scan

You can run a playbook on all the repositories of a Github account or on all the commits of a repository

Whenever you want to run an execution on each of the individual commits of a repository, you can use the scan functionality.

## Scan Github Account Repositories

```sh
satori scan githubUsername/* --playbook satori://whatever
```

Example:

![Scan Account](img/scan_account.png)

## Scan Github Repository Commits

If you target a repo, the optional parameter `-c` is used to indicate the percentage of repository commits to include in the scan. For example `-c 1` will scan 1% of the repository commits if you only want to take a sample. This is useful for sampling large repositories:

```sh
satori scan githubUsername/repository
```

Example:

![Scan Repo](img/scan_1.png)

If you however want to be sure that everything was tested, you can target full scan coverage on all the repository commits, you would:

```sh
satori scan githubUsername/repository -c 100
```

You can see how the results of your playbook affect different commits and forks of your repository.

## Scan Information

If need to get the status of a scan, you can reference its id with:

```sh
satori scan ID
```

Example:

![Scan Account](img/scan_info.png)

### Scan Status

Since normally repositories have a lot of commits, you may want to check what the execution status is with this command:

```sh
satori scan ScanID status
```

![Scan Repo](img/scan_2.png)

It shows the current status, the amount of commits found, which ones were scanned, which ones are being scanned and which ones are scheduled to be scanned. Since no scan is being run at the time of executing this command, there is no progress but in other cases it would be a percentage.

### Scan Stop

If at any point you want to cancel the scan, you use the `stop` action:

```sh
satori scan ScanID stop
```

Example:

![Stop Scan Repo](img/scan_3.png)

### Scan Reports

You can list the reports associated to a scan by running the command:

```sh
satori scan ID reports
```

Example:

![Scan Reports](img/scan_reports.png)

### Scan Clean

> [!WARNING]
> This command will delete all the reports associated to a certain repository:

```sh
satori scan githubUsername/repository clean
```

Example:

![Clean Scan Repo](img/scan_4.png)

You can also delete commit records along with reports:

```sh
satori scan githubUsername/repository clean --delete-commits
```

## Advanced Scan Options

The `satori scan` command provides extensive options for controlling scanning behavior and filtering results.

### Branch and Date Filtering

| Flag | Description | Example |
| --- | --- | --- |
| `-b, --branch BRANCH` | Scan specific branch (default: main) | `satori scan user/repo -b develop` |
| `--from YYYY-MM-DD` | Start date for scanning commits | `satori scan user/repo --from 2024-01-01` |
| `--to YYYY-MM-DD` | End date for scanning commits | `satori scan user/repo --to 2024-12-31` |

### Data and Configuration

| Flag | Description | Example |
| --- | --- | --- |
| `-d, --data JSON` | Provide secrets/parameters as JSON string | `satori scan user/repo -d '{"API_KEY":"secret"}'` |
| `--playbook URI` | Use specific playbook instead of repository's default | `satori scan user/repo --playbook satori://code/semgrep.yml` |

### Execution Control

| Flag | Description | Example |
| --- | --- | --- |
| `-s, --sync` | Wait for scan to complete | `satori scan user/repo -s` |
| `-o, --output` | Display command output | `satori scan user/repo -s --output` |
| `-r, --report` | Display test results | `satori scan user/repo -s --report` |
| `--skip-check` | Skip repository existence check | `satori scan user/repo --skip-check` |
| `--visibility {public\|private\|unlisted}` | Set scan visibility | `satori scan user/repo --visibility public` |

### Report Pagination

| Flag | Description | Example |
| --- | --- | --- |
| `-p, --page NUMBER` | Show specific page of results | `satori scan ID reports -p 2` |
| `-l, --limit NUMBER` | Number of results per page (default: 20) | `satori scan ID reports -l 50` |

### Cleanup Options

| Flag | Description | Example |
| --- | --- | --- |
| `--delete-commits` | Delete commit records during cleanup | `satori scan ID clean --delete-commits` |

### Complete Scan Example

```sh
satori scan user/repo \
  -c 50 \
  -b develop \
  --from 2024-01-01 \
  --to 2024-12-31 \
  -d '{"API_KEY":"my-secret-key"}' \
  --playbook satori://code/semgrep.yml \
  --sync \
  --report \
  --visibility private
```

This command:
- Scans 50% of commits in the `develop` branch
- Limits to commits between January 1 and December 31, 2024
- Provides an API key as a secret parameter
- Uses the Semgrep playbook
- Waits for completion and displays the report
- Sets visibility to private
