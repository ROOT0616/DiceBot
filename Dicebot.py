import random
import discord
import json
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Read configuration from an external file
with open('config.json', 'r') as file:
    config = json.load(file)

# Constants
BOT_TOKEN = config["TOKEN"]
HELP_MESSAGE = config["HELP_MESSAGE"]
MAX_FACES = config["MAX_FACES"]
MIN_FACES = config["MIN_FACES"]
MAX_ROLLS = config["MAX_ROLLS"]
MIN_ROLLS = config["MIN_ROLLS"]

# Helper Functions
def format_dice_result(result, faces, times):
    return f'{times}d{faces}: ' + ' + '.join(result) + f' = {sum(map(int, result))}'

async def send_dice_result(message, faces, times):
    result = [str(random.randint(1, faces)) for _ in range(times)]
    await message.channel.send('<@' + str(message.author.id) + '>' + format_dice_result(result, faces, times))
    logging.info('@' + str(message.author) + ' ' + format_dice_result(result, faces, times))

async def send_error(message, error_message):
    await message.channel.send('<@' + str(message.author.id) + '>' + f"エラー: {error_message}")
    logging.error('@' + str(message.author) + ' ' + f"エラー: {error_message}")

# Command Handlers
async def handle_d_command(message, faces, default_times=1):
    times_str = message.content.split(' ')[-1]
    try:
        times = int(times_str) if times_str.isdigit() else default_times
        if MIN_ROLLS <= times <= MAX_ROLLS:
            await send_dice_result(message, faces, times)
        else:
            await send_error(message, f'回数は{MIN_ROLLS}から{MAX_ROLLS}で指定してください')
    except ValueError:
        await send_error(message, '無効な回数です')

async def handle_custom_roll_command(message):
    try:
        parts = message.content.split(' ')
        times, faces = map(int, parts[1].split('d'))
        if MIN_ROLLS <= times <= MAX_ROLLS and MIN_FACES <= faces <= MAX_FACES:
            await send_dice_result(message, faces, times)
        else:
            await send_error(message, f'回数は{MIN_ROLLS}から{MAX_ROLLS}、面数は{MIN_FACES}から{MAX_FACES}で指定してください')
    except ValueError:
        await send_error(message, '無効なコマンド形式です。使用方法: /r 回数d面数')

async def handle_command(message):
    if message.author == client.user:
        return  # Ignore messages from the bot itself
    content = message.content
    if content.startswith("/dhelp"):
        await message.channel.send('<@' + str(message.author.id) + '>' + HELP_MESSAGE)
        logging.info('@' + str(message.author) + HELP_MESSAGE)
    elif content.startswith("/d1"):
        await handle_d_command(message, 6, 1)
    elif content.startswith("/d2"):
        await handle_d_command(message, 6, 2)
    elif content.startswith("/d3"):
        await handle_d_command(message, 6, 3)
    elif content.startswith("/d00"):
        await handle_d_command(message, 100, 1)
    elif content.startswith("/r "):
        await handle_custom_roll_command(message)
        
# Main
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    logging.info(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    await handle_command(message)

client.run(BOT_TOKEN)