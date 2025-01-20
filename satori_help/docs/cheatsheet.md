# Satori CI CLI Cheatsheet

## Install, Update and Configure

| Command | Description |
| --- | --- |
| `pip3 install satori-ci` | Install the latest version |
| `satori update` | Update to the latest version |
| `satori config token "USERTOKEN"` | Configure your user token as your default profile |
| `satori config token "TEAMTOKEN" --profile TEAM` | Configure your team token on your team profile |

## Run asynchronously

| Command | Description |
| --- | --- |
| `satori run ./` | Upload the current dir and run the playbook .satori.yml |
| `satori run playbook.yml` | Upload the playbook and run it |
| `satori run ./ --playbook="satori://..."` | Upload the current dir and run the specified playbook |

## Run synchronously using these parameters

| Parameter | Description |
| --- | --- |
| `--sync` | Show the result |
| `--report` | Show the report |
| `--output` | Show the output |
| `--files` | Download the files created if the setting files was set to True |

## Run playbooks with variables

| Command | Description |
| --- | --- |
| `--data VAR="This is the value of VAR"` | Provide values for the undefined playbook variables |

## Playbooks

| Command | Description |
| --- | --- |
| `satori playbooks` | List your private playbooks |
| `satori playbooks --public` | List the public playbooks |
| `satori playbook ID` | Show a certain playbook |
| `satori playbook ID public` | Toggles the playbook's visibility |
| `satori playbook ID delete` | Delete the playbook |

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
| `satori report ID files` | Download the files created (if Files was set to True in settings) |
| `satori report ID public` | Toggles the report's visibility |
| `satori report ID stop` | Stop the current report execution |
| `satori report ID delete` | Delete the report ID |

## Repos

| Command | Description |
| --- | --- |
| `satori repos` | List the repositories connected to CI or tested |
| `satori repo GithubUser/Repo` | Shows the repository Visibility, CI, Playbook, Status, Result and its team. |
| `satori repo GithubUser/Repo run` | Run the repository's playbook on the latest commit |
| `satori repo GithubUser/Repo run --playbook="satori://..."` | Run another playbook on the latest commit |
| `satori repo GithubUser/Repo commits` | Show the list of commits and the reports associated |

## Monitors

| Command | Description |
| --- | --- |
| `satori monitors` | List monitors |
| `satori monitor ID` | List the reports associated to a monitor ID |
| `satori monitor ID stop` | Stop a monitor ID |
| `satori monitor ID start` | Start a monitor ID |
| `satori monitor ID clean` | Delete the reports associated to the monitor ID |
| `satori monitor ID delete` | Delete the monitor ID |
| `satori monitor ID public` | Toggles the monitor's visibility |

## Scans

| Command | Description |
| --- | --- |
| `satori scans` | List scans |
| `satori scan GithubUser/Repo [-c N]` | Scan the Github repository with the repository's playbook a coverage of 1 (default) to 100 |
| `satori scan GithubUser/Repo [--playbook="satori://..."]` | Scan the Github repository with a different playbook |
| `satori scan GithubUser/Repo check-commits` | Get the repository commits before scanning |
| `satori scan GithubUser/Repo check-forks` | Get the repository forks before scanning |
| `satori scan ID status` | Show the status of a scan |
| `satori scan ID stop` | Stop the scan |
| `satori scan ID start` | Start a previously stopped scan on the repo |
| `satori scan ID clean` | Delete the reports associated to the repo |
| `satori scan ID delete` | Delete the monitor |
| `satori scan ID public` | Toggle the monitor's visibility |

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