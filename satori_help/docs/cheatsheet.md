# Satori CI CLI Cheatsheet

Commands marked *(on development)* are not available yet in CLI v2. Their v1 syntax is kept here for reference.

## Install, Update and Configure

| Command | Description |
| --- | --- |
| `pip install git+https://github.com/satorici/cli-v2` | Install the latest version. The console script is named `satori-v2` so it can coexist with the v1 `satori` CLI |
| `satori-v2 install` | Guided onboarding: opens browser, saves token, installs CLI v2 *(on development)* |
| `satori-v2 update` | Update to the latest version (reinstalls from git with pip) |
| `satori-v2 config` | Show the current configuration |
| `satori-v2 config token "USERTOKEN"` | Configure your user token as your default profile |
| `satori-v2 config token "TEAMTOKEN" --profile TEAM` | Configure your team token on your team profile |
| `satori-v2 config pat "GITHUB_PAT"` | Set your GitHub personal access token (patched via the API) |
| `satori-v2 whoami` | Show the active profile and whether a GitHub PAT is configured |
| `satori-v2 width` | Show console width configuration for current profile *(on development)* |

## Global options & environment

| Option / Variable | Description |
| --- | --- |
| `--json` | Print the raw JSON response (available on the root and most commands) |
| `--format {json\|md}` | Set the output format on the root command, `run`, `report ID output`, `output` and `execution output` |
| `--page N` | Page number on list commands (default: 1) |
| `-q N, --quantity N` (aliases `-l`, `--limit`) | Number of results per page on list commands (default: 10) |
| `--public` | List public items instead of yours on the root, `jobs`, `reports`, `monitors` and `scans` |
| `--profile PROFILE` | Select the credentials profile. Only valid on `satori-v2 config` |
| `~/.satori_credentials.yml` | Credentials file, one section per profile (`default`, `TEAM`, ...) |
| `SATORI_TOKEN` | Token read directly from the environment (overrides the credentials file) |
| `SATORI_PROFILE` | Profile to use (overrides `--profile`) |
| `SATORI_ENDPOINT` | API endpoint (default: `https://api-v2.satori.ci`) |

## Run in the cloud

| Command | Description |
| --- | --- |
| `satori-v2 run ./` | Upload the current dir and run the playbook .satori.yml |
| `satori-v2 run playbook.yml` | Upload the playbook and run it |
| `satori-v2 run ./ --playbook="satori://..."` | Upload the current dir and run the specified playbook |
| `satori-v2 run semgrep` | Alias: run `satori://code/semgrep.yml` on the current dir |
| `satori-v2 run pyspector` | Alias: run `satori://code/python/pyspector.yml` on the current dir |
| `satori-v2 run PLAYBOOK --repo GithubUser/Repo` | Run the playbook on the latest commit of a Github repository (creates a 1-commit scan) |

## Run locally

| Command | Description |
| --- | --- |
| `satori-v2 local ./` | Execute the playbook .satori.yml locally |
| `satori-v2 local playbook.yml` | Execute the playbook locally |
| `satori-v2 local ./ --playbook="satori://..."` | Execute the specified playbook locally |

## Local execution parameters

| Parameter | Description |
| --- | --- |
| `-s, --sync` | Show summary when execution completes |
| `--report` | Display test assertions and results |
| `-o, --output` | Display command output |
| `-p, --playbook` | Playbook to execute instead of the source's `.satori.yml` |
| `-d, --data KEY=VALUE` | Provide values for the playbook variables (repeatable) |
| `--split KEY=DELIMITER` | Split the value of `KEY` into several values using `DELIMITER` (repeatable) |
| `-df, --data-file KEY=PATH` | Load variable values from a file (repeatable) |
| `--run` | Run specific tests only (repeatable) |
| `--timeout` | Execution timeout in seconds |
| `--visibility` | Set report visibility (public/private/unlisted) |
| `-t, --tag KEY VALUE` | Tag the execution (repeatable) |
| `--test` | Filter specific test output (repeatable) *(on development)* |
| `--name` | Name for this run *(on development)* |
| `--format` | Output format (plain or md) *(on development)* |
| `--redacted` | Mark parameters as redacted (repeatable) *(on development)* |
| `--save-report` | Save report to file (true/false or path) *(on development)* |
| `--save-output` | Save command output to file (true/false or path) *(on development)* |

## Run using these parameters

| Parameter | Description |
| --- | --- |
| `-s, --sync` | Show the result |
| `--report` | Show the report |
| `-o, --output` | Show the output |
| `--live-output` | Stream the output while the execution is running |
| `--stdout` | Show only the raw stdout of the execution |
| `--stderr` | Show only the raw stderr of the execution |
| `-f, --files` | Download the files created if the setting files was set to True |
| `--save-files` | Keep the files created by the execution without downloading them |
| `-p, --playbook` | Playbook to execute instead of the source's `.satori.yml` |
| `-d, --data KEY=VALUE` | Provide values for the playbook variables (repeatable) |
| `--split KEY=DELIMITER` | Split the value of `KEY` into several values using `DELIMITER` (repeatable) |
| `-df, --data-file KEY=PATH` | Load variable values from a file (repeatable) |
| `-e, --env KEY VALUE` | Set an environment variable in the container (repeatable) |
| `-t, --tag KEY VALUE` | Tag the run (repeatable) |
| `--visibility` | Set the visibility dynamically (public/private/unlisted) |
| `--timeout` | Change the timeout dynamically (in seconds) |
| `--expire` | Expiration for the run |
| `--cpu` | Change the cpu dynamically (run only) |
| `--memory` | Change the memory dynamically (run only) |
| `--image` | Specify a custom Docker image (run only) |
| `-r, --region-filter REGION` | Restrict the execution to certain regions (repeatable) |
| `--repo GithubUser/Repo` | Run the playbook on the latest commit of a Github repository (creates a 1-commit scan, run only) |
| `--count` | Number of executions for the run (default: 1, run only) |
| `--delete-report` | Do not keep the report once the run finishes |
| `--delete-output` | Do not keep the output once the run finishes |
| `--save-report` | **Deprecated**: use `--delete-report` instead |
| `--save-output` | **Deprecated**: use `--delete-output` instead |
| `--json` | Print the raw JSON response |
| `--test` | Limit the output to a certain test *(on development)* |
| `--run` | Execute a specific test from the playbook *(on development)* |
| `--name` | Change the name of the playbook dynamically *(on development)* |
| `--storage` | Change the storage dynamically in GB (run only) *(on development)* |
| `--os` | Set the operating system (windows or linux, run only) *(on development)* |
| `--format` | Set output format (plain or md) *(on development)* |
| `--redacted` | Mark parameters as redacted in logs (repeatable) *(on development)* |
| `-i, --include` | Include additional files in execution (repeatable) *(on development)* |
| `--clone` | Clone settings from another report ID *(on development)* |
| `--rate` | Create monitor with rate expression (e.g., "every 5 minutes", run only) *(on development)*. In v2 set `rate` in the playbook `settings:`; `run` creates the monitor automatically |
| `--cron` | Create monitor with cron schedule (e.g., "0 * * * *", run only) *(on development)*. In v2 set `cron` in the playbook `settings:`; `run` creates the monitor automatically |

## Run parametrized playbooks

| Command | Description |
| --- | --- |
| `--data VAR="This is the value of VAR"` | Provide values for the undefined playbook variables |
| `--data VAR="a,b,c" --split VAR=,` | Provide several values for VAR by splitting on a delimiter |

## Playbooks

| Command | Description |
| --- | --- |
| `satori-v2 playbooks` | List the public playbooks catalog |
| `satori-v2 playbooks --json` | List the playbooks as JSON |
| `satori-v2 playbooks --public` | List the public playbooks *(on development)* |
| `satori-v2 playbook satori://...` | Show a certain public playbook |
| `satori-v2 playbook EXECUTION_ID` | Show the public playbook used by an execution |
| `satori-v2 playbook ID visibility {public, private, unlisted}` | Toggles the playbook's visibility *(on development)* |

## Dashboards

| Command | Description |
| --- | --- |
| `satori-v2` | Show your general dashboard (latest jobs) |
| `satori-v2 --public` | Show the latest public jobs |
| `satori-v2 jobs` | List your jobs (runs, scans, monitors, CI and local executions) |
| `satori-v2 job ID` | Show a job and its last 5 executions |
| `satori-v2 team TEAM` | Show your TEAM dashboard *(on development)* |

## Jobs

| Command | Description |
| --- | --- |
| `satori-v2 jobs` | List your jobs |
| `satori-v2 jobs --public` | List public jobs |
| `satori-v2 jobs --page N -q N` | Paginate the job list |
| `satori-v2 jobs --json` | List your jobs as JSON |
| `satori-v2 job ID` | Show the job ID and its last 5 executions |

## Executions & Output

Every job (run, scan, monitor, CI or local) produces one or more executions. `report ID` and `execution get ID` refer to the same execution ID.

| Command | Description |
| --- | --- |
| `satori-v2 execution get ID` | Show the execution ID |
| `satori-v2 execution list` | List executions as JSON |
| `satori-v2 execution list --job-id ID` | List the executions of a job |
| `satori-v2 execution list --job-type {RUN\|SCAN\|MONITOR\|GITHUB\|LOCAL}` | List the executions of a job type |
| `satori-v2 execution output ID` | Show the output of the execution ID |
| `satori-v2 execution output ID --test TEST_NAME` | Filter specific test output (repeatable) |
| `satori-v2 execution output ID --format {json\|md}` | Show output in specified format |
| `satori-v2 execution files ID` | Download the files created by the execution |
| `satori-v2 execution stop ID` | Stop the execution ID |
| `satori-v2 execution delete ID` | Delete the execution ID |
| `satori-v2 output ID` | Show the output of the execution ID |
| `satori-v2 output ID --raw` | Pipe the encoded results to stdout |
| `satori-v2 output ID --test TEST_NAME` | Filter specific test output (repeatable) |
| `satori-v2 output ID --format {json\|md}` | Show output in specified format |

## Stop

| Command | Description |
| --- | --- |
| `satori-v2 stop run ID` | Stop the run ID |
| `satori-v2 stop all` | Stop all your queued and running runs |

## Reports

| Command | Description |
| --- | --- |
| `satori-v2 reports` | List reports |
| `satori-v2 reports JOB-ID` | List the reports of a job |
| `satori-v2 reports --status {FINISHED\|CANCELED\|RUNNING\|QUEUED}` | List reports with a certain status |
| `satori-v2 reports --public` | List public reports |
| `satori-v2 reports --page N -q N` | Paginate the report list |
| `satori-v2 reports search [FILTERS]` | Search reports using the filters below |
| `satori-v2 reports download [FILTERS] -n PATH` | Download the outputs of the FINISHED reports that match the filters |
| `satori-v2 reports stop [FILTERS]` | Stop the RUNNING reports that match the filters |
| `satori-v2 reports delete [FILTERS]` | Delete the FINISHED and CANCELED reports that match the filters |
| `satori-v2 report ID` | Show the report ID |
| `satori-v2 report ID --json` | Show the JSON of the report ID |
| `satori-v2 report ID output` | Show the output of the report ID |
| `satori-v2 report ID output --json` | Show the JSON's output of the report ID |
| `satori-v2 report ID output --format {json\|md}` | Show output in specified format |
| `satori-v2 report ID output --test TEST_NAME` | Filter specific test output (repeatable) |
| `satori-v2 report ID files` | Download the files created (if Files was set to True in settings) |
| `satori-v2 report ID visibility {public, private, unlisted}` | Toggles the report's visibility |
| `satori-v2 report ID issues` | List the issues of the report ID |
| `satori-v2 report ID delete` | Delete the report ID |
| `satori-v2 report ID --unredacted` | Show unredacted parameters and secrets *(on development)* |
| `satori-v2 report ID issue TEMPLATE_ID` | Create GitHub issue from report *(on development)* |
| `satori-v2 report ID issue TEMPLATE_ID --query "SEARCH"` | Create issue with search query filter *(on development)* |
| `satori-v2 report ID issue TEMPLATE_ID --title "TITLE"` | Create issue with custom title *(on development)* |
| `satori-v2 report ID stop` | Stop the current report execution *(on development)*. Use `satori-v2 execution stop ID` |
| `satori-v2 report ID status` | Get report status *(on development)*. Use `satori-v2 report ID` |
| `satori-v2 report ID set-team TEAM_NAME` | Assign report to team *(on development)* |

### Report filters

Available on `reports search`, `reports download`, `reports stop`, `reports delete` and `search`:

| Filter | Description |
| --- | --- |
| `--job-type {RUN\|SCAN\|MONITOR\|GITHUB\|LOCAL}` | Filter by job type |
| `--job-id ID` | Filter by job |
| `--global` | Search across all reports, not only yours |
| `--status {FINISHED\|CANCELED\|RUNNING\|QUEUED}` | Filter by execution status (repeatable) |
| `--visibility {PUBLIC\|PRIVATE\|UNLISTED}` | Filter by visibility |
| `--from DATETIME` / `--to DATETIME` | Filter by date (ISO 8601) |
| `--report-status {PASS\|FAIL}` | Filter by report result |
| `--severity N` | Filter by severity (0 to 5) |
| `--playbook URI` | Filter by playbook |
| `--q TEXT` | Free text search |
| `-t, --tag TAG` | Filter by tag (repeatable) |
| `--page N`, `-q N` | Pagination |
| `--repo`, `--result`, `--monitor`, `--execution`, `--playbook-type` | v1 filters *(on development)* |

## Search

| Command | Description |
| --- | --- |
| `satori-v2 search [FILTERS]` | Search reports using the [report filters](#report-filters) |
| `satori-v2 search [FILTERS] --download PATH` | Download the outputs of the matching FINISHED reports to PATH |
| `satori-v2 search [FILTERS] --reports PATH` | Download the matching reports as JSON to PATH |
| `satori-v2 search [FILTERS] --stop` | Stop the matching RUNNING reports |
| `satori-v2 search [FILTERS] --delete` | Delete the matching FINISHED and CANCELED reports (asks for confirmation) |

`--download`, `--reports`, `--stop` and `--delete` are mutually exclusive.

## Findings & Issues

| Command | Description |
| --- | --- |
| `satori-v2 issues` | List your issues (sorted by severity) |
| `satori-v2 issues EXECUTION-ID` | List the issues of an execution |
| `satori-v2 issues --execution-id ID` | Same as the positional `EXECUTION-ID` |
| `satori-v2 issues --status {OPEN\|INVESTIGATING\|CONFIRMED\|FIXED\|FALSE_POSITIVE\|ACCEPTED_RISK}` | Filter issues by status |
| `satori-v2 issues --source {ASSERT\|TOOL}` | Filter issues by source |
| `satori-v2 issues --severity N` | Filter issues by severity (0 to 5) |
| `satori-v2 issues --order {ASC\|DESC}` | Order the issues (disables the default severity sort) |
| `satori-v2 issues --page N -q N --json` | Pagination and JSON output |
| `satori-v2 report ID issues` | List the issues of the report ID |
| `satori-v2 issue FINDING-ID` | Show the issue FINDING-ID |
| `satori-v2 issue FINDING-ID status {OPEN\|INVESTIGATING\|CONFIRMED\|FIXED\|FALSE_POSITIVE\|ACCEPTED_RISK}` | Set the issue status |
| `satori-v2 issue FINDING-ID advisory` | Create an external advisory for the issue and print its URL |
| `satori-v2 advisories` | List external issues (e.g. GitHub security advisories) you created |
| `satori-v2 advisories --execution-id ID` | List external issues for an execution |
| `satori-v2 advisories --kind {SECURITY_ADVISORY\|ISSUE}` | Filter by kind |
| `satori-v2 advisories --provider GITHUB` | Filter by provider |
| `satori-v2 advisories --order {ASC\|DESC}` | Order the list |
| `satori-v2 advisories --page N -q N --json` | Pagination and JSON output |
| `satori-v2 advisory ADVISORY-ID` | Show the external issue ADVISORY-ID |
| `satori-v2 advisory ADVISORY-ID --json` | Show the external issue as JSON |
| `satori-v2 advisory ADVISORY-ID visibility {PUBLIC\|PRIVATE\|UNLISTED}` | Set the external issue visibility |

## Repos

| Command | Description |
| --- | --- |
| `satori-v2 repos` | List the repositories connected to CI or tested |
| `satori-v2 repos --order {ASC\|DESC}` | Order the repository list |
| `satori-v2 repos --page N -q N --json` | Pagination and JSON output |
| `satori-v2 run PLAYBOOK --repo GithubUser/Repo` | Run a playbook on the latest commit of the repository (v2 equivalent of `repo X run`) |
| `satori-v2 run PLAYBOOK --repo GithubUser/Repo -d KEY=value` | Provide parameters/secrets to the repository run |
| `satori-v2 run PLAYBOOK --repo GithubUser/Repo --sync --output --report` | Wait for the run and display its output and report |
| `satori-v2 scan GithubUser/Repo PLAYBOOK -q N` | Run a playbook on the last N commits of the repository (see [Scans](#scans)) |
| `satori-v2 repo GithubUser/Repo` | Shows the repository Visibility, CI, Playbook, Status, Result and its team *(on development)* |
| `satori-v2 repo GithubUser/Repo --pending` | Show pending actions in repo info *(on development)* |
| `satori-v2 repo GithubUser/Repo run` | Run the repository's playbook on the latest commit *(on development)* |
| `satori-v2 repo GithubUser/Repo run --playbook="satori://..."` | Run another playbook on the latest commit *(on development)* |
| `satori-v2 repo GithubUser/Repo run -b BRANCH` | Run on specific branch (default: main) *(on development)* |
| `satori-v2 repo GithubUser/Repo run -d '{"KEY":"value"}'` | Provide secrets/parameters as JSON *(on development)* |
| `satori-v2 repo GithubUser/Repo run -s --sync` | Wait for run to complete *(on development)* |
| `satori-v2 repo GithubUser/Repo run -o --output` | Display command output *(on development)* |
| `satori-v2 repo GithubUser/Repo run -r --report` | Display test results *(on development)* |
| `satori-v2 repo GithubUser/Repo run --visibility {public\|private\|unlisted}` | Set run visibility *(on development)* |
| `satori-v2 repo GithubUser/Repo commits` | Show the list of commits and the reports associated *(on development)* |
| `satori-v2 repo GithubUser/Repo tests` | List test results *(on development)* |
| `satori-v2 repo GithubUser/Repo tests -a --all` | Show all test results *(on development)* |
| `satori-v2 repo GithubUser/Repo tests -l LIMIT` | Limit number of results (default: 100) *(on development)* |
| `satori-v2 repo GithubUser/Repo tests --fail` | Show only failed tests *(on development)* |
| `satori-v2 repo GithubUser/Repo playbook list` | List playbooks for repository *(on development)* |
| `satori-v2 repo GithubUser/Repo playbook add URI` | Add playbook to repository *(on development)* |
| `satori-v2 repo GithubUser/Repo playbook del URI` | Remove playbook from repository *(on development)* |
| `satori-v2 repo GithubUser/Repo visibility {public, private, unlisted}` | Toggles the repo's visibility *(on development)* |
| `satori-v2 repo GithubUser/Repo params` | List parameters/secrets for the repository *(on development)* |
| `satori-v2 repo GithubUser/Repo params add 'NAME=VALUE'` | Add a parameter/secret to the repository *(on development)* |
| `satori-v2 repo GithubUser/Repo params del NAME` | Delete a parameter/secret from the repository *(on development)* |

## Monitors

Monitors are created with `satori-v2 run` when the playbook has `cron`, `rate` or `monitor` in its `settings:`.

| Command | Description |
| --- | --- |
| `satori-v2 monitors` | List monitors |
| `satori-v2 monitors --public` | List public monitors |
| `satori-v2 monitors --page N -q N --json` | Pagination and JSON output |
| `satori-v2 monitors --pending` | List monitors with pending actions *(on development)* |
| `satori-v2 monitor ID` | Show the monitor ID |
| `satori-v2 monitor ID start` | Start a monitor ID |
| `satori-v2 monitor ID pause` | Pause a monitor ID |
| `satori-v2 monitor ID cancel` | Cancel a monitor ID |
| `satori-v2 monitor ID stop` | Alias of `cancel` |
| `satori-v2 monitor ID clean` | Delete the reports associated to the monitor ID |
| `satori-v2 monitor ID delete` | Delete the monitor ID |
| `satori-v2 monitor ID visibility {public, private, unlisted}` | Toggles the monitor's visibility |
| `satori-v2 reports ID` | List the reports associated to a monitor ID |

## Scans

| Command | Description |
| --- | --- |
| `satori-v2 scans` | List scans |
| `satori-v2 scans --public` | List public scans |
| `satori-v2 scans --page N -q N --json` | Pagination and JSON output |
| `satori-v2 scan GithubUser/Repo playbook.yml` | Scan the Github repository with a local playbook (directory sources are not allowed) |
| `satori-v2 scan GithubUser/Repo --playbook="satori://..."` | Scan the Github repository with a public playbook |
| `satori-v2 scan GithubUser/Repo SOURCE -q N` | Scan the last N commits of the repository (replaces v1 `-c`) |
| `satori-v2 scan GithubUser/Repo SOURCE -d KEY=value` | Provide parameters and values |
| `satori-v2 scan GithubUser/Repo SOURCE --split KEY=DELIMITER` | Split a parameter value into several values |
| `satori-v2 scan GithubUser/Repo SOURCE -df KEY=PATH` | Load variable values from a file |
| `satori-v2 scan GithubUser/Repo SOURCE -e KEY VALUE` | Set an environment variable in the container |
| `satori-v2 scan GithubUser/Repo SOURCE -s --sync` | Wait for scan to complete |
| `satori-v2 scan GithubUser/Repo SOURCE -r REGION` | Restrict the execution to certain regions (repeatable) |
| `satori-v2 scan GithubUser/Repo SOURCE --cpu N --memory N --image IMAGE` | Override the container settings |
| `satori-v2 scan GithubUser/Repo SOURCE --visibility {public\|private\|unlisted}` | Set scan visibility |
| `satori-v2 scan GithubUser/Repo SOURCE --json` | Print the raw JSON response |
| `satori-v2 scan GithubUser/Repo [-c N]` | Scan with the repository's playbook a coverage of 1 to 100 *(on development)*. Use `-q N` with an explicit playbook |
| `satori-v2 scan GithubUser/Repo -b BRANCH` | Scan specific branch (default: main) *(on development)* |
| `satori-v2 scan GithubUser/Repo --from YYYY-MM-DD` | Start date for scanning *(on development)* |
| `satori-v2 scan GithubUser/Repo --to YYYY-MM-DD` | End date for scanning *(on development)* |
| `satori-v2 scan GithubUser/Repo --skip-check` | Skip repository existence check *(on development)* |
| `satori-v2 scan GithubUser/Repo -o --output` | Display command output *(on development)* |
| `satori-v2 scan GithubUser/Repo -r --report` | Display test results *(on development)*. In v2 `-r` is `--region-filter` |
| `satori-v2 scan GithubUser/Repo check-commits` | Get the repository commits before scanning *(on development)* |
| `satori-v2 scan GithubUser/Repo check-forks` | Get the repository forks before scanning *(on development)* |
| `satori-v2 scan ID` | Show scan information |
| `satori-v2 scan ID status` | Show the status of a scan |
| `satori-v2 scan ID stop` | Stop the scan |
| `satori-v2 scan ID clean` | Delete the reports associated to the scan |
| `satori-v2 scan ID delete` | Delete the scan |
| `satori-v2 reports ID` | List the reports associated to a scan ID |
| `satori-v2 scan ID reports` | List the reports associated to a scan *(on development)*. Use `satori-v2 reports ID` |
| `satori-v2 scan ID reports -p PAGE` | Show specific page of reports *(on development)*. Use `satori-v2 reports ID --page PAGE` |
| `satori-v2 scan ID reports -l LIMIT` | Set number of results per page (default: 20) *(on development)*. Use `satori-v2 reports ID -q LIMIT` |
| `satori-v2 scan ID clean --delete-commits` | Delete reports and commit records *(on development)* |
| `satori-v2 scan ID visibility {public, private, unlisted}` | Toggles the scan's visibility *(on development)* |

## Shell

| Command | Description |
| --- | --- |
| `satori-v2 shell` | Launch an interactive remote shell container |
| `satori-v2 shell EXECUTION-ID` | Open a shell on the container of a running execution |
| `satori-v2 shell --image IMAGE` | Use a specific Docker image |
| `satori-v2 shell --cpu CPU` | Set CPU allocation (AWS Fargate) |
| `satori-v2 shell --memory MEMORY` | Set memory allocation (AWS Fargate) |
| `satori-v2 shell -r REGION, --region-filter REGION` | Select AWS region (repeatable) |
| `satori-v2 shell sessions` | List your shell sessions (replaces v1 `shells`) |
| `satori-v2 shell sessions --page N -q N --json` | Pagination and JSON output |
| `satori-v2 shell --timeout SECONDS` | Set session duration limit *(on development)* |

## Teams

| Command | Description |
| --- | --- |
| `satori-v2 teams` | List your teams *(on development)* |
| `satori-v2 team TEAM` | Show the TEAM dashboard *(on development)* |
| `satori-v2 team TEAM create` | Create a new team named TEAM *(on development)* |
| `satori-v2 team TEAM members` | List your TEAM members *(on development)* |
| `satori-v2 team TEAM monitors` | List your TEAM monitors *(on development)* |
| `satori-v2 team TEAM repos` | List your TEAM repositories *(on development)* |
| `satori-v2 team TEAM reports` | List your TEAM reports *(on development)* |
| `satori-v2 team TEAM settings` | List your TEAM settings *(on development)* |
| `satori-v2 team TEAM get_config NAME` | Show your TEAM's config setting *(on development)* |
| `satori-v2 team TEAM set_config NAME VALUE` | Set your TEAM CONFIG setting *(on development)* |
| `satori-v2 team TEAM add --github="GithubUser"` | Owners and admins can add users via Github to the TEAM *(on development)* |
| `--role="READ"` | Use the role READ (default) or ADMIN *(on development)* |
| `satori-v2 team TEAM add --email="usr@example.com"` | Owners and admins can add users via Email to the TEAM *(on development)* |
| `--role="READ"` | Use the role READ (default) or ADMIN *(on development)* |
| `satori-v2 team TEAM add --monitor="MONITORID"` | Add the monitor ID to your TEAM *(on development)* |
| `satori-v2 team TEAM add --repo="GithubUser/repo"` | Add the repo to your TEAM *(on development)* |
| `satori-v2 team TEAM del --github="GithubUser"` | Delete the GithubUser from your TEAM *(on development)* |
| `satori-v2 team TEAM del --email="usr@example.com"` | Delete the email from the TEAM *(on development)* |
| `satori-v2 team TEAM del --repo="GithubUser/repo"` | Delete the repo from the TEAM *(on development)* |
| `satori-v2 team TEAM del --monitor="MONITORID"` | Delete the monitor from the TEAM *(on development)* |
| `satori-v2 team TEAM delete` | Delete the TEAM *(on development)* |

Team tokens can still be used in v2 through profiles: `satori-v2 config token "TEAMTOKEN" --profile TEAM` and `SATORI_PROFILE=TEAM`.

## Shards

| Command | Description |
| --- | --- |
| `satori-v2 shards --shard X/Y --input INPUT` | Divide massive datasets into smaller chunks for distributed processing |
| `--shard X/Y` | Shard index X out of Y total shards (required) |
| `--input INPUT` | Input file path or direct IP/CIDR/range/domain/URL (required) |
| `--exclude PATH or ENTRY` | Exclusion file path or direct IP/CIDR/range/domain/URL to exclude |
| `--seed N` | Seed for deterministic pseudorandom distribution (default: 1) |
| `--results PATH` | Output file path (writes to stdout if omitted) |

## Notifications

| Command | Description |
| --- | --- |
| `satori-v2 settings` | Interactive menu to configure notification settings (Slack, Discord, Email, Telegram, Datadog) *(on development)* |
| `satori-v2 settings KEY` | View current value of a notification setting *(on development)* |
| `satori-v2 settings KEY VALUE` | Set a notification setting directly *(on development)* |
| `satori-v2 settings --team TEAM` | Configure notifications for a specific team *(on development)* |
| `satori-v2 team TEAM settings` | Alias for configuring team notifications interactively *(on development)* |
