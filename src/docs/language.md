# [Intro](README.md)
## Language

In Satori, the files where testing procedures are defined are known as Playbooks. These files use YAML syntax and have the ".yml" file extension.

Playbooks may contain a variety of components such as settings, imports, tests, executions, and asserts. All of these elements follow a specific language specification[1].

### Reserved Words

Certain words in the Satori playbook language are reserved for special operations:

- **settings**: Used to define global options for the playbook.
- **import**: Incorporates other YAML files into the current playbook.
- **assert***: A group of keywords used for asserting conditions. Examples include assertStdoutEquals, assertStdoutNotEquals, etc.

### [Execution](language_execution.md)

If you were to execute a program called "HelloWorld", this is how you would do it:

```yml
Hello_World_Test:
- [ ./HelloWorld ]
```

### [Asserts](language_asserts.md)

Asserts are used to verify the output or behavior of the executed program. If you would wish to assert that the output will be "Hello World", you would then add an assert to the parent test. 

```yml
Hello_World_Test:
  assertStdoutContains: "Hello World"
  run:
  - [ ./HelloWorld ]
```

### [Input](language_inputs.md)

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

### [Settings](language_settings.md)

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

### [Playbooks](language_playbooks.md)

All the information mentioned above is contained within Playbook files. By default, these playbooks are private for all users. However, Satori provides a set of public playbooks to assist users in creating complex test cases: https://github.com/satorici/playbooks.

### Errors

Satori validates the schema of your playbook as soon as it is received to ensure the syntax and grammar are correct [1]. If any errors are detected (either from user input or from the system), we will promptly inform you. The error details can be accessed via the `satori-cli report` command or from the **Reports** section of the Satori Web.

[1] https://github.com/satorici/playbook-validator