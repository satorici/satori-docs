# Language

In Satori, the files where testing procedures are defined are known as Playbooks. These files use YAML syntax and have the ".yml" file extension.

Playbooks may contain a variety of components such as settings, imports, tests, executions, and asserts. All of these elements follow a specific language specification[1].

## Reserved Words

Certain words in the Satori playbook language are reserved for special operations:

- **settings**: Used to define global options for the playbook.
- **assert\***: A group of keywords used for asserting conditions. Examples include assertStdoutEquals, assertStdoutNotEquals, etc.

## [Execution](execution.md)

If you were to execute a program called "HelloWorld", this is how you would do it:

```yml
Hello_World_Test:
- [ ./HelloWorld ]
```

## [Asserts](asserts.md)

Asserts are used to verify the output or behavior of the executed program. If you would wish to assert that the output will be "Hello World", you would then add an assert to the parent test.

```yml
Hello_World_Test:
  assertStdoutContains: "Hello World"
  run:
  - [ ./HelloWorld ]
```

## [Input](inputs.md)

You can use inputs to provide parameters to the executed programs. This allows you to test the same program with different input values:

```yml
Hello_World_Test:
  assertStdoutContains: "Hello World"
  who:
  - "Foo"
  - "World"
  run:
  - [ ./HelloWorld $(who) ]
```

## [Settings](settings.md)

Playbooks have specific settings for various aspects like providing names to tests, configuring notifications, setting execution frequency to monitor systems, and more:

```yml
settings:
  name: "Tests Hello World with parameters"
  logOnFail: slack

Hello_World_Test:
  assertStdoutContains: "Hello World"
  who:
  - "Foo"
  - "World"
  run:
  - [ ./HelloWorld $(who) ]
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
  - "Foo"
  - "World"
  run:
  - [ ./HelloWorld $(who) ]
```

The name `import` is not mandatory and the node can be placed in any place (given that is valid YAML).

## Errors

Satori validates the schema of your playbook as soon as it is received to ensure the syntax and grammar are correct. If any errors are detected (either from user input or from the system), we will promptly inform you. The error will be shown when viewing your report with `satori report REPORTID` command or from the **Reports** section of the Satori Web.

If you need any help, please reach out to us on [Discord](https://discord.gg/F6Uzz7fc2s) or via [Email](mailto:support@satori-ci.com)
