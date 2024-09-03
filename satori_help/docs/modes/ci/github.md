# Github CI App

Each time you push code to your Github repository, there's a risk that it could affect the security of your project. Furthermore, should your data ever be compromised, it's crucial to minimize the exposure of sensitive information. Two primary areas of concern are:

- Secrets in your code
- Vulnerable code from yourself or third parties

Automatically test your GitHub repositories by installing our App:

**1) Satori CI for Github** <https://github.com/apps/satorici>

![Satori CI Github Install](img/github_1.png)

Be mindful that you need to be authenticated to configure it.

**2) Click on Configure**

![Install Satori CI on your account](img/github_2.png)

Select which accounts you will be setting it up for.

**3) Select the repositories where you will be installing it or select all repositories**

![Select your Github repositories where you will use Satori](img/github_3.png)

Once you are done, click on **Save**. We care about your security, so we will only store your email, your repositories names, and the reports. Your code only lives within the virtual machines that are present during the execution.

**4) Create your first .satori.yml file**

Within the repositories that you will connect, you want to create a file named `.satori.yml`. This file will contain the tests that you will executing on every push. Let's keep it simple, and start checking for secrets with Trufflehog:

```yml
settings:
  name: CI Tests for every push of my Repo

import:
- "satori://code/trufflehog.yml"

tests:
  assertReturnCode: 0
  build:
  - make
  run:
    assertStdoutContains: "An expected output" # assert the output of    the main system execution of your project
    your_project:
    - ./your_project
```

These are the steps to run it locally:

```sh
git clone https://github.com/satoridev01/Hello_C_World.git
cd Hello_C_World
satori run ./ --output
```
---

If you need any help, please reach out to us on [Discord](https://discord.gg/NJHQ4MwYtt) or via [Email](mailto:support@satori-ci.com)
