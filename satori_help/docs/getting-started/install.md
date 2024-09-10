---
next:
  text: 'Hello World Test'
  link: '/getting-started/hello_world'
---

# Install

We offer various installation options and integrations to fit your development workflow. You can connect Satori via CLI, which can be installed using pip, or integrate it with your [Github Application](../modes/ci/github.md). Additionally,we support integration with other CI/CD platforms such as  [Gitlab](../modes/ci/gitlab.md), [Jenkins](../modes/ci/jenkins.md), and [Github Actions](../modes/ci/action.md). To enhance your experience and better visualize of your test results, we provide ca user-friendly web interface <https://satori.ci>, to better visualize your test results.

## Install Satori CLI
**Step 1: Install the Satori-CI CLI**

Open your command line terminal and execute the following command to install the Satori CLI:

```console
pip3 install satori-ci
```

![PiPY install](img/install_1.png)

**Step 2: Obtain Your Satori Token**

To use Satori-CI, you need to get your API Token. Follow these steps:

1. Log in to the Satori website using your GitHub credentials at [https://satori.ci/login](https://satori.ci/login).
2. Navigate to `Settings` -> `Teams`.
3. Copy your API Token.

**Step 3: Configure Satori-CI**

Replace the placeholder `YOUR_TOKEN` on the next command with the API Token you copied in the previous step :

```console
satori config token YOUR_TOKEN
```

![Satori CLI Config Token](img/install_2.png)

## Install Satori CI Github App

To ensure the security of your project and minimize the risk of exposing sensitive information, you can automatically test your GitHub repositories by installing the Satori CI GitHub App. Follow these steps:

**Step 1: Install the Satori CI GitHub App**

1. Go to the [Satori CI GitHub App page](https://github.com/apps/satorici). Make sure you are authenticated with GitHub to proceed with the installation.
   
![Satori CI Github Install](../modes/ci/img/github_1.png)
   
2. Click on **Configure**.
   
![Install Satori CI on your account](../modes/ci/img/github_2.png)

3. Choose the GitHub accounts where you want to set up the Satori CI App.
4. Select the repositories where you want to install the app. You can choose specific repositories or select **All repositories**.
   
![Select your Github repositories where you will use Satori](../modes/ci/img/github_3.png)

Once you are done, click on **Save**. We care about your security, so we will only store your email, your repositories names, and the reports. Your code only lives within the virtual machines that are present during the execution.

---
### Next Steps

Now that the Satori CI GitHub App is installed and configured, you can proceed to learn how to test a "[Hello World](../getting-started/hello_world.md)" example to get started with practical testing

---

If you need any help, please reach out to us on [Discord](https://discord.gg/NJHQ4MwYtt) or via [Email](mailto:support@satori-ci.com)
