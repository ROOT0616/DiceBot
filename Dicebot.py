
import random
import discord
from discord.ext import commands
import json
import os

# Read configuration from an external file
config_path = '/home/game/Dicebot/config.json'

# Error handling for missing or invalid config file
try:
    with open(config_path, 'r') as file:
        config = json.load(file)
except FileNotFoundError:
    print("Error: config.json file not found.")
    exit(1)
except json.JSONDecodeError:
    print("Error: config.json is not a valid JSON file.")
    exit(1)

# Get the bot token from the configuration
try:
    BOT_TOKEN = config["TOKEN"]
except KeyError:
    print("Error: BOT_TOKEN is not found in config.json.")
    exit(1)

# Read HELP_MESSAGE from an external file or from config.json
try:
    HELP_MESSAGE = config["HELP_MESSAGE"]
except KeyError:
    print("Warning: HELP_MESSAGE is not found in config.json. Using default value.")
    HELP_MESSAGE = """
    /d1, /d2, /d3 で1から3回の6面のサイコロを振ります。
    /d00 で1回の100面のサイコロを振ります。/r 回数d面数で、指定した回数と面数のサイコロを振ります。回数は1から10、面数は2から100で指定してください。
    """


# Functions
def format_dice_result(result, faces, times):
    """Format the dice roll result."""
    return f'{times}d{faces}: ' + ' + '.join(result) + f' = {sum(map(int, result))}'

async def send_dice_result(message, faces, times):
    """Send the dice roll result to the channel and print it."""
    result = [str(random.randint(1, faces)) for _ in range(times)]
    formatted_result = format_dice_result(result, faces, times)
    await message.channel.send(f'<@{message.author.id}>' + formatted_result)
    print(f'<@{message.author.id}>' + formatted_result)

async def send_error(message, error_message):
    """Send an error message to the channel."""
    await message.channel.send(f'<@{message.author.id}> Error: {error_message}')

async def handle_roll_command(message, command, faces, default_times=1):
    times_str = command[len(command.split(' ')[0]):]
    if times_str:
        try:
            times = int(times_str)
        except ValueError:
            await send_error(message, f'回数は整数で入力してください。コマンド: {command}')
            return
    else:
        times = default_times

    if 1 <= times <= 10:
        await send_dice_result(message, faces, times)
    else:
        await send_error(message, '1から10の回数で振ってください')

async def handle_custom_roll_command(message, command):
    try:
        parts = command.split(' ')
        times, faces = map(int, parts[1].split('d'))
        if 1 <= times <= 10 and 2 <= faces <= 100:
            await send_dice_result(message, faces, times)
        else:
            await send_error(message, '回数は1から10、面数は2から100で指定してください')
    except ValueError:
        await send_error(message, '無効なコマンド形式です。使用方法: /r 回数d面数')

async def handle_command(message):
    if client.user == message.author:
        return  # Ignore messages from the bot itself
    content = message.content
    if content.startswith("/dhelp"):
        await message.channel.send('<@' + str(message.author.id) + '>' + HELP_MESSAGE)
        print('<@' + str(message.author.id) + '>' + HELP_MESSAGE)
    elif content.startswith("/d1"):
        await handle_roll_command(message, content, 6, 1)
    elif content.startswith("/d2"):
        await handle_roll_command(message, content, 6, 2)
    elif content.startswith("/d3"):
        await handle_roll_command(message, content, 6, 3)
    elif content.startswith("/d00"):
        await handle_roll_command(message, content, 100, 1)
    elif content.startswith("/r "):
        await handle_custom_roll_command(message, content)

# Main
intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    await handle_command(message)

client.run(BOT_TOKEN)
