# [Intro](README.md)
## Repo

Satori provides automatic testing for repositories, in particular when they are connected to our [GitHub Application](https://github.com/apps/satorici). At the same time, we also have the possibility of testing repositories that are not connected to your CI, but that you have access to.

Whenever you want to check the status of your repositories, the Satori CLI repo command can assist you. It will execute the `.satori.yml` playbook within your repo unless you are using public playbooks (you can list them with `satori-cli playbook --public`)

### List

List all your repositories
- `satori-cli repo`

### Show

Shows if the repository is connected to CI, if it has a valid playbook and the last results of its execution (including any potential errors that could have been found during the execution of the playbook)
- `satori-cli repo githubUsername/repository`

### Run

**Repository Playbook**

Run the .satori.yml playbook on the latest commit of the repository:
- `satori-cli repo githubUsername/repository run`

**Public Playbook**

Public playbooks can be listed with the command `satori-cli playbook --public`. They are public predefined tests by Satori that are hosted on https://github.com/satorici/playbooks/, which is replaced by the short URI form `satori://`. 

For example, you can run the public playbook satori://some/playbook.yml (equivalent to https://github.com/satorici/playbooks/some/playbook.yml):
- `satori-cli repo githubUsername/repository run --playbook satori://some/playbook.yml`: 

**Run on Multiple Repositories**

Trufflehog is a piece of software that finds secrets stored in code. You can run the Trufflehog playbook to test all the repositories of a certain given account. For example:
- `satori-cli repo githubUsername/* run --playbook satori://code/trufflehog.yml`

**Commit**

Run the repository's playbook on a specific commit (in whatever branch you want):
- `satori-cli repo https://github.com/satorici/satori-cli/commit/96a654f9efb8962b20a514eccbe827518ca725b2 run`

### Scan

Whenever you want to run an execution on each of the individual commits of a repository, you can use the scan functionality. 

#### Single Commit

On its most simple form, you can scan a single commit using the following approach:

`satori-cli repo https://github.com/satorici/satori-cli/commit/226f19d5eb0e2dd1bd6449f452c8e7e725c04c00 run`

#### Multiple Commits

If you target a repo, the optional parameter `-c` is used to indicate the percentage of repository commits to include in the scan. For example, if you only want to just take a sample, when not using the `-c` parameter, is the equivalent to `-c 1` "scan 1% of the repository commits". This is useful for sampling large repositories:

- `satori-cli repo githubUsername/repository scan`

If you however want to be sure that everything was tested, you can target full scan coverage on all the repository commits, you would:
- `satori-cli repo githubUsername/repository scan -c 100`


The previous command, initially starts by checking which are the repository commits for the repo. The task can be individually launched without the scan if you wish:
- `satori-cli repo githubUsername/repository check-commits`

You can also request the list of forks associated to the repo. Again, the task can be launched with check-forks:
- `satori-cli repo githubUsername/repository check-forks`

You can see how the results of your playbook affect different commits and forks of your repository.

#### Multiple Repos

Scan repositories of a GitHub account for secrets
```sh
satori-cli repo mercadolibre/* run --playbook satori://code/trufflehog.yml
```

#### Status

Since normally repositories have a lot of commits, you may want to check what is the execution status with this command:
- `satori-cli repo githubUsername/repository scan-status`

The scan status output will look like this:
```sh
% satori-cli repo satorici/satori-cli scan-status
Satori CI 1.2.25 - Automated Software Testing Platform 
▢ status: Stopped
▢ commits: 281
▢ commits scanned: 273
▢ commits being scanned: 0
▢ commits scheduled to be scanned: 0
▢ progress: None
```

It shows the current status, the amount of commits found, which ones were scanned, which ones are being scanned and which ones are scheduled to be scanned. Since no scan is being run at the time of executing this command, there is no progress but in other cases it would be a percentage.

#### Stop

If at any point you want to cancel the scan, you use the `scan-stop` action:
- `satori-cli repo githubUsername/repository scan-stop`

#### Clean

Warning: this commmand will delete all the reports associated to a certain repository:
- `satori-cli repo githubUsername/repository clean`

You may want to do this when analyzing your repo with a different playbook.