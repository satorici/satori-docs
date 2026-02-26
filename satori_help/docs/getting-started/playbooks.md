# Playbooks overview

In Satori, testing procedures are defined in files known as Playbooks. These Playbooks utilize YAML syntax and are saved with the ".yml" file extension.

A Playbook may include several key components such as settings, imports, tests, executions, and asserts. Each component follows a specific language specification to ensure consistency and functionality across different Playbooks.

## Writing your first playbook

To begin testing with Satori, you first need to gather information by executing commands. These commands can produce various outputs such as stdout, stderr, return codes, and time spent.
Here’s a basic example of how to execute a command:

```yml
execute:
  - echo Hello world!
```

In this example, the command `echo Hello world!` is executed. However, to validate whether the command works as expected, you need to add assertions. For instance, you can check if the return code is zero and if the output contains a specific string:

```yml
test:
  assertStdoutEqual: "Hello world!\n"
  assertReturnCode: 0

  execute:
    - echo Hello world!
```

In this setup, you have a test that includes both execution and assertions. You can define multiple tests within a single Playbook, and tests can also be nested. For example:

```yml
test:
  assertReturnCode: 0

  nested-test:
    assertStdoutContains: Bye
    cmd:
      - echo Bye, see you later!

  execute:
    - echo Hello world!
```

In this case, the `nested-test` will check if the output contains the string "Bye" while inheriting the assertion of a zero return code from the parent `test`.

If you need to test multiple cases, you can use input references:

```yml
test:
  assertReturnCode: 0

  input:
    - Hello world!
    - See you later!

  execute:
    - echo ${{input}}
```
In this example, the `input` list provides different values to the command `echo`, allowing you to test multiple scenarios.
For more details about the [language](../playbooks/language.md) features and available [asserts](../playbooks/asserts.md).

# Running playbooks

Once you’ve created your Playbook, you need to know how to execute it. There are two primary methods for running Playbooks in Satori:

#### 1. Command Line Interface (CLI)
To run a Playbook from the command line, use the following command:

```bash
satori run hello.yml
```

![Hello World Report](img/playbooks_1.png)

This command submits your Playbook and runs it asynchronously by default. You can use additional flags like `--sync`, `--report`, `--output` or `--files` to customize the execution
For more details on CLI options and functions, refer to the [CLI Reference](../modes/run.md).

For example `--output` will display each command output: stdout, stderr, return code, etc.

![Hello World Output](img/playbooks_2.png)

## Public Playbooks

Satori provides 200+ ready-to-use playbooks covering security testing, code analysis, infrastructure scanning, and more. Browse the full catalog at [satori.ci/playbooks](https://satori.ci/playbooks) or on the [playbook repository](https://github.com/satorici/playbooks).

### Categories

| Category | Playbooks | What it covers |
|----------|-----------|----------------|
| `code/` | 72 | SAST, linting, dependency audit (Python, JS, Go, Java, Ruby, Rust, and more) |
| `web/` | 34 | DAST, crawling, fuzzing, XSS, SQLi, CMS detection, TLS testing |
| `dns/` | 17 | Subdomain discovery, DNS enumeration, takeover detection |
| `scan/` | 17 | Port scanning, banner grabbing, network reconnaissance |
| `container/` | 8 | Container image scanning, Dockerfile linting, IaC security (Terraform, Kubernetes) |
| `llm/` | 8 | Query and test LLMs (OpenAI, Gemini, Llama, Qwen) |
| `cve/` | 8 | Specific CVE detection and testing |
| `email/` | 7 | Email harvesting and OSINT |
| `secrets/` | 5 | Secret detection (Gitleaks, Trufflehog, Semgrep) |
| `monitor/` | 4 | Uptime, SSL expiry, DNS change monitoring |
| `malware/` | 4 | Antimalware scanning and anomaly detection |
| `compliance/` | 3 | OWASP Top 10, PCI-DSS, SOC2 |
| `cloud/` | 2 | AWS and multi-cloud security auditing |
| `dos/` | 2 | Load testing and slow HTTP attacks |

### Static Playbooks (SAST)

Static playbooks analyze source code without running it. They are designed to be integrated into CI processes or run against a local repository with `satori run ./`:

```bash
satori run ./ --playbook satori://code/semgrep.yml --sync --report
```

You can import multiple playbooks in a single `.satori.yml` file:

```yaml
import:
  - satori://code/semgrep.yml
  - satori://secrets/trufflehog.yml
  - satori://container/grype.yml
```

![Code example](img/code_example.png)

![SAST Output](img/sast.png)

### Dynamic Playbooks (DAST)

Dynamic playbooks test running systems by providing parameters such as a host or URL:

```bash
satori run satori://scan/nmap.yml -d HOST="target.com" --report --output
satori run satori://web/nuclei.yml -d URL="https://target.com" --report --output
satori run satori://dns/dnsx.yml -d HOST="target.com" --report --output
```

![Dast Output](img/dast_output.png)

##### 2. Continuous Integration (CI)

You can also run your Playbook automatically using GitHub. To do this:
1. Create a Playbook named `.satori.yml` in the root directory of your GitHub repository.
2. Ensure the Satori GitHub App is installed and configured for your repository.
   
With this setup, the Playbook will be executed with each push to the repository.

See more about that in [GitHub CI](../modes/ci/github.md)
For more ways to run your playbooks visit the [execution modes](../modes/modes.md) section.
