# Language

Playbooks are the core configuration files that define the settings, executions, inputs, and assertions for testing procedures. These files use the **YAML** syntax, and all Playbooks are saved with the `.yml` file extension.


## Key Components of a Playbook

- **Settings**: configuration details that determine the environment and parameters for the tests.
- **Executions**: the actual commands or scripts that are run as part of the test process.
- **Inputs**: data or parameters required by the tests to execute properly.
- **Assertions**: Conditions or checkpoints used to validate if the software or system behaves as expected.

## Reserved Words

Certain words in the Satori playbook language are reserved for special operations:

Within **settings**, all these words are reserved:
- **`name`**: specifies the name of the Playbook.
- **`description`**: provides a description of the Playbook.
- **`mitigation`**: describes how to address potential risks.
- **`cron`** or **`rate`**: defines the frequency for remote monitoring.
- **`timeout`**: sets the maximum time allowed before the Playbook is terminated.
- **`cpu`**: indicates the number of CPU units to be allocated remotely.
- **`memory`**: specifies the amount of RAM to be used remotely.
- **`storage`**: defines the amount of storage required remotely.

Within a **test**, you may define:
- **`assert*`**: a category of keywords used for asserting conditions. Examples include `assertStdoutEquals`, `assertStdoutNotEquals`, etc.
- **`setSeverity`**: Defines the severity level of the test.

## [Execution](execution.md)

To execute a program named `HelloWorld`, you can define in a Playbook as follows:

```yml
Hello_World_Test:
- HelloWorld.exe
```

## [Asserts](asserts.md)

Asserts are used to validate the output or behavior of a program after execution. For example, if you want to verify that the output contains the text "Hello World", you can add an assert statement to the parent test as shown below:

```yml
Hello_World_Test:
  assertStdoutContains: "Hello World"
  run:
  - HelloWorld.exe
```

## [Input](inputs.md)

Inputs are used to provide parameters to the programs being executed, allowing you to test the same program with various input values. This helps in verifying how the program handles different scenarios.

```yml
Hello_World_Test:
  assertStdoutContains: "Hello World"
  who:
  - - "Foo"
    - "World"
  run:
  - HelloWorld.exe ${{who}}
```

## [Settings](settings.md)

Playbooks allow you to configure various settings to customize test execution and management. Settings can include naming tests, configuring notifications and more

```yml
settings:
  name: "Tests hello world with parameters"
  timeout: 60 # no more than 60 seconds should be required
  logOnFail: slack

Hello_World_Test:
  assertStdoutContains: "Hello World"
  who:
  - - "Foo"
    - "World"
  run:
  - HelloWorld.exe ${{who}}
```

## Imports

Imports allow you to include other Playbooks into your own, enabling you to leverage existing tests or configurations. You can import both public Playbooks and local files. 

```yml
import:
  - satori://some/public/playbook.yml
  - file://some/local/playbook.yml

Hello_World_Test:
  assertStdoutContains: "Hello World"
  who:
  - - "Foo"
    - "World"
  run:
  - HelloWorld.exe ${{who}}
```

The `import` keyword is not mandatory. You can place the import section anywhere in your YAML file, as long as it adheres to valid YAML syntax.

## Errors

Satori performs schema validation on your Playbook as soon as it is received, ensuring that the syntax and grammar are correct. If any errors are detected, either from user input or system issues, you will be promptly informed.
The error will be shown when viewing your report with `satori report REPORTID` command or from the **Reports** section of the Satori Web.

---
If you need any help, please reach out to us on [Discord](https://discord.gg/NJHQ4MwYtt) or via [Email](mailto:support@satori-ci.com)
