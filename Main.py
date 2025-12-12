import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import asyncio

from scrape import scan
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
channelID = int(os.getenv('DISCORD_CHANNEL_ID'))

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

async def send_message():
    await bot.wait_until_ready()
    await asyncio.sleep(5)

    channel = bot.get_channel(channelID)

    song = scan()
    if channel:
        if song == True :
            await channel.send(f"({song}")
        else:
            print("Nothing returned")
        


@bot.event
async def on_ready():
    print(f"Hello world, {bot.user.name}")
    bot.loop.create_task(send_message())


bot.run(token, log_handler=handler, log_level=logging.DEBUG)

