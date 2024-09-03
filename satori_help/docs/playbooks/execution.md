
# Executions

The execution occurs whenever your test includes a specific element. For clarity, an "element" refers to any test component that triggers an action. For example:

```yml
echo_stdout:
- echo 'Hello World'
```

Commands will automatically execute under a shell, or you can ensure execution by enclosing commands in quotes:

```yml
echo_file:
- "echo 'Hello World' > file"
```

## Inputs on Executions

It should be noted that [inputs](inputs.md) can be defined to be used as part of the executions. For instance:

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
This example asserts the output 'Hello World,' leading to one pass and one fail due to the possible combinations. For more information on the assert mechanism, please visit the [asserts](asserts.md) section.

If you need any assistance, please reach out to us on [Discord](https://discord.gg/NJHQ4MwYtt) or via [Email](mailto:support@satori-ci.com).
