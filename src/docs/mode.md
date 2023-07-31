# [Intro](README.md)
## Execution Mode

Satori is a testing platform that can:
- Run on demand, 
- on CI/CD,
- and scheduled, also known as monitoring

### [Run](run.md)

You can run your playbooks on demand with Satori CLI whenver you want to:
- Run a playbook that is not related to a repository. For example, you want to stress test a server or assert what is the status of previously found vulnerabilities of a penetration test.
- Upload a directory with a playbook to test its content. This is particularly useful when working with code that is not part of a cloud repository, for example when using Jenkins.

### CI

Whenever you want to test your software automatically, you can use Satori as part of a CI/CD pipeline with:
- [Satori GitHub CI](github_ci.md)
- [Satori CLI running on Github Actions or Jenkins](github_action.md)

Tests can range from static to dynamic testing of your code.

### [Monitor](monitor.md)

Certain tests must be executed with a certain frequency. For example:
- Every 5 minutes when you are testing if your live systems are working as expected
- Daily when you are monitoring the security of an AWS environment

If you need any help, please reach out to us on [Discord](https://discord.gg/F6Uzz7fc2s) or via [Email](mailto:support@satori-ci.com)
