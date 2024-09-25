# Run

Satori runs remotely in our platform or locally where it is being executed. 

## Run Remotely

This playbook named `hello.yml`:

```yml
test:
  assertStdoutEqual: "Hello world\n"
  assertReturnCode: 0

  execute:
    - echo Hello world
```

Can be run:

- With no parameters: asynchronously
- With `--sync`: synchronously and it shows the status when it is complete
- With `--report`: synchronously and it shows the report when it is complete
- With `--output`: synchronously and it shows the output when it is complete

![Run remotely aync and async](img/run_1.png)

## Run Remotely with Parameters

If you include a ${{variable}} within your playbook that is not defined within your playbook, they will be parameters required when being called. Consider the playbook named `satori://test.yml` that will echo the ${{WHAT}} parameter:

```yml
test:                                                                                                                                                                             
  assertStdoutContains: Hello World                                                                                                                                               
  hello:                                                                                                                                                                          
  - echo Hello World                                                                                                                                                              
  whatever:                                                                                                                                                                       
  - echo ${{WHAT}}
```

You will execute it like this

![Run with params](img/run_2.png)

### Run with the files in the Local Directory

In case you are working locally on a directory with source code, you save your playbook as `.satori.yml` within the directory, just as you would for your repo when testing your code through CI. 

Consider the following example main.c file, that is referenced by a Makefile, and a playbook that verifies that everything returns the code 0 and when running the code it outputs "Hello World":

- **main.c**:

```c
#include <stdio.h>

int main() {
    printf("Hello World\n");
    return 0;
}
```

- **Makefile**:

```c
all: hello

hello: main.c
	gcc -o hello main.c
```

- **.satori.yml**:

```yml
install:
  updates:
    - apt update >> /dev/null
  dependencies:
    - apt install -qy make gcc >> /dev/null

tests:
  assertReturnCode: 0
  build:
    - make
  run:
    assertStdoutContains: "Hello World"
    hello:
      - ./hello
```

![Run with the files in the Local Directory](img/run_3.png)

You would use it like this when developing locally before pushing, or when being used as part of Github Actions or Jenkins.

### Run a public Playbook

You can run on-demand public playbooks. You can see a list of the publicly available playbooks with: `satori playbook --public`

Then you can execute them passing parameters if required with `-d`:

```sh
satori run satori://some/playbook.yml
```

![Run a public playbook with a parameter](img/run_4.png)

You would run it like this when there is a public playbook that already addresses your problem.

### Run Locally

The playbook named `hello.yml` that we ran before remotely can also be executed locally and the assertion results will be confirmed by Satori:

![Run locally aync and async](img/run_local.png)

[Learn more about Monitors](monitor.md)

### Run a process in Background

If you are running a service that needs to listen on background, processes will remain in foreground if you use shell scripting techniques. The recommended approach is to install screen and send the process to the background. An additional tip is to include a timeout in settings to set a limit for the container. For example:

```yml
settings:
  name: Background process
  timeout: 60

install:
- apt update >> /dev/null
- apt install -qy screen >> /dev/null

background:
  - screen -dm sleep 10

check:
  assertStdoutContains: "10"
  ps:
    - ps wuax | grep sleep
```

![Background](img/run_background.png)

The `screen -dm` command is used to start a new detached `screen` session in the background. This is useful for running commands or scripts in the background and continue executing additional commands to test the background service.
