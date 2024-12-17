from discord.ext import commands
import discord
from dotenv import load_dotenv
import os
# load .env
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

bot = commands.Bot(command_prefix = "!", intents = discord.Intents.all())

@bot.event
async def on_ready():
    print("Hello Study! Bot is ready")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Hello Study! Bot is ready")
    
@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

    
bot.run(BOT_TOKEN)