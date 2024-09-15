
# Executions

In Satori, an execution happens when your test includes a specific element that triggers an action. Here, an "element" refers to any component of the test that initiates a command or process. For example:

```yml
echo_stdout:
- echo 'Hello World'
```

Commands defined in your Playbook will be executed automatically within a shell environment. For clarity and to ensure proper execution, you can enclose commands in quotes.

```yml
echo_file:
- "echo 'Hello World' > file"
```

## Inputs in Executions

[Inputs](inputs.md) allow you to define parameters that can be used dynamically during the execution of your tests. 

```yml
salute:
- - "Hello"
  - "Bye"

echo_salute:
  assertStdoutEqual: "Hello World"
  run:
  - echo '${{salute}} World'
```

Example:

![inputs on executions](img/execution_1.png)

In this example:
- The output "Hello World" is expected for the input "Hello" and will result in a pass.
- Other combinations of inputs, such as "Bye World", will not match "Hello World", leading to a fail.
For more details on how assertions work, please refer to the [asserts](asserts.md) section.
