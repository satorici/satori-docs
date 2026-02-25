# Satori CI CLI Cheatsheet

## Install, Update and Configure

| Command | Description |
| --- | --- |
| `pip3 install satori-ci` | Install the latest version |
| `satori update` | Update to the latest version |
| `satori config token "USERTOKEN"` | Configure your user token as your default profile |
| `satori config token "TEAMTOKEN" --profile TEAM` | Configure your team token on your team profile |
| `satori whoami` | Display current user information |
| `satori width` | Show console width configuration for current profile |

## Run in the cloud

| Command | Description |
| --- | --- |
| `satori run ./` | Upload the current dir and run the playbook .satori.yml |
| `satori run playbook.yml` | Upload the playbook and run it |
| `satori run ./ --playbook="satori://..."` | Upload the current dir and run the specified playbook |

## Run locally

| Command | Description |
| --- | --- |
| `satori local ./` | Execute the playbook .satori.yml locally |
| `satori local playbook.yml` | Execute the playbook locally |
| `satori local ./ --playbook="satori://..."` | Execute the specified playbook locally |

## Local execution parameters

| Parameter | Description |
| --- | --- |
| `--sync` | Show summary when execution completes |
| `--report` | Display test assertions and results |
| `--output` | Display command output |
| `--test` | Filter specific test output (repeatable) |
| `--run` | Run specific tests only (repeatable) |
| `--timeout` | Execution timeout in seconds |
| `--name` | Name for this run |
| `--visibility` | Set report visibility (public/private/unlisted) |
| `--format` | Output format (plain or md) |
| `--redacted` | Mark parameters as redacted (repeatable) |
| `-df, --data-file` | Load variable values from file (repeatable) |
| `--save-report` | Save report to file (true/false or path) |
| `--save-output` | Save command output to file (true/false or path) |

## Run using these parameters

| Parameter | Description |
| --- | --- |
| `--sync` | Show the result |
| `--report` | Show the report |
| `--output` | Show the output |
| `--test` | Limit the output to a certain test|
| `--files` | Download the files created if the setting files was set to True |
| `--run` | Execute a specific test from the playbook |
| `--visibility` | Set the visibility dynamically (public/private/unlisted) |
| `--name` | Change the name of the playbook dynamically |
| `--timeout` | Change the timeout dynamically (in seconds) |
| `--cpu` | Change the cpu dynamically (run only) |
| `--memory` | Change the memory dynamically (run only) |
| `--storage` | Change the storage dynamically in GB (run only) |
| `--os` | Set the operating system (windows or linux, run only) |
| `--image` | Specify a custom Docker image (run only) |
| `--format` | Set output format (plain or md) |
| `--redacted` | Mark parameters as redacted in logs (repeatable) |
| `-i, --include` | Include additional files in execution (repeatable) |
| `-df, --data-file` | Load variable values from file (repeatable) |
| `--save-report` | Save report to file (true/false or path) |
| `--save-output` | Save command output to file (true/false or path) |
| `--clone` | Clone settings from another report ID |
| `--repo` | Specify repository URL to scan (run only) |
| `--rate` | Create monitor with rate expression (e.g., "every 5 minutes", run only) |
| `--cron` | Create monitor with cron schedule (e.g., "0 * * * *", run only) |
| `--count` | Number of executions for monitor (run only) |

## Run parametrized playbooks

| Command | Description |
| --- | --- |
| `--data VAR="This is the value of VAR"` | Provide values for the undefined playbook variables |

## Playbooks

| Command | Description |
| --- | --- |
| `satori playbooks` | List your private playbooks |
| `satori playbooks --public` | List the public playbooks |
| `satori playbook ID` | Show a certain playbook |
| `satori playbook ID visibility {public, private, unlisted}` | Toggles the playbook's visibility |

## Dashboards

| Command | Description |
| --- | --- |
| `satori` | Show your general dashboard |
| `satori team TEAM` | Show your TEAM dashboard |

## Reports

| Command | Description |
| --- | --- |
| `satori reports` | List reports |
| `satori report ID` | Show the report ID |
| `satori report ID --json` | Show the JSON of the report ID |
| `satori report ID output` | Show the output of the report ID |
| `satori report ID output --json` | Show the JSON's output of the report ID |
| `satori report ID output --format {plain\|md}` | Show output in specified format |
| `satori report ID output --test TEST_NAME` | Filter specific test output (repeatable) |
| `satori report ID --unredacted` | Show unredacted parameters and secrets |
| `satori report ID files` | Download the files created (if Files was set to True in settings) |
| `satori report ID visibility {public, private, unlisted}` | Toggles the report's visibility |
| `satori report ID issue TEMPLATE_ID` | Create GitHub issue from report |
| `satori report ID issue TEMPLATE_ID --query "SEARCH"` | Create issue with search query filter |
| `satori report ID issue TEMPLATE_ID --title "TITLE"` | Create issue with custom title |
| `satori report ID stop` | Stop the current report execution |
| `satori report ID delete` | Delete the report ID |
| `satori report ID status` | Get report status |
| `satori report ID set-team TEAM_NAME` | Assign report to team |

## Repos

| Command | Description |
| --- | --- |
| `satori repos` | List the repositories connected to CI or tested |
| `satori repo GithubUser/Repo` | Shows the repository Visibility, CI, Playbook, Status, Result and its team. |
| `satori repo GithubUser/Repo --pending` | Show pending actions in repo info |
| `satori repo GithubUser/Repo run` | Run the repository's playbook on the latest commit |
| `satori repo GithubUser/Repo run --playbook="satori://..."` | Run another playbook on the latest commit |
| `satori repo GithubUser/Repo run -b BRANCH` | Run on specific branch (default: main) |
| `satori repo GithubUser/Repo run -d '{"KEY":"value"}'` | Provide secrets/parameters as JSON |
| `satori repo GithubUser/Repo run -s --sync` | Wait for run to complete |
| `satori repo GithubUser/Repo run -o --output` | Display command output |
| `satori repo GithubUser/Repo run -r --report` | Display test results |
| `satori repo GithubUser/Repo run --visibility {public\|private\|unlisted}` | Set run visibility |
| `satori repo GithubUser/Repo commits` | Show the list of commits and the reports associated |
| `satori repo GithubUser/Repo tests` | List test results |
| `satori repo GithubUser/Repo tests -a --all` | Show all test results |
| `satori repo GithubUser/Repo tests -l LIMIT` | Limit number of results (default: 100) |
| `satori repo GithubUser/Repo tests --fail` | Show only failed tests |
| `satori repo GithubUser/Repo playbook list` | List playbooks for repository |
| `satori repo GithubUser/Repo playbook add URI` | Add playbook to repository |
| `satori repo GithubUser/Repo playbook del URI` | Remove playbook from repository |
| `satori repo GithubUser/Repo visibility {public, private, unlisted}` | Toggles the repo's visibility |
| `satori repo GithubUser/Repo params` | List parameters/secrets for the repository |
| `satori repo GithubUser/Repo params add 'NAME=VALUE'` | Add a parameter/secret to the repository |
| `satori repo GithubUser/Repo params del NAME` | Delete a parameter/secret from the repository |

## Monitors

| Command | Description |
| --- | --- |
| `satori monitors` | List monitors |
| `satori monitor ID` | List the reports associated to a monitor ID |
| `satori monitor ID stop` | Stop a monitor ID |
| `satori monitor ID start` | Start a monitor ID |
| `satori monitor ID clean` | Delete the reports associated to the monitor ID |
| `satori monitor ID delete` | Delete the monitor ID |
| `satori monitor ID visibility {public, private, unlisted}` | Toggles the monitor's visibility |

## Scans

| Command | Description |
| --- | --- |
| `satori scans` | List scans |
| `satori scan GithubUser/Repo [-c N]` | Scan the Github repository with the repository's playbook a coverage of 1 (default) to 100 |
| `satori scan GithubUser/Repo [--playbook="satori://..."]` | Scan the Github repository with a different playbook |
| `satori scan GithubUser/Repo -b BRANCH` | Scan specific branch (default: main) |
| `satori scan GithubUser/Repo -d '{"KEY":"value"}'` | Provide secrets/parameters as JSON |
| `satori scan GithubUser/Repo --from YYYY-MM-DD` | Start date for scanning |
| `satori scan GithubUser/Repo --to YYYY-MM-DD` | End date for scanning |
| `satori scan GithubUser/Repo --skip-check` | Skip repository existence check |
| `satori scan GithubUser/Repo -s --sync` | Wait for scan to complete |
| `satori scan GithubUser/Repo -o --output` | Display command output |
| `satori scan GithubUser/Repo -r --report` | Display test results |
| `satori scan GithubUser/Repo --visibility {public\|private\|unlisted}` | Set scan visibility |
| `satori scan GithubUser/Repo check-commits` | Get the repository commits before scanning |
| `satori scan GithubUser/Repo check-forks` | Get the repository forks before scanning |
| `satori scan ID` | Show scan information |
| `satori scan ID status` | Show the status of a scan |
| `satori scan ID reports` | List the reports associated to a scan |
| `satori scan ID reports -p PAGE` | Show specific page of reports |
| `satori scan ID reports -l LIMIT` | Set number of results per page (default: 20) |
| `satori scan ID stop` | Stop the scan |
| `satori scan ID clean` | Delete the reports associated to the scan |
| `satori scan ID clean --delete-commits` | Delete reports and commit records |
| `satori scan ID delete` | Delete the scan |
| `satori scan ID visibility {public, private, unlisted}` | Toggles the scan's visibility |

## Teams

| Command | Description |
| --- | --- |
| `satori teams` | List your teams |
| `satori team TEAM` | Show the TEAM dashboard |
| `satori team TEAM create` | Create a new team named TEAM |
| `satori team TEAM members` | List your TEAM members |
| `satori team TEAM monitors` | List your TEAM monitors |
| `satori team TEAM repos` | List your TEAM repositories |
| `satori team TEAM reports` | List your TEAM reports |
| `satori team TEAM settings` | List your TEAM settings |
| `satori team TEAM get_config NAME` | Show your TEAM's config setting |
| `satori team TEAM set_config NAME VALUE` | Set your TEAM CONFIG setting |
| `satori team TEAM add --github="GithubUser"` | Owners and admins can add users via Github to the TEAM |
| `--role="READ"` | Use the role READ (default) or ADMIN |
| `satori team TEAM add --email="usr@example.com"` | Owners and admins can add users via Email to the TEAM |
| `--role="READ"` | Use the role READ (default) or ADMIN |
| `satori team TEAM add --monitor="MONITORID"` | Add the monitor ID to your TEAM |
| `satori team TEAM add --repo="GithubUser/repo"` | Add the repo to your TEAM |
| `satori team TEAM del --github="GithubUser"` | Delete the GithubUser from your TEAM |
| `satori team TEAM del --email="usr@example.com"` | Delete the email from the TEAM |
| `satori team TEAM del --repo="GithubUser/repo"` | Delete the repo from the TEAM |
| `satori team TEAM del --monitor="MONITORID"` | Delete the monitor from the TEAM |
| `satori team TEAM delete` | Delete the TEAM |

## Shards

| Command | Description |
| --- | --- |
| `satori shards --shard X/Y --input INPUT` | Divide massive datasets into smaller chunks for distributed processing |
| `--shard X/Y` | Shard index X out of Y total shards (required) |
| `--input INPUT` | Input file path or direct IP/CIDR/range/domain/URL (required) |
| `--exclude PATH or ENTRY` | Exclusion file path or direct IP/CIDR/range/domain/URL to exclude |
| `--seed N` | Seed for deterministic pseudorandom distribution (default: 1) |
| `--results PATH` | Output file path (writes to stdout if omitted) |

## Notifications

| Command | Description |
| --- | --- |
| `satori settings` | Interactive menu to configure notification settings (Slack, Discord, Email, Telegram, Datadog) |
| `satori settings KEY` | View current value of a notification setting |
| `satori settings KEY VALUE` | Set a notification setting directly |
| `satori settings --team TEAM` | Configure notifications for a specific team |
| `satori team TEAM settings` | Alias for configuring team notifications interactively |
