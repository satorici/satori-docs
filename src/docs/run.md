# [Intro](README.md)
## Run

Satori is an automatic testing platform that can run tests on demand with the `run` command. By default, it works asynchronous by launching the process in background and providing a report ID that can be followed up to get the results of the test. If synchronous execution is required, either because the execution may block future actions or because you want to get the report or the output that will be generated, that can 

--sync: returns a short response
--report: TBC
--output: TBC

There are some general guidances on Run:
- Executions run asynchronous by default or synchronous with the parameter `--report` and `--output`

### Non-Repo
**Local Playbook**
Run allows you to run Satori Playbooks on demand. Whenever your playbook by itself is enough, you can simply run it with:

```sh
satori-cli run playbook.yml
```

You would run it like this when:
- you are developing a playbook and you are debugging its [report and output](report.md)
- it is a playbook that needs to be run ocasionally. For example, you want to test something with `curl` that showed up as part of a pentest and you want to verify that is fixed on a certain system automatically.
- that will become a [monitor](monitor.md) once the `cron` or `rate` is introduced in `settings`. 

**Local Directory with Playbook**
In case you are working on a directory with source code, where you are interested in understanding how the files behave with the code, you want to save your playbook as `.satori.yml` and then run:

```sh
satori-cli run ./
```

You would run it like this when:
- your code lives locally, before it is being pushed to a [repo](repo.md)
- your code lives remotely, and you are executing it within a [GitHub Action or as part of a Jenkins process](action.md)

**Public Playbook**
You can run on demand public playbooks. You can see a list of the publicly available playbooks with: `satori-cli playbook --public`

And then you can execute them like this:
```sh
satori-cli run --playbook satori://some/playbook.yml
```

You would run it like this when there is a public playbook that already addresses your problem. 

