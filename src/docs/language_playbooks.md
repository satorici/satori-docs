# [Intro](README.md)
## [Language](language.md)
### Playbooks

Playbooks store tests that will [execute](language_execute.md) commands to [assert](language_asserts.md) its behavior with potentially different forms of [inputs](language_input.md). 

Playbooks can have undefined variables that can be supplied as dynamic parameters. Consider the following playbook that uses the undefined VAR variable:

echo.yml:
```yml
test:
    - [ echo $(VAR) ]
```

The previous playbook can be executed on the following way by Satori CLI:

```sh
$ satori-cli run echo.yml --data="{'VAR':'Hello World'}"
```

#### Public Playbooks

At Satori we have defined multiple playbooks to execute some of the most common functionalities of devops and secdevops processes, such as:
- Static source code analyzers
- Dynamic security testing
- Third party libraries checks

You can check the complete list of public playbooks with the command:

`satori-cli playbook --public`

Here is a sample output:

-------------------------------------------------------------------------------------------------------------------------------------------
| Filename                         | Name                                                                            |         Parameters |
|----------------------------------|---------------------------------------------------------------------------------|--------------------|
| satori://attack/bombardment.yml  | Run siege with an ever-increasing number of users                               |                URL |
| satori://attack/siege.yml        | Siege - Load testing web servers                                                |                URL |
| satori://attack/slowhttptest.yml | SlowHTTPTest - Common low-bandwidth application layer Denial of Service attacks |                URL |
| satori://aws/scoutsuite.yml      | Scout suite for AWS                                                             | KEY_SECRET, KEY_ID |
| satori://code/cloc.yml           | Count the lines of code                                                         |                    |
| ...                              |                                                                                 |                   ||

If you notice, some playbooks have predefined parameters that will be expected to be executed. Parameters try to be self descriptive, so a URL is expected whenever the parameter is called `URL`.

#### Private Playbooks

In case you need to check your previously executed playbooks, you may do so with the following command:
`satori-cli playbook`

Your playbooks are private by default, and you can further interact with them with their id to read them:

`satori-cli playbook ID`

Or to delete them:

`satori-cli playbook ID delete`

#### Import Playbooks

Playbooks can be imported by other playbooks. Local files or publicly available playbooks from Satori can be imported by other playbooks. They are executed on the order that they were introduced on the YAML file.

##### Import of Local Playbooks

The reserved word `import` can be used in playbooks to import local and public playbooks:

PositiveHelloWorldTest.yml
```yml
PositiveHelloWorldTest:
    assertStdoutEquals: "Hello World"
    run:
    - [ echo Hello World ]
```

NegativeHelloWorldTest.yml
```yml
NegativeHelloWorldTest:
    assertStdoutNotEquals: "Hello World"
    input:
      - "Hello World"
      mutate_qty: 1
    run:
    - [ echo $(input) ]
```

Then you can execute:

HelloWorldTest.yml
```yml
import:
    - "PositiveHelloWorldTest.yml"
    - "NegativeHelloWorldTest.yml"
```

`satori-cli run HelloWorldTest.yml`

##### Import of Public Playbooks

Include on the root folder of your GitHub repository a file named `.satori.yml` with the following line to automatically verify for secrets in the code:
```yml
import:
    - "satori://code/trufflehog.yml"
```

#### Run referencing Playbooks

##### Run Local Playbook

If you create the following HelloWorld.yml playbook file:
```
test:
    assertStdoutEqual: "Hello World"
    run:
    - [ echo Hello World ]
```

You can execute it with the following oneliner to check its output:
`satori-cli run HelloWorld.yml --report"`

The optional `--report` parameter will run satori synchronously and print its report. If you want to check the output instead, you would use `--output`

##### Run Public Playbook

If you want to use some of our public playbooks, you can do so referencing by referencing any of the public list (`satori-cli playbook --public`) 
`satori-cli repo satorici/satori-cli run --playbook "satori://code/trufflehog.yml" --report`

If you need any help, please reach out to us on [Discord](https://discord.gg/F6Uzz7fc2s) or via [Email](mailto:support@satori-ci.com)
