# Programmatic CI

With file-based CI (GitHub, GitLab, Jenkins), you commit a `.satori.yml` file into your repository to define what tests run. Programmatic CI takes a different approach: you assign playbooks to repositories from the outside using CLI commands, without modifying the repository's code.

This is useful when you:

- Want to enforce the same security checks across **all** your repositories.
- Need to assign tests to a repository you don't have write access to.
- Manage many repositories and prefer centralized control over what tests run.
- Want to add tests without going through a pull request or code review process.

## Global playbooks

Global playbooks run on **every** repository connected to your account. This is ideal for organization-wide policies like secret detection or license compliance.

```sh
# List global playbooks
satori repos playbook list

# Add a playbook that runs on all repos
satori repos playbook add satori://secrets/semgrep.yml

# Remove a global playbook
satori repos playbook del satori://secrets/semgrep.yml
```

## Per-repo playbooks

Per-repo playbooks are assigned to a **specific** repository. Use this when different repos need different tests.

```sh
# List playbooks assigned to a repo
satori repo satorici/satori-cli playbook list

# Add a playbook to a specific repo
satori repo satorici/satori-cli playbook add satori://code/yamllint.yml

# Remove a playbook from a repo
satori repo satorici/satori-cli playbook del satori://code/yamllint.yml
```

## When to use each approach

| Approach | Defined in | Best for |
| --- | --- | --- |
| File-based CI (`.satori.yml`) | Inside the repository | Tests tightly coupled to the repo's code |
| Programmatic CI (global) | CLI / dashboard | Organization-wide policies across all repos |
| Programmatic CI (per-repo) | CLI / dashboard | Assigning specific tests to specific repos externally |

Global and per-repo playbooks can be combined with each other and with a `.satori.yml` file in the same repository. All assigned playbooks will run on each push.
