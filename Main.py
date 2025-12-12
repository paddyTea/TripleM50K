import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import asyncio
from datetime import datetime

from scrape import scan
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
channelID = int(os.getenv('DISCORD_CHANNEL_ID'))

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

async def time_watcher():
    START_HOUR = 9
    END_HOUR = 16
    CURRENT_TIME = datetime.now()

    while True:
        if START_HOUR <= CURRENT_TIME.hour < END_HOUR:
            await scan_and_message()
            print("Scanned for song, Sleeping for 2 minutes")
            await asyncio.sleep(120)
            
        else:
            print("Out of time range, Sleeping for 4 minutes")
            await asyncio.sleep(240)
            
    

async def scan_and_message():
    await bot.wait_until_ready()
    channel = bot.get_channel(channelID)

    song = scan()
    if song == True :
        await channel.send(f"({song}")
    else:
        print("Nothing returned")
        

@bot.event
async def on_ready():
    bot.loop.create_task(time_watcher())

bot.run(token, log_handler=handler, log_level=logging.DEBUG)

