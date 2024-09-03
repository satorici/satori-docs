# Asserts

You can assert what will be the behavior of [executions](execution.md):

| Assert                  | Value          | Description                                                            |
|-------------------------|----------------|------------------------------------------------------------------------|
| assertStdout            | Boolean        | Is output produced?
| assertStdoutEquals      | String\*       | Is the output equal to the String?
| assertStdoutNotEquals   | String         | Is the output different than the String?
| assertStdoutContains    | String         | Does the output contain the String?
| assertStdoutNotContains | String         | Does the output not contain the String?
| assertStdoutSHA256      | SHA256Checksum | Is the output equal to this SHA256 hash?
| assertStdoutRegex       | Regex          | Does the output match your regular expression?
| assertStdoutNotRegex    | Regex          | Does the output not match your regular expression?
| assertStderr            | Boolean        | Are errors produced?
| assertStderrEquals      | String\*       | Is the error equal to the String?
| assertStderrNotEquals   | String         | Is the error different than the String?
| assertStderrContains    | String         | Does the error contain the String?
| assertStderrNotContains | String         | Does the error not contain the String?
| assertStderrSHA256      | SHA256Checksum | Is the error equal to this SHA256 hash?
| assertStderrRegex       | Regex          | Does the error match your regular expression?
| assertStderrNotRegex    | Regex          | Does the error not match your regular expression?
| assertReturnCode        | Integer        | Is the return code equal to the Integer?
| assertReturnCodeNot     | Integer        | Is the return code not equal to the Integer?
| assertSoftwareExists    | Boolean        | Does the software being executed exist? True by default
| assertDifferent         | Boolean        | Does the execution behave differently when using different inputs?
| assertKilled            | Boolean        | Did the software time out?

---

### General usage

Asserts are defined within tests:

```yml
HelloWorld:
  assertStdoutContains: "Hello World"
  echo:
  - echo Hello World
```

And they can have a severity associated, especially useful when working with ticketing systems:

```yml
HelloWorld:
  assertStdoutContains: "Hello World"
  setSeverity: 1
  echo:
  - echo Hello World
```

---

## assertStdout
| Input   | Description                            |
|---------|-----------------------------------------
| Boolean | Asserts if an output has been produced |

- <span style="color:green">Example Pass Test</span>: the program should deliver output, and it does:
```yml
test:
    assertStdout: True
    run:
    - echo Hello World
```

- <span style="color:red">Example Fail Test</span>: the program should deliver output, but no output is produced:

```yml
test:
    assertStdout: True
    run:
    - ./broken_executable
```

---

## assertStdoutEquals

| Input  | Description                                    |
|--------|-------------------------------------------------
| String | Asserts that the output is equal to the String |

- <span style="color:green">Example Pass Test</span>: the program should only output "Hello World", and it does:

```yml
test:
    assertStdoutEquals: "Hello World"
    run:
    - echo Hello World
```

- <span style="color:red">Example Fail Test</span>: the program should only output "Hello World", but it doesn't:

```yml
test:
    assertStdoutEquals: "Hello World"
    run:
    - echo 'hello world'
```

---

## assertStdoutNotEquals

| Input | Description                          |
|-------|---------------------------------------
|String | Is the output different than String? |

- <span style="color:green">Example Pass Test</span>: the program output should not be equal to "Hello World", and is not:

```yml
test:
    assertStdoutNotEquals: "Hello World"
    input:
    - - value: "Hello World"
        mutate: radamsa
        mutate_qty: 1
    run:
    - echo ${{input}}
```

---

## assertStdoutContains

| Input | Description |
|-------|--------------
| String         | Does the output contain the String?

- <span style="color:green">Example Pass Test</span>: the program output should contain the string "Hello World", and it does:

```yml
test:
    assertStdoutContains: "Hello World"
    run:
    - echo Hello World 2023
```

---

## assertStdoutNotContains

| Input  | Description                             |
|--------|------------------------------------------
| String | Does the output not contain the String? |
- <span style="color:green">Example Pass Test</span>: the program output should not contain the string "Error", and it does not:
```yml
test:
    assertStdoutNotContains: "Error"
    run:
    - echo Hello World
```

---

## assertStdoutSHA256
| Input          | Description                              |
|----------------|-------------------------------------------
| SHA256Checksum | Is the output equal to this SHA256 hash? |
- <span style="color:green">Example Pass Test</span>: Network ports of , and it does:

```yml
settings:
    name: "Nmap: did any service changed?"

install:
    assertReturnCode: 0
    updates:
    - apt update
    nmap:
    - apt install -y nmap
nmap:
    assertReturnCode: 0
    run:
    - nmap -n www.example.com -Pn -p21,22,80,443,3000,3306,5432 -sT -oG nmap
    services:
      assertStdoutSHA256:
      - "e3b0c44298fc1c142afbf4c8996fb92427ac41e4649b934ca49599ab7852b855"
      running:
      - "grep Ports nmap | sort -u" # the assert will calculate the hash value of this output and compare if there are differences
```

---

## assertStdoutRegex
| Input | Description                          |
|-------|---------------------------------------
| Regex | Does the output match your regular expression? |

- <span style="color:green">Example Pass Test</span>: the program output should contain the string "Hello " and additional characters, and it does:
```yml
test:
    assertStdoutRegex: "Hello .*"
    run:
    - echo Hello World
```
---

##  assertStdoutNotRegex
| Input | Description                            |
|-------|-----------------------------------------
| Regex | Does the output not match your regular expression? |

- <span style="color:gray">Example Unknown Test</span>: the program output should not contain the string "Hello World" anywhere on the output, but the input could be mutated to "somethingHello World" and the result depends on the mutation:

```yml
test:
    assertStdoutNotRegex: "*Hello World*"
    input:
    - - value: "Hello World"
        mutate: radamsa
        mutate_qty: 1
    run:
    - echo Hello ${{input}}
```

---

## assertStderr
| Input   | Description           |
|---------|-----------------------|
| Boolean | Are errors produced?  |
- <span style="color:green">Example Pass Test</span>: the program output should not output errors, and it does not:
```yml
test:
    assertStderr: False
    run:
    - echo Hello World
```
---

## assertStderrEquals
| Input    | Description                       |
|----------|------------------------------------
| String\* | Is the error equal to the String? |
- <span style="color:pass">Example Pass Test</span>: the programs should error requesting the value of the x parameter:
```yml
test:
    assertStderr: "The value of the parameter -x is required for the program"
    run:
    - program -x
```
---

## assertStderrNotEquals
| Input  | Description                         |
|--------|--------------------------------------
| String | Is the error different than the String? |
- <span style="color:pass">Example Pass Test</span>: the programs should not error requesting the value of the x parameter when is defined:
```yml
test:
    assertStderrNotEquals: "The value of the parameter -x is required for the program"
    run:
    - program -x whatever
```
---

## assertStderrContains
| Input  | Description                         |
|--------|--------------------------------------
| String | Does the error contains the String? |
- <span style="color:pass">Example Pass Test</span>: the program's errors should contain the string Traceback, and it does:
```yml
install:
   - "echo import nonexistent > test.py"
test:
    assertStderrContains: "Traceback"
    run:
    - python3 test.py
```
---

## assertStderrNotContains
| Input  | Description                            |
|--------|-----------------------------------------
| String | Does the error not contain the String? |
- <span style="color:fail">Example Fail Test</span>: the program's errors should not contain the string Traceback, but it does:
```yml
install:
   - "echo import nonexistent > test.py"
test:
    assertStderrNotContains: "Traceback"
    run:
    - python3 test.py
```
---

##  assertStderrSHA256
| Input          | Description                             |
|----------------|------------------------------------------
| SHA256Checksum | Is the error equal to this SHA256 hash? |
- <span style="color:fail">Example Fail Test</span>: the program's errors should not contain the string Traceback, but it does:
```yml
install:
   - "echo import nonexistent > test.py "
test:
    assertStderrSHA256: "69827a4c85154b891cae9c35d99887375d815ec676bb7ce86e1f7601f6fec3ad"
    run:
    - python3 test.py
```
---

## assertStderrRegex
| Input | Description                         |
|-------|--------------------------------------
| Regex | Does the error match your regular expression? |
- <span style="color:gray">Example Unknown Test</span>: the Python script my_script.py might throw a KeyError exception with 'unexpected_key' if a certain condition in the script isn't met:
```yml
RunPythonScriptTest:
    assertStderrRegex: ".*KeyError: 'unexpected_key'.*"
    run:
    - python3 my_script.py
```
---

## assertStderrNotRegex
| Input | Description                           |
|-------|----------------------------------------
| Regex | Does the error not match your regular expression? |
- <span style="color:green">Example Pass Test</span>: the program's errors should  not throw a Traceback, and it doesn't:

```yml
install:
   - "echo import os > test.py"
test:
    assertStderrNotRegex: "*Traceback*"
    run:
    - python3 test.py
```
---

## assertReturnCode
| Input   | Description                              |
|---------|-------------------------------------------
| Integer | Is the return code equal to the Integer? |
- <span style="color:green">Example Pass Test</span>: the program should return the code 0, and it does:
```yml
test:
    assertReturnCode: 0
    run:
    - echo This program is executed correctly
```
---

## assertReturnCodeNot
| Input   | Description                              |
|---------|-------------------------------------------
| Integer | Is the return code not equal to the Integer? |
- <span style="color:green">Example Positive Pass Test</span>: the program should not return the code 0, and it doesn't:

```yml
test:
    assertReturnCodeNot: 0
    run:
    - return 2
```
---

## assertSoftwareExists

| Input | Description |
|-------|--------------
| Boolean        | Does the software being executed exists? True by default
- <span style="color:fail">Example Fail Test</span>: the program should exist, and it does not:

```yml
test:
    assertSoftwareExists: True # by default
    run:
    - ./your_program
```

---

## assertDifferent
| Input   | Description                                                         |
|---------|----------------------------------------------------------------------
| Boolean | Does the execution behave differently when using different inputs? |
- <span style="color:fail">Example Fail Test</span>: the production and staging environment should look the same, and it does not:

```yml
API:
- - "www.example.com"
  - "staging.example.com"

test:
    assertDifferent: False
    run:
    - curl $API
```

---

## assertKilled
| Input   | Description                 |
|---------|------------------------------
| Boolean | Did the software time out? |
- <span style="color:fail">Example Fail Test</span>: the software should finish execution within 10 seconds, and it does not:
```yml
settings:
    software_timeout: 10

test:
    assertKilled: False
    run:
    - sleep 20
```

---

If you need any help, please reach out to us on [Discord](https://discord.gg/NJHQ4MwYtt) or via [Email](mailto:support@satori-ci.com)
