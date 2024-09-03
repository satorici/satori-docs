# Language

Playbooks store the settings, executions, inputs and assertions associated with the testing procedures. These files have a YAML syntax and use the ".yml" file extension.

## Reserved Words

Certain words in the Satori playbook language are reserved for special operations:

Within **settings**, all these words are reserved:
- **name**: the playbook name
- **description**: a description of the playbook
- **mitigation**: how to mitigate the risk
- **cron** or **rate**: the frequency at which it should be monitored remotely
- **timeout**: when to kill the playbook
- **cpu**: how many CPU units should be used remotely?
- **memory**: how much RAM should be used remotely?
- **storage**: how much storage is required remotely?

Within a test, you may define:
- **assert\***: A group of keywords used for asserting conditions. Examples include assertStdoutEquals, assertStdoutNotEquals, etc.
- **setSeverity**: defines the severity for the test

## [Execution](execution.md)

If you were to execute a program called "HelloWorld", this is how you would do it:

```yml
Hello_World_Test:
- HelloWorld.exe
```

## [Asserts](asserts.md)

Asserts are used to verify the output or behavior of the executed program. If you would wish to assert that the output will be "Hello World", you would then add an assert to the parent test.

```yml
Hello_World_Test:
  assertStdoutContains: "Hello World"
  run:
  - HelloWorld.exe
```

## [Input](inputs.md)

You can use inputs to provide parameters to the executed programs. This allows you to test the same program with different input values:

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

Playbooks have specific settings for various aspects like providing names to tests, configuring notifications, setting execution frequency to monitor systems, and more:

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

To include other playbooks in your own you can use imports. Imports can include either public Satori playbooks or local files, for example:

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

The name `import` is not mandatory and the node can be placed in any place (given that is valid YAML).

## Errors

Satori validates the schema of your playbook as soon as it is received to ensure the syntax and grammar are correct. If any errors are detected (either from user input or from the system), we will promptly inform you. The error will be shown when viewing your report with `satori report REPORTID` command or from the **Reports** section of the Satori Web.

If you need any help, please reach out to us on [Discord](https://discord.gg/NJHQ4MwYtt) or via [Email](mailto:support@satori-ci.com)
