# Minecraft Player Status Discord Messenger

## What this program does

This program messeges a list of the current online players from a specified minecraft server to a Discord webhook.

---
## Required Packages
- mcstatus
- python-dotenv
## How this program works
This program works roughly as follows:
1. Load .env variables
2. Query the specified Minecraft server
   1. Note: The Minecraft server must have `enable-query=true` set in it's `server.properties` file for this program to be able to query player names.
3. Compares the returned names to the returned names from the previous query.
4. If they are different, a message will be send to the specified Discord channel webhook.
5. The latest player names are logged.
---
## Setup
For this program to work, you will need to create a file names `.env` in the same directory containing the configuration info.
The file may contain the following:
|Variable Name | Required | Definition | Example Value |
|--------------|------------|---------------|----------|
|SERVER_ADDRESS | yes | Minecraft server IP Address or URL, including port number if different than 25565|51.178.221.10|
|LAST_STATUS_FILE_NAME | yes | name of the file to store the player name list after query for future comparison | names.txt |
|DISCORD_WEBHOOK_URL | yes | webhook for the discord channel the message will be sent to - more info [here](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks) | https://discord.com/api/webhooks/120643/acc8as80acdae |
| DISCORD_USERNAME | yes | username shown in Discord channel when message is sent | mc-status-bot |
| DISCORD_AVATAR_URL | no | URL of image to be shown in Discord when message is sent | www.picbin.com/apple.jpg |

So an empty `.env` file would look like this:
```
SERVER_ADDRESS=
LAST_STATUS_FILE_NAME=
DISCORD_WEBHOOK_URL=
DISCORD_USERNAME=
DISCORD_AVATAR_URL=
```
---

Shoutout to https://choosealicense.com/licenses/ for making open source software licences more approachable.