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

Monitors allow you to automate scheduled checks on systems, ensuring they function correctly over time. 
You can set your playbooks to run at regular intervals, defined by a time rate (e.g., '5 minutes')
Monitors can be viewed via the [Web interface](https://www.satori.ci/monitors/), the CLI (`satori monitors`), or [Grafana](https://github.com/satorici/satori-plugin-grafana).

## [Notifications](notifications.md)

We offer a flexible notification system to keep your team updated about the satatus of your projects. We support a variety of communication methods:

- Slack
- Discord
- Email
- Telegram
- Github Issues

You can define these notifications within your [dashboard settings](https://satori.ci/dashboard/) and set notification preferences in your project’s satori.yml file. Specify the conditions under which you want to be notified, whether on a failure or a success.

## [Reports](getting-started/execution-data.md)

We process the *output* to generate *reports* based on the *files* that were produced. To help you track changes over time, we can highlight differences between consecutive reports. This feature is useful for identifying whether you are fixing existing bugs or introducing new ones.
You can access your reports using on the [reports section of the Web](https://www.satori-ci/reports/) or with the CLI: `satori reports`.

## Support

If you need any help, please reach out to us on [Discord](https://discord.gg/NJHQ4MwYtt) or via [Email](mailto:support@satori-ci.com)
