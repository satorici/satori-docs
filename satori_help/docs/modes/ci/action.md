# Satori CLI on Github Actions

If you want to test part of your workflow with Satori:

1) Include as part of your workflow the Satori Job:
```yml
name: Satori CLI Action
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
          satori-cli config token $SATORITOKEN
          satori-cli run ./ -s
```

2) Go to your repository `Settings`

3) Click on `Secrets and variables` and then on `Actions`

4) Click on `New repository secret`

5) Enter SATORITOKEN as the `Name` of your secret

6) Paste on the `Secret` your `User API Token` (https://www.satori-ci.com/user-settings/)

7) Click on `Add Secret`
