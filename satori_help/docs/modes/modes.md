# Execution modes

Satori is an automated testing platform where you can run tests:

- On demand
- As part of a CI/CD process
- Scheduled (also known as monitoring)
- And on your repositories

## [Run](run.md)

You can run your playbooks on demand with Satori CLI whenever you:

- Are creating a new testing playbook using the command `satori run playbook.yml`. You can also run your playbook locally with `satori local -p playbook.yml`.
- Want to assert if the issues found on your testing environments are present on your production servers.
- Upload a directory with a playbook to test its content. This is particularly useful when working with code that is not part of a cloud repository.

## CI

Whenever you want to test your software automatically, you can use Satori as part of a CI/CD pipeline with:

- Our [Github Application](https://github.com/apps/satorici) to analyze your repositories
- A [GitHub action](ci/action.md) using the Satori CLI.
- A [Gitlab](ci/gitlab.md) using the Satori CLI.
- A [Jenkins](ci/jenkins.md) using the Satori CLI.

The automated testing can range from static analysis to dynamically testing live applications.

## [Monitor](monitor.md)

Certain tests have to be executed with a certain frequency. For example:

- Every 5 minutes to get notified in case your production systems are not working as expected
- Daily when you are monitoring the security of an AWS environment

Since your remote playbooks are run on live containers, you can define specific assertions about your services, such as:

- Is your domain name responding with the right IP address?
- Is your login page working with testing credentials?
- Is your mail server delivering mail?

## [Scan](scan.md)

You can run a playbook against all the repositories of a certain account. Scanning either the latests commits of all your repos, or deep scanning all the commits of your repositories to expose the commits that are not following the expected assertions.

If you need any help, please reach out to us on [Discord](https://discord.gg/NJHQ4MwYtt) or via [Email](mailto:support@satori-ci.com)
