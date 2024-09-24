# Settings

Your playbook will have metadata associated with it, including specific CPU and memory requirements.  It may need to run at a certain rate or schedule.  It may require a general timeout to run concurrently several times or destroy the output upon execution. Here is how you can define it.

## Name, Description and Mitigation Settings

You can define your playbook name to easily identify it, along with a description and a mitigation for deeper follow ups:

```yaml
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


## Change the amount of CPUs and Memory

You can set the CPU and Memory required for playbooks like this:

```
settings:
  cpu: 16384
  memory: 122880
```

These are the possible combinations you can use:

| CPU value      | Memory value                                                                                                                                                                                              | Operating systems supported |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- |
| 256 (.25 vCPU) | 512<br>1024<br>2048                                                                                                                                                                                       | Linux                       |
| 512 (.5 vCPU)  | 1024<br>2048<br>3072<br>4096                                                                                                                                                                              | Linux                       |
| 1024 (1 vCPU)  | 2048<br>3072<br>4096<br>5120<br>6144<br>7168<br>8192                                                                                                                                                      | Linux, Windows              |
| 2048 (2 vCPU)  | 4096<br>5120<br>6144<br>7168<br>8192<br>9216<br>10240<br>11264<br>12288<br>13312<br>14336<br>15360<br>16384                                                                                               | Linux, Windows              |
| 4096 (4 vCPU)  | 8192<br>9216<br>10240<br>11264<br>12288<br>13312<br>14336<br>15360<br>16384<br>17408<br>18432<br>19456<br>20480<br>21504<br>22528<br>23552<br>24576<br>25600<br>26624<br>27648<br>28672<br>29696<br>30720 | Linux, Windows              |
| 8192 (8 vCPU)  | 16384<br>20480<br>24576<br>28672<br>32768<br>36864<br>40960<br>45056<br>49152<br>53248<br>57344<br>61440                                                                                                  | Linux                       |
| 16384 (16vCPU) | 32768<br>40960<br>49152<br>57344<br>65536<br>73728<br>81920<br>90112<br>98304<br>106496<br>114688<br>122880                                                                                               | Linux                       |
## Cron Settings

For detailed information on how to use Cron settings in your playbooks, please refer to the CRON Scheduling section in the [Monitor](../modes/monitor.md#cron-scheduling) documentation.

## Rate Settings

For information on how to use Rate settings in your playbooks, please see the Rate Setting section in the [Monitor](../modes/monitor.md#rate-setting) documentation.

## Alert your result every time a execution runs or when the expected result is different than the one expected

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

Different log types can be specified simultaneously to notify people in different ways:

```yaml
settings:
    #log: slack-logs
    logOnFail: slack-fails
    #logOnPass: email-auditor
```

## Timeout Settings

You can define a maximum amount of time in seconds that the execution should run for:

```yaml
settings:
    timeout: 60 # the default value is 3600 seconds
```

In case it reaches the timeout without completing, the instance will be shutdown killing current executions.

## Count Settings

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

## Report Settings

You may not want to store any data on Satori servers after the execution has been completed. You can set that by defining the report as False. On the other hand, if you want to receive a copy of your report, you can specify in what format you would like to receive it. If you don't define anything for your report, you will still be able it to see it online with the CLI or the Web. 

### Report PDF

Send yourself a PDF version of our report with this setting when receiving along with the notification, we can save you a click:

```yaml
settings:
    report: pdf
```

### Report False

If you don't want to store a copy of your report or output, define the report as False. You will still get the overall status of your report and test after completion but the outputs will not be stored.

```yml
settings:
  report: False
```

If you need any help, please reach out to us on [Discord](https://discord.gg/NJHQ4MwYtt) or via [Email](mailto:support@satori-ci.com)
