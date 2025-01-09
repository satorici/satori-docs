---
next:
  text: 'Hello World Test'
  link: '/getting-started/hello_world'
---

# Install

We offer various installation options and integrations to fit your development workflow. You can connect Satori via CLI, which can be installed using pip, or integrate it with your [Github Application](../modes/ci/github.md). Additionally, we support integration with other CI/CD platforms such as  [Gitlab](../modes/ci/gitlab.md), [Jenkins](../modes/ci/jenkins.md), and [Github Actions](../modes/ci/action.md). To enhance your experience and better visualize your test results, we provide a user-friendly web interface <https://satori.ci>.

## Install Satori CI Github App

We recommend that you use your Github account to automatically test your repositories. You can create an account without Github, but that won't allow you to scan for repositories' bugs. 

**Step 1: Install the Satori CI GitHub App**

1. Go to the [Satori CI GitHub App page](https://github.com/apps/satorici). Authenticate with GitHub to proceed with the installation.
   
![Satori CI Github Install](../modes/ci/img/github_1.png)
   
2. Click on **Configure**.
   
![Install Satori CI on your account](../modes/ci/img/github_2.png)

3. Choose the GitHub accounts where you are installing the Satori CI App.
4. Select the repositories where you want to install the app. We recommend to select **All repositories**.
   
![Select your Github repositories where you will use Satori](../modes/ci/img/github_3.png)

Once you are done, click on **Save**. 

If you are pushing code, we will check it with the repository playbooks and the default playbooks defined. Your code only lives within the virtual machines that are present during the execution, it only remains on your Github account.

---


## Install Satori CLI

The CLI interface is the best way to interact with Satori. New functionalities get pushed here first, and that allow us to test ourselves before pushing the new features to the web. 

**Step 1: Install the Satori-CI CLI**

Open your command line terminal and execute the following command to install the Satori CLI:

```console
pip3 install satori-ci
```

![PiPY install](img/install_1.png)

**Step 2: Obtain Your Satori Token**

To use Satori-CI, you need to get your API Token. Follow these steps:

0. Log in to the Satori website [https://satori.ci/login](https://satori.ci/login).
1. Navigate in the Satori CI website to your Profile.
2. Copy your API Token.

**Step 3: Configure Satori-CI**

Replace the placeholder `YOUR_TOKEN` on the next command with your Satori CI API Token:

```console
satori config token YOUR_TOKEN
```

![Satori CLI Config Token](img/install_2.png)

### Next Steps

Learn how to automatically test "[Hello World](../getting-started/hello_world.md)".

---

If you need any help, please reach out to us on [Discord](https://discord.gg/NJHQ4MwYtt) or via [Email](mailto:support@satori-ci.com)
