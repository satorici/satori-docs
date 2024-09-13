# Satori CLI on Github Actions

If you want to test part of your workflow with Satori:

**1) Go to Actions and click on New Workflow**

![New Workflow Action](img/github_action_1.png)

**2) Click on set up a workflow yourself**

![Set up a workflow](img/github_action_2.png)


**3) Include as part of your workflow the Satori Job:**

```yml
name: Satori CI Analysis
on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]
jobs:
  satori-cli_run:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: run
        env:
          SATORITOKEN: ${{ secrets.TOKEN }}
        run: |
          pip3 install satori-ci
          satori config token $SATORITOKEN
          satori run ./ -s
```

Click on **Commit Changes**

![Satori CI workflow](img/github_action_3.png)

**4) Go to your repository `Settings`, click on `Secrets and variables` and then on `Actions`**

![](img/github_action_4.png)

**5) Click on `New repository secret`**

![](img/github_action_5.png)

**6) Enter SATORITOKEN as the `Name` of your secret and paste on the `Secret` your `Team API Token`. You can find it going to you [Dashboard](https://satori.ci/dashboard), select your team, click on `Settings` and copy your `Team API token`**

![](img/github_action_6.png)

Click on **`Add Secret`**
