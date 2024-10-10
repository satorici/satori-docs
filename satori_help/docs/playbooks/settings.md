# Settings

In your playbook, you can set specific settings to define its execution requirements. These settings allow you to:

- Specify CPU and memory requirements.

- Set execution rate or schedule.

- Define a general timeout and concurrency.

- Manage output handling.

These settings help customize the playbook performance to your project’s needs, making testing processes more efficient and scalable.

## Name, Description and Mitigation Settings

In your playbook, you can define a name, description, and mitigation strategy to enhance playbook identification. Here’s how each component contributes to a clear and actionable setup:

**- Name:** assign a descriptive name to identify the playbook quickly.

**- Description:** provide details about the playbook's purpose, such as supported languages and tool functionalities. 

**- Mitigation:** specify a remediation step if the playbook fails, it provides clear guidance for necessary actions upon failure.

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

Associating this metadata with each playbook run provides valuable context and supports informed follow-up actions, especially if mitigation measures are necessary.

## Configuring CPU and Memory for Playbooks

Define the required CPU and memory for each playbook to ensure optimal performance. Use the `settings` to specify these parameters:

```yml
settings:
  cpu: 16384
  memory: 122880
```
These are the possible combinations of CPU and memory configurations and the compatible operating systems. Select the values that best suit your playbook's requirements.

| CPU value      | Memory value                                                                                                                                                                                              | Operating systems supported |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- |
| 256 (.25 vCPU) | 512<br>1024<br>2048                                                                                                                                                                                       | Linux                       |
| 512 (.5 vCPU)  | 1024<br>2048<br>3072<br>4096                                                                                                                                                                              | Linux                       |
| 1024 (1 vCPU)  | 2048<br>3072<br>4096<br>5120<br>6144<br>7168<br>8192                                                                                                                                                      | Linux, Windows              |
| 2048 (2 vCPU)  | 4096<br>5120<br>6144<br>7168<br>8192<br>9216<br>10240<br>11264<br>12288<br>13312<br>14336<br>15360<br>16384                                                                                               | Linux, Windows              |
| 4096 (4 vCPU)  | 8192<br>9216<br>10240<br>11264<br>12288<br>13312<br>14336<br>15360<br>16384<br>17408<br>18432<br>19456<br>20480<br>21504<br>22528<br>23552<br>24576<br>25600<br>26624<br>27648<br>28672<br>29696<br>30720 | Linux, Windows              |
| 8192 (8 vCPU)  | 16384<br>20480<br>24576<br>28672<br>32768<br>36864<br>40960<br>45056<br>49152<br>53248<br>57344<br>61440                                                                                                  | Linux                       |
| 16384 (16vCPU) | 32768<br>40960<br>49152<br>57344<br>65536<br>73728<br>81920<br>90112<br>98304<br>106496<br>114688<br>122880                                                                                               | Linux                       |

## Scheduling Playbooks with Cron and Rate settings

To schedule playbook execution based on specific times or intervals, configure Cron or Rate settings. Each offers a different approach to scheduling:

**- Cron Settings:** use cron settings to schedule playbooks at precise times or recurring intervals, such as daily or weekly runs. For more detailed instructions, refer to the Cron Scheduling section in the [Monitor](../modes/monitor.md#cron-scheduling) documentation.

**- Rate Settings:** configure rate settings for simple, fixed-interval scheduling, such as every 5 minutes or hourly. See the rate setting section in the [Monitor](../modes/monitor.md#rate-setting) documentation for guidance.

These settings help automate playbook runs, ensuring timely and consistent execution based on your testing needs.

## Notification settings for execution results

You can customize how you receive notifications based on the execution results of your playbook. Choose from three notification settings:

- **log**: receive notifications for every execution, regardless of the outcome.
- **logOnFail**: get notified only when the result is a failure.
- **logOnPass**: receive notifications only when the result is a success.

Notifications can be sent through various channels. Use the following formats to define your notification preferences:

- **slack** followed by the alias you defined for the Slack channel.
- **email** followed by the email you defined for email notifications.
- **telegram** followed by the alias you defined for the Telegram channel.
- **discord** followed by the alias you defined for the Discord channel.

You can define these aliases in your [Settings](https://satori.ci/dashboard/) when adding a notification.

You can specify different log types simultaneously to notify users through multiple channels:

```yaml
settings:
    logOnFail: slack, email, telegram, discord
```
## Timeout Settings

Set a maximum runtime for playbook executions to control resource usage. Specify the timeout duration in seconds:

```yaml
settings:
    timeout: 60 # the default value is 3600 seconds
```
If the playbook reaches the defined timeout without completing, the instance will automatically shut down, terminating any ongoing processes. This setting helps prevent excessive resource use and ensures timely task completion.

## Count Settings

The `count` parameter allows you to launch multiple instances of the same playbook concurrently through the Satori Cloud infrastructure. Each instance runs independently and generates its own report, which is especially useful for tests requiring high concurrency, such as load or DDoS testing. Here’s an example configuration for a DDoS test playbook:

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
  - [ curl -s ${(URL}} -m 3 ]
  siege:
  - [ siege -c 100 -t 30s $(URL) ]
  results:
  - [ "set +f; cat siege.*" ]
  after_siege:
  - [ curl -s ${{URL}} -m 3 ]
```

## Report Settings

Control whether and how reports are saved after playbook execution. You can prevent data storage on Satori servers or specify a format to receive a downloadable copy.

**- Disable report storage:** set `report` to `false` to avoid storing any report data on Satori servers, while still receiving an execution summary upon completion.

**- Receive a report copy in PDF:** set `report` to `pdf` to receive a PDF copy of the report.

If no report format is specified, you can still access the report online using the CLI or Web interface.

### Example Configurations

- **PDF report**: sends a downloadable PDF version of your report.
    ```yaml
    settings:
        report: pdf
    ```

- **No report storage**: ensures no report data is saved on Satori servers after execution. You will still get the overall status of your report and test after completion but the outputs will not be stored.
    ```yaml
    settings:
        report: False
    ```

If you need any help, please reach out to us on [Discord](https://discord.gg/NJHQ4MwYtt) or via [Email](mailto:support@satori-ci.com)
