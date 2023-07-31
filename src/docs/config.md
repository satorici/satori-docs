# [Intro](README.md)
## Config

The config command is used to store configuration settings for satori-cli. The most common use case for it is the following:

```sh
$ satori-cli config token YOUR_API_TOKEN
```

Your API Token can be found on https://www.satori-ci.com/user-settings/, and it will be stored as the default token. In case of having more than one token associated, you can store it with another profile name:

```sh
$ satori-cli config token ANOTHER_API_TOKEN -p profile
```

This will create a file on your home directory called .satori_credentials.yml with the profile and its token.