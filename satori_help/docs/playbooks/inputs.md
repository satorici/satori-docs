# Inputs

When testing a system, the behaviors are analyzed based on the inputs used, examining the outputs produced from a [black box perspective](https://en.wikipedia.org/wiki/Black_box) where the internal logic of the system is not directly observed.

Inputs in Satori can either be predefined within the playbook or left undefined, allowing them to be specified at execution. Inputs may be valid and invalid inputs to test the software behavior, making it possible to assess the system's response to expected and unexpected data.

## Parametrized

Consider the following playbook,  `satori://test.yml `, which includes a variable  `${{WHAT}} ` that is not defined within the playbook:

```yml
test:
  assertStdoutContains: Hello World
  hello:
    - echo Hello World
  whatever:
    - echo ${{WHAT}}
```

When running this playbook, you will need to pass a value for `${{WHAT}}` at execution, as it is not predefined in the playbook, with the next command `-d`:

```sh
satori run .satori.yml  -d WHAT="Bye World" --report --output
```

![Parametrized inputs](img/inputs_0.png)

## Defined within the playbook

Inputs can be specified directly in the playbook and named accordingly for the software being tested. In the example below, the `echo` command will iterate through each value defined under `input`:


```yml
input:
- - "One"
  - "Two"

echo:
- echo ${{input}}
```

This will produce the following output:

![use inputs](img/inputs_1.png)

You can also organize inputs with nested values. The following example demonstrates how a positive test will pass, while a negative test will fail:

```yml
input:
  positive:
  - - "Hello"
  negative:
  - - "Bye"

echo:
  assertStdoutEqual: "Hello World"
  input:
  - echo -n ${{input)}} World
```

For example:

![use positive and negative values](img/inputs_2.png)

## Dictionaries as Input

Dictionary files can serve as input sources by splitting the file content by newlines. In the example below, `dict-input` is defined to read from `dict.txt` and splits each entry by newline `\n` for use in the tests:

```yml
dict-input:
- - file: dict.txt
    split: \n

echo:
  assertReturnCode: 0
  run:
  - echo ${{dict-input}}
```

## Mutating inputs for testing

Mutations allow you to test software resilience by altering inputs unexpectedly. By modifying input strings with mutations, you can observe how software responds to diverse, potentially malformed data. The following example demonstrates setting up mutations for the input `"Hello World"` using two different mutation types, `radamsa` and `zzuf`:


```yml
input:
- - value: "Hello World"
    mutate: radamsa
    mutate_qty: 5

  - value: "Hello World"
    mutate: zzuf
    mutate_qty: 5

echo:
  assertStdoutNotEqual: "Hello World"
  input:
  - echo -n ${{input}}
```
In this playbook, each mutation tool (e.g., `radamsa` and `zzuf`) will generate 5 variations of the input, totaling 10 distinct mutations. The mutations are then echoed, with the `assertStdoutNotEqual` check verifying that none of the mutated outputs match the original string `"Hello World"`.

For example:

![mutate your inputs](img/inputs_4.png)
