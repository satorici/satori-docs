# [Intro](README.md)
## Github CI App

Each time you push code to your Github repository, there's a risk that it could affect the security of your project. Furthermore, should your data ever be compromised, it's crucial to minimize the exposure of sensitive information. Two primary areas of concern are:
- Secrets on your code
- Vulnerable code from yourself or third parties

Automatically test your GitHub repositories by installing our App:

1. Go to https://github.com/apps/satorici
2. Click on Install
3. Select the repositories where you will be installing it or select all repositories

We care about your security, so we will only store your email, your repositories names, and the reports. Your code only lives within the virtual machines that are present during the execution. 

Within the repositories that you will connect, you want to create a file named .satori.yml that may look like this:
. This file will contain the tests that you will execute with every push. For example, you can choose to start by checking your code for secrets and from a static source code audit point of view:


```yml
settings:
  name: CI Tests for every push of my Repo
  description: Find secrets on the code, static source code audit and run an end to end test asserting the expected output for your project
  onLogFail: slack-monitor # Send a message to the monitor channel on Slack if the test Fails
import: # public playbooks
  - "satori://search/trufflehog.yml" # will search for secrets on your code with Trufflehog (https://github.com/trufflesecurity/trufflehog)
  - "satori://code/semgrep.yml" # will perform a static source code analysis with Semgrep (https://github.com/returntocorp/semgrep)
install: # the required software to execute your tests
  assertReturnCode: 0 # the return code or something else of the software that you need to install
  - [ make ]
execute:
  assertStdoutContains: "An expected output" # assert the output of the main system execution of your project
  - [ ./your_project ]
```

If you need any help, please reach out to us on [Discord](https://discord.gg/F6Uzz7fc2s) or via [Email](mailto:support@satori-ci.com)
