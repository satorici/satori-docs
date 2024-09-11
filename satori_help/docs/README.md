<p align="center"><img src="https://satori.ci/wp-content/themes/satorici/assets/images/logo.svg" alt="Satori CI Logo" style="width:200px;"/></p>

# Intro

Satori CI is an automated testing platform designed to validate the behavior of command executions through assertions. It allows to perform testing on software applications, binaries, and live systems using pre-built [playbooks](https://github.com/satorici/playbooks/) or creating own custom playbooks. Satori CI is a versatile tool for in-depth project testing.

## [Install](getting-started/install.md)

Satori offers flexible execution options for your tests, allowing them to run either synchronously or asynchronously.
- Use our [CLI tool](https://github.com/satorici/satori-cli), which will allow you to execute tests directly from your terminal installed with `pip install satori-ci`.
- Using the [Web](https://satori.ci) Interface, you can use our web interface to manage and execute your tests without any installation required.

## CI

You can integrate Satori with various CI/CD tools:
- Our [Github Application](https://github.com/apps/satorici) to analyze your repositories
- A [GitHub action](modes/ci/action.md) using the Satori CLI.
- A [Gitlab](modes/ci/gitlab.md) using the Satori CLI.
- A [Jenkins](modes/ci/jenkins.md) using the Satori CLI.


## [Playbook's language](playbooks/language.md)

Our YAML-based [language](playbooks/language.md) allows you to define [executions](playbooks/execution.md), specify their [inputs](playbooks/inputs.md), and [assert](playbooks/asserts.md) whether their behavior aligns with your expectations. Tests are encapsulated within files called playbooks, with different [settings](playbooks/settings.md) depending on the [execution mode](modes/modes.md): Run, CI, Scan, and/or Monitor.

All our tests are stored in what we call playbooks. You can check our online playbooks in our [Github repository](https://github.com/satorici/playbooks/) for our public marketplace.

## [Repositories](repo.md)

We provide a comprehensive approach to testing code repositories on Github. Whether your repositories are attached to our CI process or not, you can perform tests on one or all of your repositories to assert their correctness (e.g., ensuring no passwords are stored, that software is being built and executed correctly, and that secure coding standards are followed). You can visualize the results using our [Web interface](https://satori.ci/repos/) or with our CLI (`satori repos`).

## [Monitor](modes/monitor.md)

Your playbooks can run at a certain rate. The frequency is defined within the settings with a certain rate (ie, '5 minutes') or using the cron format (ie, '*/5 * * * *'). 

You can view your monitors using the [Web interface](https://www.satori.ci/monitors/), the CLI (`satori monitors`), or [Grafana](https://github.com/satorici/satori-plugin-grafana).

## [Notifications](notifications.md)

We will notify you according to your preferences. We support a variety of communication methods:

- Slack
- Discord
- Email
- Telegram
- Github Issues

You can define these notifications within your [Team settings](https://www.satori-ci.com/team-settings/)

## Reports

We process the *output* to produce *reports* based on the *files* that were generated. We can also let you know about the difference between consecutive reports to identify whenever you are fixing -or introducing new- bugs. You can access your reports using on the [reports section of the Web](https://www.satori-ci.com/reports/) or with the CLI: `satori reports`.

## Support

If you need any help, please reach out to us on [Discord](https://discord.gg/NJHQ4MwYtt) or via [Email](mailto:support@satori-ci.com)
