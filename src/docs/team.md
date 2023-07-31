# [Intro](README.md)
## Team

By default you are a member of your private team. You can invite people to it or define new ones.

Team will allow you to group repositories and people with notifications channels.

### Create a Team

```sh
$ satori-cli team TeamName create
```

### Delete a Team

```sh
$ satori-cli team TeamName delete
```

### Members

```sh
$ satori-cli team Private members
```

### Add Member

If the user's email is part of Satori CI, it will be automatically added. Otherwise, they will receive an invitation to join the team.

```sh
$ satori-cli team Private add_member --email member_email@yourdomain.com
```

### Delete member
```sh
$ satori-cli team Private del_member --email member_email@yourdomain.com
```

### Notifications

You can get the following notification configurations:
- slack_workspace
- slack_channel
- discord_channel
- notification_email 

And it would be used like this:
```sh
$ satori-cli team SatoriCI get_config discord_channel
Satori CI 1.2.51 - Automated Software Testing Platform - Started on 2023-07-03 16:50:40
discord_channel: 87654
```

The previous value, was defined like this:
```sh
satori-cli team Private set_config discord_channel 87654
True
```
