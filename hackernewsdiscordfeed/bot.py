"""
This module defines the Discord bot that sends daily messages with the latest best stories from Hacker News.
"""

import discord
from discord.ext import commands
import asyncio
from dotenv import load_dotenv
import os
from hackernewsdiscordfeed.hackernews import fetch_hacker_news_stories

# Load environment variables from the .env file
load_dotenv()

TOKEN = os.getenv('DISCORD_BOT_TOKEN')
CHANNEL_ID_STR = os.getenv('CHANNEL_ID')

# Ensure the environment variables are properly loaded
if TOKEN is None:
    raise ValueError("DISCORD_BOT_TOKEN environment variable is not set")

if CHANNEL_ID_STR is None:
    raise ValueError("CHANNEL_ID environment variable is not set")

CHANNEL_ID = int(CHANNEL_ID_STR)

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

async def fetch_and_post_stories():
    """
    Fetches the latest best stories from Hacker News and posts them to the specified Discord channel as embeds.
    """
    channel = bot.get_channel(CHANNEL_ID)
    stories = await fetch_hacker_news_stories()
    for story in stories:
        url = story.get('url')
        if url:  # Only post stories with valid URLs
            embed = discord.Embed(
                title=story['title'],
                description=f"Score: {story['score']}",
                url=url,
                color=discord.Color.blue()
            )
            await channel.send(embed=embed)

@bot.event
async def on_ready():
    """
    Event handler that is called when the bot is ready.
    """
    print(f'Logged in as {bot.user.name}')
    bot.loop.create_task(daily_task())

async def daily_task():
    """
    A daily task that sends the best stories from Hacker News every 24 hours.
    """
    await bot.wait_until_ready()
    while not bot.is_closed():
        await fetch_and_post_stories()
        await asyncio.sleep(86400)

@bot.command(name='post_stories')
async def post_stories(ctx):
    """
    Command to manually fetch and post the latest best stories from Hacker News.
    """
    await fetch_and_post_stories()
    await ctx.send("Posted today's top Hacker News stories!")

async def main():
    """
    The main function to start the bot.
    """
    await bot.start(TOKEN)

asyncio.run(main())
