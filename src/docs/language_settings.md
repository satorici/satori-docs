# [Intro](README.md)
## [Language](language.md)
### Settings

There are several settings that can be applied to your Satori CI playbooks to better define the information and conditions that need to be met by your test. They can only be defined for the root playbook, not within imported playbooks.

#### Name, Description, Mitigation

You can define your playbook name to easily identify it, along with a description and a mitigation for deeper follow ups:

```yml
settings:
    name: Find Secrets using Semgrep
    description: A free open-source static code analysis tool with stable support for C#, Go, Java, JavaScript, JSON, Python, PHP, Ruby, and Scala. It has experimental support for nineteen other languages, as well as a language agnostic mode.
    mitigation: Remove secrets from your code if the playbook fails
install:
    assertReturnCode: 0
    semgrep:
    - [ python3 -m pip install semgrep ]
semgrep:
    assertStdout: False
    secrets:
    - [ semgrep --config "p/secrets" -q ]
```

Having this information associated to the playbook's execution is valuable for context and follow up on the understanding of the situation and the potential following actions required in case it fails and a mitigation is required.

#### Cron

If you define a cron schedule for a playbook, it will execute with the defined frequency:

```yml
settings:
    cron: 5 8 * * 0 # Run this playbook every Sunday at 8:05am
```

As another example, this playbook runs an nmap every 10 minutes and notifies in case the expected result output changes:

```yml
settings:
    name: "Nmap: did any service changed?"
    cron: "*/10 * * * *"
    logOnFail: telegram-ciso
    mitigation: Verify the latest Pass execution to confirm what services changed their status
install:
    assertReturnCode:0
    nmap:
    - [ apt install -y nmap]
    ips:
    - [ "echo -e \"host1\nhost2\" > domains"]
nmap:
    assertReturnCode:0 
    run:
    - [ "nmap -n -iL domains -Pn -p21,22,80,443,3000,3306,5432 -sT -oG nmap" ]
    services: 
        # The SHA256 hash "e3b0c4..." of the `running` execution represents the expected working state of the `ips`'s ports. In case it changes, it means that there are more open or closed ports than expected. This value needs to be verified first for the output before putting this on a production environment.
        assertStdoutSHA256:
        - "e3b0c44298fc1c149afbf4c7996fb92427ae41e4649b934ca495991b7852b855"
        running:
        - [ "grep Ports nmap | sort -u" ]
```

For more details on the `assertReturnCode` and `assertStdoutSHA256` please check the [asserts](language_asserts.md) section and for more details on the `nmap`, `ips` and `running` [executions](language_execution.md) please check the corresponding section.

For more details on the logOnFail, please check the [notifications](notifications.md) section.

#### Rate

Another terminology that may be easier than `cron` is the `rate` setting. You can define a time lapse such as `30 minutes` or 

**Rate expression examples**:

|Frequency	       | Expression       |
|------------------|------------------|
| Every 10 minutes | rate: 10 minutes |
| Every hour       | rate: 1 hour     |
| Every seven days | rate: 7 days     |

For example:

```yml
settings:
    rate: 10 minutes
```

#### Log

You can choose between the three different results and how you would like to be notified once the execution is complete. These are your options:

- **log**: Always be notified
- **logOnFail**: Be notified in case the result is Fail
- **logOnPass**: Be notified in case the result is Pass

Which can be used with the following parameters:
- **slack-** followed by the alias that you defined for the channel
- **email-** followed by the alias that you defined for the channel
- **telegram-** followed by the alias that you defined for the channel
- **discord-name** followed by the alias that you defined for the channel
- **issue** to create a github issue on the project, which does not require a suffix to be added since it will be created on the project repository (only valid for CI)

The previous aliases can be defined on your [Team Settings](https://www.satori-ci.com/team-settings/) when adding a notification

Different log types can be specified simultaneously to notify people on different ways:

```yml
settings:
    #log: slack-logs
    logOnFail: slack-fails
    #logOnPass: email-auditor
```

#### Timeout

You can define a maximum amount of time in seconds that the execution should run for:

```yml
settings:
    timeout: 60 # the default value is 3600 seconds
```

In case it reaches the timeout without completing, the instance will be shutdown killing current executions.

#### Count

Multiple instances can be launched independently by the Satori Cloud infrastructure in parallel using the same playbook with the count parameters and the number of instances with each execution having its own report. Consider the following case of a playbook that performs a DDoS test:

```yml
settings:
  name: "Siege - Load testing web servers"
  description: "Knowing how much traffic your web server can handle when under stress is essential for planning 
                future grow of your website or application. By using tool called siege, you can run a load test 
                on your server and see how your system performs under different circumstances."
  mitigation: "Use an anti DDoS service such as CloudFlare to prevent network attacks"
  count: 100 # maximum amount of concurrent instances for a playbook
install:
  assertReturnCode: 0
  siege:
  - [ apt install -y siege ]
host:
  assertReturnCode: 0
  before_siege:
  - [ curl -s $(URL) -m 3 ]
  siege:
  - [ siege -c 100 -t 30s $(URL) ]
  results:
  - [ "set +f; cat siege.*" ]
  after_siege:
  - [ curl -s $(URL) -m 3 ]
```

#### Report

Do you want to save yourself a click? Send a PDF version of our report with this setting:

```yml
settings:
    report: pdf
```

If you need any help, please reach out to us on [Discord](https://discord.gg/F6Uzz7fc2s) or via [Email](mailto:support@satori-ci.com)
