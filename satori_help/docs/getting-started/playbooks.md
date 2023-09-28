# Playbooks overview

In Satori, the files where testing procedures are defined are known as Playbooks. These files use YAML syntax and have the ".yml" file extension.

Playbooks may contain a variety of components such as settings, imports, tests, executions, and asserts. All of these elements follow a specific language specification[1].

## Writing your first playbook

In order to test something we first need to get the information. The way to do this is executing commands to get the outputs: stdout, stderr, return code, time taked, etc.

How can you express this? Simple:

```yml
execute:
  - [echo Hello world!]
```

This playbook is a litle dumb, it doesn't do any testing! Let's add some assertions:

```yml
test:
  assertStdoutEqual: Hello world!\n
  assertReturnCode: 0

  execute:
    - [echo Hello world!]
```

Notice that now we have an actual test, it executes something and does some output checks. We can have many tests in a single playbook, and also nested tests.

Here's something interesting, the `cmd` execution inherits all the 2 assertions and `execute` only gets the return code check:

```yml
test:
  assertReturnCode: 0

  nested-test:
    assertStdoutContains: Bye
    cmd:
      - [echo Bye, see you later!]

  execute:
    - [echo Hello world!]
```

But what if you want to tests many cases? You can reference inputs this way:

```yml
test:
  assertReturnCode: 0

  input:
    - Hello world!
    - See you later!

  execute:
    - [echo $(input)]
```

You can read more about the [language](../playbooks/language.md) features and the possible [asserts](../playbooks/asserts.md).
