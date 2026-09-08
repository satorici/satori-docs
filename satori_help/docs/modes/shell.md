# Shell

The `satori-v2 shell` command launches an interactive remote shell inside a container. This is useful for exploring an environment, debugging a playbook, or trying out commands before adding them to a playbook.

## Launch a Shell

```sh
satori-v2 shell
```

This starts a remote container and connects you to an interactive session over SSH.

## Attach to a Running Execution

You can also open a shell **inside the container of an execution that is currently running**, which is handy to inspect the environment of a playbook while it runs:

```sh
satori-v2 shell EXECUTION-ID
```

The execution ID is the one shown by `satori-v2 run`, `satori-v2 reports` or `satori-v2 report ID`. The container options below do not apply in this case, since the container already exists.

## Options

You can customize the container running your session:

| Flag | Description | Example |
| --- | --- | --- |
| `--image IMAGE` | Docker image for the container | `satori-v2 shell --image debian` |
| `--cpu CPU` | CPU allocation (AWS Fargate) | `satori-v2 shell --cpu 512` |
| `--memory MEMORY` | Memory allocation (AWS Fargate) | `satori-v2 shell --memory 1024` |
| `-r, --region-filter REGION` | Region where the container is started (repeatable). Replaces the v1 `--region` flag | `satori-v2 shell -r us-east-1` |

Example combining several options:

```sh
satori-v2 shell --image debian --cpu 512 --memory 1024 -r us-east-1
```

::: warning On development
`--timeout` (session duration limit) and the old `--region` spelling are not available yet in CLI v2. The v1 syntax is kept here for reference.
:::

| Flag | Description | Example |
| --- | --- | --- |
| `--region REGION` | AWS region (repeatable) *(renamed to `-r/--region-filter`)* | `satori-v2 shell --region us-east-1` |
| `--timeout SECONDS` | Session duration limit in seconds *(on development)* | `satori-v2 shell --timeout 600` |

```sh
satori-v2 shell --image debian --cpu 512 --memory 1024 --timeout 600
```

## List Shell Sessions

You can list your shell sessions with:

```sh
satori-v2 shell sessions
```

Pagination and output flags:

| Flag | Description | Example |
| --- | --- | --- |
| `-q, --quantity NUMBER` | Number of sessions per page (default: 10). `-l/--limit` is an alias | `satori-v2 shell sessions -q 20` |
| `--page NUMBER` | Show a specific page of results | `satori-v2 shell sessions --page 2` |
| `--json` | Print the list as JSON | `satori-v2 shell sessions --json` |

::: warning On development
The v1 command `satori-v2 shells` has been renamed to `satori-v2 shell sessions` in CLI v2, and its `-p` short flag for `--page` is not available. The v1 syntax is kept here for reference.
:::

```sh
satori-v2 shells
satori-v2 shells -q 20
satori-v2 shells -p 2
```
