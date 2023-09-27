# Running playbooks

Now you have your shinny new playbook but how to make it do something? We present you two ways to do it.

## CLI

```bash
satori run shinny-playbook.yml
```

You can explore more functions in the CLI reference but here are some highlights. By running the previous command your playbook will be submitted and runned asynchroically, but if you use `--sync`, `--report`, `--output` or `--files` it'll run in sync mode, the last three will also show additional data accordingly.

For example `--output` will display each command output: stdout, stderr, return code, etc.

## CI

You can have a playbook named `.satori.yml` in the root of your GitHub repository. If you have the GitHub App installed, in each push the playbook will be run against the repository contents.

See more about that in [GitHub CI](../modes/ci/github.md)

For more ways to run your playbooks visit the [execution modes](../modes/modes.md) section.
