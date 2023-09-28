# Teams

By default you are a member of your own Private team. Here is where your repositories and monitors will be by default. Teams allow you to group monitors, repositories and people with their own notifications channels.

## Create a Team

This is how you would create the TeamName team:

```sh
$ satori team TeamName create
```

#### List Members

You can list the members of your teams like this:

```sh
$ satori team Private members
```

#### Add Member

If the user's email is part of Satori CI, it will be automatically added. Otherwise, they will receive an invitation to join your team.

```sh
$ satori team Private add member="member_email@yourdomain.com"
```

#### List Repos

You can list the repositories of your team like this:

```sh
$ satori team Private repos
```

#### Add Repo

Include within your team a certain repo:

```sh
$ satori team Private add repo="GithubAccount/Repository"
```

#### Add Account Repositories

Include within your team all the repositories of a certain account:

```sh
$ satori team Private add repo="GithubAccount/*"
```

#### List Monitors

You can list the monitors of your team like this:

```sh
$ satori team Private monitors
```

#### Add Monitor

Include within your team the monitor ID mABC123:

```sh
$ satori team Private add monitor="mABC123"
```

## Delete a Team

You can remove a team like this:

```sh
$ satori team TeamName delete
```

## Notifications

You can get the following notification configurations:

- slack_workspace
- slack_channel
- discord_channel
- notification_email

And it would be used like this:

```sh
$ satori team SatoriCI get_config discord_channel
Satori CI 1.2.51 - Automated Software Testing Platform - Started on 2023-07-03 16:50:40
discord_channel: 87654
```

The previous value, was defined like this:

```sh
$ satori team Private set_config discord_channel 87654
True
```
