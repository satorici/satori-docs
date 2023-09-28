# Intro

Satori CI is an Automated Cloud Testing platform that asserts the behavior of command executions. Start testing software and systems using our simple one-liners from our Playbook marketplace.

Head to https://www.satori-ci.com, setup your account using GitHub and start testing with Satori.

## [Install](getting-started/install.md)

Satori can execute tests synchronously or asynchronously:

- Use our [CLI tool](https://github.com/satorici/satori-cli), which can be installed with `pip install satori-ci`.
- Use our [Website](https://www.satori-ci.com).

## [Language](playbooks/language.md)

Our YAML-based [language](playbooks/language.md) allows you to define [executions](playbooks/execution.md), specify their [inputs](playbooks/inputs.md), and [assert](playbooks/asserts.md) whether their behavior aligns with your expectations. Tests are encapsulated within files called playbooks, with different [settings](playbooks/settings.md) depending on the [execution mode](modes/modes.md): Run, CI, Scan, and/or Monitor.

All our tests are stored in what we call playbooks. You can check our online playbooks in our [Github repository](https://github.com/satorici/playbooks/) for our public marketplace.

## CI
You can use Satori with:
- Our [Github Application](https://github.com/apps/satorici) to analyze your repositories
- A [GitHub action](modes/ci/action.md) using the Satori CLI.
- A [Gitlab](modes/ci/gitlab.md) using the Satori CLI.
- A [Jenkins](modes/ci/jenkins.md) using the Satori CLI.
  
## [Repositories](repo.md)

We provide a comprehensive approach to testing code repositories on Github. Whether your repositories are attached to our CI process or not, you can perform tests on one or all of your repositories to assert their correctness (e.g., ensuring no passwords are stored, that software is being built and executed correctly, and that secure coding standards are followed). You can visualize the results using our [Web interface](https://www.satori-ci.com) or with our CLI (`satori repo`).

## [Monitor](modes/monitor.md)

It's worth noting that you can define a `cron` or `rate` for your playbooks. The frequency may be significant for different types of tests, especially when you want to monitor their status. You can later review the results using our [Web interface](https://www.satori-ci.com), the CLI (`satori monitor`), or [Grafana](TBC).

## [Notifications](notifications.md)

We will notify you when and how you prefer. We support a variety of communication methods:

- Slack
- Discord
- Email
- Telegram
- Github Issues

You can define these notifications within your [Team settings](https://www.satori-ci.com/team-settings/)

## [Reports](reports.md)

We process the *output* to produce *reports* based on the *files* that were generated. We can also let you know about the difference between consecutive reports to identify whenever you are fixing -or introducing new- bugs. You can access your reports using on the [reports section of the Web](https://www.satori-ci.com/reports/) or with the CLI: `satori report`.

## Support

If you need any help, please reach out to us on [Discord](https://discord.gg/F6Uzz7fc2s) or via [Email](mailto:support@satori-ci.com)
