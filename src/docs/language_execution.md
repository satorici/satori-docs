# [Intro](README.md)
## [Language](language.md)
### Execution

The execution happens whenever your test contains an array. For example:

```yml
echo_stdout:
    - [ echo 'Hello World' ]
```

Whenever you need shell commands or you are concatenating multiple commands with the assistance of a shell, you must include them between quotes

```yml
echo_file:
    - [ "echo 'Hello World' > file" ]
```

It should be noted that [inputs](language_inputs.md) can be defined to be used as part of the executions:
```yml
salute:
  - "Hello"
  - "Bye"
echo_salute:
  assertStdoutEqual: "Hello World"
  - [ echo '$(salute) World' ]
```

The previous example will assert that the output will be Hello World, and it will show one Pass and one Fail due to the possible combinations. For more information on the assert please visit the [asserts](language_asserts.md) section. If you need any help, please reach out to us on [Discord](https://discord.gg/F6Uzz7fc2s) or via [Email](mailto:support@satori-ci.com)
