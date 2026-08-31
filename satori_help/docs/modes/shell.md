# Shell

The `satori shell` command launches an interactive remote shell inside a container. This is useful for exploring an environment, debugging a playbook, or trying out commands before adding them to a playbook.

## Launch a Shell

```sh
satori shell
```

This starts a remote container and connects you to an interactive session over SSH.

## Options

You can customize the container running your session:

| Flag | Description | Example |
| --- | --- | --- |
| `--image IMAGE` | Docker image for the container | `satori shell --image debian` |
| `--cpu CPU` | CPU allocation (AWS Fargate) | `satori shell --cpu 512` |
| `--memory MEMORY` | Memory allocation (AWS Fargate) | `satori shell --memory 1024` |
| `--region REGION` | AWS region (repeatable) | `satori shell --region us-east-1` |
| `--timeout SECONDS` | Session duration limit in seconds | `satori shell --timeout 600` |

Example combining several options:

```sh
satori shell --image debian --cpu 512 --memory 1024 --timeout 600
```

## List Shell Sessions

You can list your shell sessions with:

```sh
satori shells
```

Pagination is supported with the following flags:

| Flag | Description | Example |
| --- | --- | --- |
| `-q, --quantity NUMBER` | Number of sessions per page (default: 10) | `satori shells -q 20` |
| `-p, --page NUMBER` | Show a specific page of results | `satori shells -p 2` |
