# Hello World Test

The most basic program that we can have for a programming languages is one that prints "Hello World" on the screen. The most popular [repository](https://github.com/blackbird71SR/Hello-World) on Github about this has a great collection to start testing.

We have made a fork of that repository and created our own .satori.yml file within it to test 4 languages:

```yml
settings:
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

Since the playbook is present in the playbook, we can ask satori to run on this repo showing the report and the output:

`satori repo satoridev01/test.blackbird71SR.Hello-World run --report --output`

[Run Satori on the repo showing the report and the output of 4 Hello World programming languages](img/hello_01.png)
