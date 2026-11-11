# Organizations

An **organization** is an account shared by its members. Its jobs, reports, issues, advisories, monitors, scans and saved parameters belong to the organization, not to the user who created them, so every member works on the same data.

By default, every command acts on your own account. To act on an organization, select it as described in [Selecting an organization](#selecting-an-organization).

## Listing and creating organizations

```sh
satori-v2 organizations
```

Lists the organizations you are a member of, with their ID, name, plan and your role.

To create one, your account must have the ENTERPRISE plan. You become its `OWNER`. Creating an organization does not switch to it:

```sh
satori-v2 organizations create Acme
satori-v2 organization 7 use
```

## Selecting an organization

You can select the organization to act on in three ways. From highest to lowest precedence:

| How | Scope | Example |
| --- | --- | --- |
| `--org ORG` at the end of a command | That command only | `satori-v2 run ./ --org 7`, `satori-v2 report V1StGXR8Z5jdHi6BmyT2k --org Acme` |
| `SATORI_ORGANIZATION` environment variable | Every command in that environment | `SATORI_ORGANIZATION=7 satori-v2 jobs` |
| Saved in the profile | Every following command of that `--profile` | `satori-v2 config organization Acme` or `satori-v2 organization 7 use` |

`--org` and `config organization` accept an ID or a name. The name match is case-insensitive and must match exactly one of your organizations; if several share the name, use the ID. `SATORI_ORGANIZATION` only accepts an ID.

To show the organization saved in the profile, or to go back to your own account:

```sh
satori-v2 config organization          # prints "7 (Acme)"
satori-v2 config organization none     # or: config organization personal, or: satori-v2 organizations personal
```

`satori-v2 whoami` also shows the selected organization, with its name and ID.

In CI, set `SATORI_ORGANIZATION` next to `SATORI_TOKEN` so the pipeline's jobs belong to the organization.

## Managing an organization

| Command | Who | Description |
| --- | --- | --- |
| `satori-v2 organization ORG-ID` | Members | Show the organization and your role |
| `satori-v2 organization ORG-ID use` | Members | Act on it in the following commands (saved per `--profile`) |
| `satori-v2 organization ORG-ID members` | Members | List members (user ID, name, email, role) |
| `satori-v2 organization ORG-ID rename NAME` | OWNER, ADMIN | Rename it |
| `satori-v2 organization ORG-ID add EMAIL [--role ROLE]` | OWNER, ADMIN | Add a user who has already logged in to Satori (default `MEMBER`) |
| `satori-v2 organization ORG-ID role USER-ID ROLE` | OWNER, ADMIN | Change a member's role |
| `satori-v2 organization ORG-ID remove USER-ID` | OWNER, ADMIN; anyone for themselves | Remove a member, or leave the organization with your own user ID |
| `satori-v2 organization ORG-ID delete` | OWNER | Delete it with all of its jobs, reports and findings (asks for confirmation; add `--yes` to skip the prompt in scripts) |

Roles are `OWNER`, `ADMIN` and `MEMBER`. Only an `OWNER` can grant or revoke the `OWNER` role, and an organization always keeps at least one `OWNER`: to get rid of the last one, delete the organization instead.

```sh
satori-v2 organization 7 add alice@example.com --role ADMIN
satori-v2 organization 7 members
satori-v2 organization 7 role 42 MEMBER
satori-v2 organization 7 remove 42
```

## API and MCP

The CLI sends the selected organization in the `X-Satori-Organization` header. Send the same header (with the organization ID) to act on an organization through the API:

```sh
curl -H "Authorization: Bearer $SATORI_TOKEN" -H "X-Satori-Organization: 7" https://api-v2.satori.ci/jobs
```

The MCP server has equivalent tools (`list_organizations`, `use_organization`, `use_personal_account`, and others) and shares the organization saved in the CLI configuration. See [MCP Tools](modes/mcp/tools.md).
