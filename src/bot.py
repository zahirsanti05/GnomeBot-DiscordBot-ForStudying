from discord.ext import commands
import discord
from dotenv import load_dotenv
import os
from utils.session import Session
from utils.startSession import start_session
from utils.endSession import end_session
from utils.break_reminder import break_reminder

# load .env
load_dotenv()

# set discord token and channel id
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))


bot = commands.Bot(command_prefix = "!", intents = discord.Intents.all())

# start a session method
session = Session()

@bot.event
async def on_ready():
    print("Hello Study! Bot is ready")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Hello Study Buddy! Bot is ready to study!")
    
@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

# command to start a study session in est Local time
@bot.command()
async def startSession(ctx):
    await start_session(ctx, session)
    break_reminder.start(bot, CHANNEL_ID)
    
# command to end a study session and return amount spent studying
@bot.command()
async def endSession(ctx):
    await end_session(ctx, session)
    break_reminder.stop()

    
bot.run(BOT_TOKEN)