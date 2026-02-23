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

## Filtering Reports

You can filter your reports using various parameters to narrow down the results with `satori reports search`:

- **`playbook-type`**: filter by playbook type {public,private}
- **`visibility`**: filter by report visibility {public-global,public,unlisted,private}
- **`result`**: filter by report result {pass,fail,unknown}
- **`query`**: filter by output string (supports regex)      
- **`monitor`**: filter by monitor ID
- **`playbook`**: filter by playbook
- **`status`**: filter by status {provisioning,pending,running,completed,stopped,timeout}
- **`from`**: filter by from date
- **`to`**: filter by to date
- **`severity`**: filter by output severity
- **`execution`**: filter by execution type {local,run,ci,scan,monitor}

These parameters can be used to check and filter specific reports that you are looking for.

- Example: _"I want to see all failed reports for the repositories of the account satorici"_

```sh
satori reports search --repo "satorici/*" --result fail
```

- Example: *"I want to see a list of reports related to the playbook trufflehog"*

```sh
satori reports search --playbook satori://code/trufflehog
```

## Pagination

When dealing with a large number of results, such as reports, repositories, or monitors, we provide a pagination system to help you navigate through the data more efficiently. To access additional pages, use the `-p X` option, where `X` represents the page number you want to view.

```sh
satori reports -p 2
```

## Viewing a Single Report

To view a specific report, specify the report ID as follows:

```sh
satori report REPORT_ID
```

![CLI Report](img/execution-data_3.png)

Or on the web:

![Web Report](img/execution-data_4.png)

## Command output

This displays a summary of the execution data along with the command output and assertions applied.

```sh
satori report REPORT_ID output
```

Or on the web:

![Web Report](img/execution-data_5.png)

## Configuring Report Visibility

You can configure the visibility of your results report with three distinct settings to manage who can view it:

- **`private`**: accessible only to the owner or specifically permitted users.
- **`unlisted`**: accessible only to individuals with a direct link to the report. This visibility is useful for sharing specific results without making them publicly.
- **`public`**: open access, visible to all users without restrictions.

To set the visibility of a report, use the following command and specify the visibility level:

```sh
satori report REPORT_ID visibility [private|unlisted|public]
```
These configurations provide flexible control over report access, allowing you to choose the visibility level that best suits your sharing needs.

## Downloading Files

If your execution generates files, you can download them using the CLI:

```sh
satori report REPORT_ID files
```

---

## Advanced Report Command Options

The `satori report` command provides several options for viewing and managing execution results.

### Output Formatting

| Flag | Description | Example |
| --- | --- | --- |
| `--format {plain\|md}` | Set output format (plain text or Markdown) | `satori report ID output --format md` |
| `--test TEST_NAME` | Filter output for specific test (repeatable) | `satori report ID output --test my_test` |
| `--unredacted` | Show unredacted parameters and secrets | `satori report ID --unredacted` |

### GitHub Issue Creation

Create GitHub issues directly from report results:

| Flag | Description | Example |
| --- | --- | --- |
| `issue TEMPLATE_ID` | Create issue using template | `satori report ID issue template_123` |
| `--query "SEARCH"` | Filter with search query | `satori report ID issue template_123 --query "critical"` |
| `--title "TITLE"` | Override issue title | `satori report ID issue template_123 --title "Security Issue"` |

### Report Management

| Command | Description | Example |
| --- | --- | --- |
| `status` | Get report execution status | `satori report ID status` |
| `stop` | Stop running report | `satori report ID stop` |
| `delete` | Delete report | `satori report ID delete` |
| `set-team TEAM` | Assign report to team | `satori report ID set-team my_team` |

### Complete Examples

**View report output in Markdown format:**

```sh
satori report AOQxDWDkXpZp output --format md
```

**View specific test output with unredacted secrets:**

```sh
satori report AOQxDWDkXpZp output --test integration_test --unredacted
```

**Create GitHub issue from report:**

```sh
satori report AOQxDWDkXpZp issue template_123 \
  --query "severity:critical" \
  --title "Critical Security Vulnerability Found"
```

**Filter multiple tests:**

```sh
satori report AOQxDWDkXpZp output \
  --test unit_tests \
  --test integration_tests \
  --format md
```

These advanced options give you fine-grained control over how you view and share execution results.
