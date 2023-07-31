# Intro

Satori is an automated testing platform designed to assert the behavior of command executions. You can test software and systems using simple one-liners from our Playbook marketplace.


## [Install](install.md)

Satori can execute tests [synchronously or asynchronously](asynchronous_and_synchronous_executions.md) in various ways:
- With our [Github Application](https://github.com/apps/satorici) to analyze your [repositories](repo.md).
- With our [CLI tool](https://github.com/satorici/satori-cli), which can be installed with `pip install satori-ci`.
- Through our [Website](https://www.satori-ci.com).
- Within a [GitHub action](action.md) using the Satori CLI.
- On-demand using [Satori CLI Run](run.md).

## [Language](language.md)

Our YAML-based [language](language.md) allows you to define [executions](language_execution.md), specify their [inputs](language_inputs.md), and [assert](language_asserts.md) whether their behavior aligns with your expectations. Tests are encapsulated within files called [playbooks](language_playbooks.md), with different [settings](language_settings.md) depending on the [execution mode](mode.md): [Run](run.md), [Github CI](github_ci.md), and/or [Monitor](monitor.md).

All our tests are stored in what we call playbooks. You can check our online playbooks in our [Github repository](https://github.com/satorici/playbooks/) for our public marketplace.

## [Repo](repo.md)

We provide a comprehensive approach to testing code repositories on Github. Whether your repositories are attached to our CI process or not, you can perform tests on one or all of your repositories to assert their correctness (e.g., ensuring no passwords are stored, that software is being built and executed correctly, and that secure coding standards are followed). You can visualize the results using our [Web interface](https://www.satori-ci.com) or with our CLI (`satori-cli repo`).

## [Monitor](monitor.md)

It's worth noting that you can define a `cron` or `rate` for your playbooks. The frequency may be significant for different types of tests, especially when you want to monitor their status. You can later review the results using our [Web interface](https://www.satori-ci.com), the CLI (`satori-cli monitor`), or [Grafana](TBC).

## [Notifications](notifications.md)

We will notify you when and how you prefer. We support a variety of communication methods:
- Slack
- Discord
- Email
- Telegram
- Github Issues

You can define these notifications within your [Team settings](https://www.satori-ci.com/team-settings/)

## [Reports](reports.md)

We process the [output](output.md) to produce [reports](reports.md) based on the [files](files.md) that were generated. We can also let you know about the difference between consecutive reports to identify whenever you are fixing -or introducing new- bugs. You can access your reports using on the [reports section of the Web](https://www.satori-ci.com/reports/) or with the CLI: `satori-cli report`.

## Support

If you need any help, please reach out to us on [Discord](https://discord.gg/F6Uzz7fc2s) or via [Email](mailto:support@satori-ci.com)
