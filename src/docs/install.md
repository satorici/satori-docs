# Intro
## Install

### Install Satori CLI

Three steps:
1. Execute on your command line terminal:

```console 
pip3 install satori-ci
```

2. With Satori CLI installed, now we need to get a Satori Token to use it:

 * Log in the Satori website using Github credentials: https://www.satori-ci.com/login
 * On the Satori website go to User Settings 
 * Copy your User API Token

3. Replace the string YOUR_TOKEN with your clipboard on the next command: 

```console 
satori-cli config token YOUR_TOKEN`
```

### Install Satori CLI inside a Github Action

TBC

### Install Satori CI Github App

We tested on demand. Now let's do it as part of your regular Github CI process. 

1. Go to https://github.com/apps/satorici

2. Click on Install

3. Select the repositories where you will be installing it or select all repositories

By default you can get notifications via email and Github issues. If you want to get notified in slack, discord or telegram go to https://www.satori-ci.com/user-settings/ to define their details. 


If you want to detail in your playbook to be notified when the scans are ready, add the following to them:

```yml
settings:
  log|logOnFail|logOnPass: slack|email|issue|discord|telegram
```

For example:
```yml
settings:
    logOnFail: slack
  
test:
    assertStdoutEqual: Hello World
    python:
    - [ python hello_world.py ]
```

and put it on a file named .satori.yml inside your repository.

