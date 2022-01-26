from datetime import datetime
from logging import lastResort
import os
import pytz
from mcstatus import MinecraftServer
import requests
from dotenv import load_dotenv

load_dotenv()
SERVER_ADDRESS = os.getenv('SERVER_ADDRESS')
LAST_STATUS_FILE_NAME = os.getenv('LAST_STATUS_FILE_NAME')
DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')
DISCORD_USERNAME = os.getenv('DISCORD_USERNAME')
DISCORD_AVATAR_URL = os.getenv('DISCORD_AVATAR_URL')

print("getting timezone")
CST = pytz.timezone('America/Chicago')
print("getting time")
CURRENT_DATETIME = datetime.now(CST)


def check_server():
    print("checking server")
    # Get the current server info
    server = MinecraftServer.lookup(SERVER_ADDRESS)
    # 'players' has attributes 'max', 'names' and 'online' (count)
    players = server.query().players
    # number of online players
    online = players.online
    # a list of the name strings
    names = players.names

    return names


def load_last_status():
    # loads last player name list
    # if no file, or file is blank, returns []
    names = []
    
    print("getting current working directory")
    if os.path.isfile(LAST_STATUS_FILE_NAME):
        try:
            last_status_file = open(LAST_STATUS_FILE_NAME, 'r')
            names = last_status_file.read().split(',')
            last_status_file.close()
        except Exception as e:
            print(e.with_traceback)
    return names


def update_last_status(names):
    # updates the last status file w/ online and names list
    last_status_file = open(LAST_STATUS_FILE_NAME, 'w')
    last_status_file.write(','.join(names))
    last_status_file.close()


def message_discord(names):
    # sends a message to discord
    message = "⛔ No current online players. ⛔"
    if len(names) == 1:
        message = f"🚶‍♂️ Current player: {', '.join(names)} 🚶‍♂️"
    if len(names) > 1:
        message = f"👯‍♂️ Current players: {', '.join(names)} 👯‍♂️"

    data = {
        "username": DISCORD_USERNAME,
        "avatar_url": DISCORD_AVATAR_URL,
        "content": message
    }
    headers = {
        "Content-Type": "application/json",
        "charset": "utf-8"
    }
    response = requests.post(DISCORD_WEBHOOK_URL, headers=headers, json=data)


def main():
    names = check_server()
    last_names = load_last_status()

    names.sort()
    # last_names dont need to be sorted since they were sorted before being saved
    if names == last_names:
        # lists are the same
        print(f"{CURRENT_DATETIME} - lists are the same. Current online players - {', '.join(names)}")
    else:
        # lists are not the same
        print(f"{CURRENT_DATETIME} - the lists are different. Current online players - {', '.join(names)}")
        update_last_status(names)
        message_discord(names)
    

if (__name__ == "__main__"):
    main()