# [Intro](README.md)
## [Language](language.md)
### Inputs

Inputs can be grouped under any non reserved word (settings, assert*)

```yml
input:
  - "One"
  - "Two"
echo:
  - [ echo $(input) ]
```

You can also define different nested values. The following example will show a Pass for the positive test, and a Fail for the negative test:

```yml
input:
  positive:
  - "Hello"
  negative:
  - "Bye"
echo:
    assertStdoutEqual: "Hello World"
  - [ echo $(input) World ]
```

#### Dictionaries

Dictionary files can be splitted by certain characters (normally newlines) to be used as inputs for the tests.

- Example:
```
install:
    - [ wget -O https://raw.githubusercontent.com/danielmiessler/SecLists/master/Fuzzing/big-list-of-naughty-strings.txt ]
dict-input:
    - file: big-list-of-naughty-strings.txt
      split: \n
echo:
    assertReturnCode: 0
    run:
    - [ echo $(dict-input) ]
```

#### Mutations

Input can be mutated. Mutations are always different than the original string. They are specified as follow:

```yml
input:
    - "Hello World"
      mutate_qty: 10
echo:
    assertStdoutNotEqual: "Hello World"
    - [ echo $(input) ]
```

The previous playbook will generate 10 different mutations of the string "Hello World" that will be echoed to the standard output. 

If you need any help, please reach out to us on [Discord](https://discord.gg/F6Uzz7fc2s) or via [Email](mailto:support@satori-ci.com)
