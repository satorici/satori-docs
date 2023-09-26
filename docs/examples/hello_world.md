## satori-cli run

Consider the following example "Hello World" program written in Python:

```py
print("Hello World")
```

If you save that into a file named `hello_world.py` and you execute the program, you will see the following on your console:

```console 
foo@bar:~$ python hello_world.py
Hello World
```

Now, regardless of the language of your program, lets assert that the output should be equal to Hello World

```console
foo@bar:~$ cat .satori.yml
test:
    assertStdoutEqual: Hello World
    python:
    - [ python hello_world.py ]
```

Lets test the code with the playbook
```console
foo@bar:~$ satori-cli run ./ --sync
Satori CI 1.2.3 - Automated Software Testing Platform 
Uploading... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 331/331 bytes 0:00:00
UUID: AOQxDWDkXpZp
Report: https://www.satori-ci.com/report_details/?n=AOQxDWDkXpZp
- Report status: Completed | Result: Pass | Elapsed time: 62.6s
  • test: test > python
  • asserts:
      ░ assert: assertStdoutEqual
      ░ status: Pass
      ░ expected: Hello World
      - - - - - - - - - - - - - - - - - - - - 
  • testcases: 1
  • test_status: Pass
  • total_fails: 0
  - - - - - - - - - - - - - - - - - - - - 
```

The code and the Satori playbook instructions were executed on a private Docker instance hosted by AWS. Your code is not stored Satori, as it only analysis the behavior of the software being executed using the output that is created. 
