# [Intro](README.md)
## Monitor

Monitors are playbooks that contain either a `cron` or a `rate` setting in the `settings` section. They are specially useful to assert that the behavior of live systems is working as expected with a certain frequency.

### Rate

This is the easiest way of speaking of frequency:

**Rate expression examples**:

|Frequency             | Expression       |
|------------------|------------------|
| Every 10 minutes | rate: 10 minutes |
| Every hour       | rate: 1 hour     |
| Every seven days | rate: 7 days     |

For example, the following file `monitor.yml` checks that the Satori's website is live and showing its name every 10 minutes:

```yml
settings:
    name: "Verify Satori's website"
    rate: 10 minutes

test:
    assertStdoutContains: "Satori CI"
    curl:
    - [ curl -s http://www.satori-ci.com ]
```

To install this playbook, you just need to run it:

```sh
$ satori-cli run monitor.yml 
```

### Cron

As a more advanced example, consider the following example playbook that runs nmap every 10 minutes to identify any services that may have changed their port status. We check the SHA256 hash of what is the expected output of the port status:

```yml
settings:
    name: "Nmap: did any service changed?"
    cron: "*/10 * * * *"
    logOnFail: slack
install:
    assertReturnCode: 0
    nmap:
    - [ apt install -y nmap ]
nmap:
    assertReturnCode: 0
    run:
    - [ "nmap -n 1.1.1.1/24 -Pn -p 21,22,23,80,443 -sT -oG nmap" ]
services:
    assertStdoutSHA256:
    - "d34db33f93ac1c149afbf4c8996fb924271e41e4649b933ca495991b7852b854"
    running:
    - [ "grep Ports nmap | sort -u" ]
```

To install this playbook, you just need to run it:

```sh
$ satori-cli run nmap-cron.yml 
```

### List your monitors

Once you have added a monitor, you can list them with the `monitor` command like this:

```sh
$ satori-cli monitor
```

**Stop Monitor**
Now, besides listing your monitors, you may want to stop them. - 

```sh
$ satori-cli monitor ID stop`: disable the monitor id
```

**Start Monitor**

You can start again your monitors when they are stopped by doing:

```sh
$ satori-cli monitor ID run
```

**Delete Monitor**

Delete a monitor id that is on a stopped state:
```sh
$ satori-cli monitor id delete
```

If you need any help, please reach out to us on [Discord](https://discord.gg/F6Uzz7fc2s) or via [Email](mailto:support@satori-ci.com)
