# Scan

Whenever you want to run an execution on each of the individual commits of a repository, you can use the scan functionality.

## Multiple Commits

If you target a repo, the optional parameter `-c` is used to indicate the percentage of repository commits to include in the scan. For example, if you only want to just take a sample, when not using the `-c` parameter, is the equivalent to `-c 1` "scan 1% of the repository commits". This is useful for sampling large repositories:

```
satori scan githubUsername/repository
```

![Scan Repo](img/scan_1.png)


If you however want to be sure that everything was tested, you can target full scan coverage on all the repository commits, you would:

```
satori scan githubUsername/repository -c 100
```

You can see how the results of your playbook affect different commits and forks of your repository.

## Status

Since normally repositories have a lot of commits, you may want to check what is the execution status with this command:

```
satori scan githubUsername/repository status`
```

![Scan Repo](img/scan_2.png)

It shows the current status, the amount of commits found, which ones were scanned, which ones are being scanned and which ones are scheduled to be scanned. Since no scan is being run at the time of executing this command, there is no progress but in other cases it would be a percentage.

## Stop

If at any point you want to cancel the scan, you use the `stop` action:

```
satori scan githubUsername/repository stop
```

![Stop Scan Repo](img/scan_3.png)

## Clean

Warning: this commmand will delete all the reports associated to a certain repository:

```
satori scan githubUsername/repository clean
```

![Clean Scan Repo](img/scan_4.png)