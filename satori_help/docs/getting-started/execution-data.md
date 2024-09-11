# Playbook results

Satori-CI is an automated testing platform that executes Playbooks to validate conditions. After a Playbook is run, the platform generates a report indicating the result of the test, we deliver a report either a *Pass* or *Fail*.

You can view and manage your test reports using either the command line interface or on the web.

## Listing Reports

To list all your reports from the command line, use the following command:

```sh
satori reports
```

![CLI Reports](img/execution-data_1.png)

You can also view your reports on the Satori-CI website at:

[https://satori.ci/reports/](https://satori.ci/reports/)

![Web Reports](img/execution-data_2.png)

Both methods allow you to obtain the report IDs, which you can use to view single report.

### Filtering Reports

You can filter your reports using various parameters to narrow down the results:

- **`repo`**: filter by repository (e.g., satorici/satori-cli).
- **`playbook`**: filter by Playbook URL (e.g., satori://code/semgrep.yml).
- **`status`**: filter by report status (Pending, Running, Completed, or Undefined).
- **`result`**: filter by report result (Pass or Fail).
- **`from`**: limit to commits from a specific date (format: year-month-day, e.g., 2020-12-30).
- **`to`**: limit to commits until a specific date (format: year-month-day, e.g., 2023-01-10).
- **`satori_error`**: filter by whether an error occurred during report generation (True or False).
- **`email`**: filter by pusher email.
- **`user`**: filter by Satori-CI user name.
- **`type`**: filter by report execution type (monitor, github, or playbook_bundle).

This parameters can be used to check and filter specific reports that you are looking for.

- Example: _"I want to see all failed reports for the repositories of the account satorici"_

```sh
satori reports --filter="repo=satorici/*,result=fail"
```

- Example: *"I want to see a list of reports related to the playbook trufflehog"*

```sh
satori reports --filter="playbook=satori://code/trufflehog"
```

#### Pagination

When dealing with a large number of results, such as reports, repositories, or monitors, we provide a pagination system to help you navigate through the data more efficiently. To access additional pages, use the `-p X` option, where `X` represents the page number you want to view.

```sh
satori reports -p 2
```

### Viewing a Single Report

To view a specific report, specify the report ID as follows:

```yml
satori report REPORT_ID
```

![CLI Report](img/execution-data_3.png)

Or on the web:

![Web Report](img/execution-data_4.png)

## Command output

This displays a summary of the execution data along with the command output and assertions applied.

```yml
satori report REPORT_ID output
```

Or on the web:

![Web Report](img/execution-data_5.png)

## Downloading Files

If your execution generates files, you can download them using the CLI:

```yml
satori report REPORT_ID files
```
