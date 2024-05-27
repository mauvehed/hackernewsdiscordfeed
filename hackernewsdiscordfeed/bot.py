"""
This module defines the Discord bot that sends daily messages with the latest best stories from Hacker News.
"""

import discord
import asyncio
from dotenv import load_dotenv
import os
from hackernewsdiscordfeed.hackernews import fetch_hacker_news_stories

# Load environment variables from the .env file
load_dotenv()

TOKEN = os.getenv('DISCORD_BOT_TOKEN')
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))

intents = discord.Intents.default()
client = discord.Client(intents=intents)

async def send_daily_message():
    """
    Sends a daily message to the specified Discord channel with the latest best stories from Hacker News.
    """
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)
    while not client.is_closed():
        stories = await fetch_hacker_news_stories()
        message = "Today's Top Hacker News Stories:\n"
        for story in stories:
            message += f"{story['title']} (Score: {story['score']})\n{story['url']}\n\n"
        await channel.send(message)
        await asyncio.sleep(86400)

@client.event
async def on_ready():
    """
    Event handler that is called when the bot is ready.
    """
    print(f'Logged in as {client.user.name}')

client.loop.create_task(send_daily_message())
client.run(TOKEN)
