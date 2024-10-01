# Execution modes

Satori is an automated testing platform that offers multiple ways to execute tests, allowing flexibility for different testing needs. You can run tests in the following modes:

  - **On demand:** execute tests manually when needed.
  - **As part of a CI/CD process:** integrate automated tests into your CI/CD pipeline.
  - **Scheduled (also known as monitors):** set up tests to run at specific intervals, allowing continuous monitoring of your environments.
  - **On Your Repositories:** run tests directly on the code within your repositories.

## [Run](run.md)

You can execute your playbooks on demand using the Satori CLI in several scenarios:

  **- Creating a new playbook:** run the command `satori run playbook.yml` to test the playbook during its creation.
  
  **- Running locally:** use `satori local -p playbook.yml` to execute your playbook on your local machine.
  
  **- Verifying production issues:** check if issues found in your testing environment persist in production.
  
  **- Testing offline code:** upload a directory with a playbook to test its content when working with non-cloud repositories.

## CI

To automate software testing as part of a CI/CD pipeline, Satori offers several integration options:

  **- [Github Application](https://github.com/apps/satorici):** analyze your repositories automatically by using the Satori GitHub App.
  
  **- [GitHub Action](ci/action.md):** implement automated tests in your GitHub workflows with the Satori CLI.
  
  **- [Gitlab](ci/gitlab.md):** use the Satori CLI within your GitLab CI pipeline to automate testing.
  
  **- [Jenkins](ci/jenkins.md):** add the Satori CLI to your Jenkins pipeline for continuous automated testing.

Satori supports a wide range of tests, from static code analysis to dynamic testing of live applications. 

## [Monitor](monitor.md)

Satori allows you to schedule and run tests at specific intervals to continuously monitor your systems. This ensures that issues can be detected and addressed in real-time. Examples of scheduled testing include:
  
  **- Every 5 minutes:** to get notified in case your production systems are not working as expected.
  
  **- Daily security checks:** regularly monitor the security of your AWS environment, ensuring your infrastructure remains secure.

When using remote playbooks running on live containers, you can define specific assertions about your services, such as:

  - Is your domain name resolving to the correct IP address?
  
  - Is your login page functioning correctly with the provided testing credentials?
  
  - Is your mail server successfully delivering emails?

## [Scan](scan.md)

Satori allows you to run a playbook across all repositories associated with a specific account. You can choose between two scanning methods:

**- Latest commits scan:** quickly analyze the most recent commits in all your repositories to identify any that do not adhere to the expected assertions.

**- Deep Scan of All Commits:** conduct a comprehensive scan of all commits in your repositories. 

---

