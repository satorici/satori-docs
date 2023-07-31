# [Intro](README.md)
## Playbook


### Private playbooks

Your previously executed playbooks can be retrieved with the command:

```sh
$ satori-cli playbook
```

That will present you with the list of playbooks that you previously executed. If you want to get more information about any of them, you just request it like this:

```sh
$ satori-cli playbook ID
```

And eventually if you want to remove any of your playbooks, you can do so with:

```sh
$ satori-cli playbook ID delete
```

### Public playbooks

Public playbooks can be seen on the command line with:
```sh
$ satori-cli playbook --public
```

The playbooks listed in there are publicly available in here https://github.com/satorici/playbooks . They can also be individually retrieved with:

```sh
$ satori-cli playbook satori://code/semgrep.yml
```
