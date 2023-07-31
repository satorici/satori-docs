# [Intro](README.md)
## Gitlab CI/CD:

First define the following action for your Gitlab CI/CD process, to evaluate your code:

```yml
image: python:latest

variables:
  SATORI_TOKEN: $SATORI_TOKEN

SatoriCI:
  stage: build
  script:
    - pip3 install satori-ci
    - satori-cli config token $SATORI_TOKEN -p default
    - satori-cli upload ./
```

Define the `$SATORI_TOKEN` value in **Settings -> CI/CD -> Variables -> Expand -> Add variable**:
- **Key**: `SATORI_TOKEN`
- **Value**: `<token>`


Be mindful if you want your tests to be [asynchronous or synchronous](asynchronous_and_synchronous_executions) when executing satori-cli.