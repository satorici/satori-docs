# Polyglot Hello World Test

The "Hello World" program is the most basic example in any programming language. 
In this guide, we’ll use this concept to create a test that can be executed across multiple languages using Satori. This will help verify that a basic program can correctly output "Hello World" to the console.

We have forked a popular "Hello World" repository on GitHub and created a .satori.yml file within it. This file defines the tests for four different languages:

```yml
settings:
  name: Polyglot Hello World Test
  image: nikolaik/python-nodejs
  
tests:
  assertStdoutContains: Hello World
  
  bash:
    - bash HelloWorld.sh
  javascript:
    - node HelloWorld.js
  perl:
    - perl HelloWorld.pl
  python:
    - python3 HelloWorld.py
```

The previous playbook uses an image that has preinstalled node and python. Bash and Perl come by default, so no need to install them separatedly.

**Running tests without cloning the repository**

Since the .satori.yml playbook is present in the repository, running Satori on this repository will automatically use the defined configuration file to execute the tests showing the output and report.
To run the tests on this repository, use the following command:

`satori repo satoridev01/test.blackbird71SR.Hello-World run --output --report `

This is how the output and the report will look like on the console:

![Run Satori on the repo showing the report and the output of multiple Hello World programming languages](img/hello_01.png)

You can also view the report online since we have made it public using the command `satori report rLmtEtgJ3EhDFj2A public`, you can also check it out [online](https://satori.ci/report_details/?n=rLmtEtgJ3EhDFj2A):

![Web report of multiple Hello World programming languages](img/hello_02.png)

**Running tests locally**

If you'd like to run a test with code stored on your local machine, you can simulate it by cloning the repository and running the tests:

```sh
~ $ git clone --quiet https://github.com/satoridev01/test.blackbird71SR.Hello-World.git 
~ $ cd test.blackbird71SR.Hello-World/
test.blackbird71SR.Hello-World $ satori run ./ --output --report
```

This is how it looks:

![Run Satori remotely uploading from your code from localhost](img/hello_03.png)

To run the commands locally on your project and then upload the results to Satori for analysis, use the following command:

`satori local ./ --output --report`

And it would look like this:

![Run locally and analyze them with Satori](img/hello_04.png)
