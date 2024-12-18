from discord.ext import commands, tasks
import discord
from dotenv import load_dotenv
import os
from dataclasses import dataclass
from utils.session import Session
from pytz import timezone

# load .env
load_dotenv()

# set discord token and channel id
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
take_break_reminder = 30

bot = commands.Bot(command_prefix = "!", intents = discord.Intents.all())

# start a session method
session = Session()

@tasks.loop(minutes = take_break_reminder, count = 2)
async def break_reminder():
    if break_reminder.current_loop == 0:
        return
    
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(f"**Take a Break! You've been studying for {take_break_reminder} minutes.")


@bot.event
async def on_ready():
    print("Hello Study! Bot is ready")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Hello Study! Bot is ready")

# command to start a study session in est Local time
@bot.command()
async def startSession(ctx):
    if session.is_active:
        await ctx.send("A session is already active!")
        return
    else:
        session.is_active = True
        session.start_time = ctx.message.created_at.timestamp()
        
        local_time = ctx.message.created_at.astimezone(timezone('US/Eastern'))
        human_readable = local_time.strftime("%I:%M %p")
        break_reminder.start()
        
        await ctx.send(f"New study session started at {human_readable}")

# command to end a study session and give the total duration of session     
@bot.command()
async def endSession(ctx):
    if not session.is_active:
        await ctx.send("There is no active session")
        return 
    else:
        session.is_active = True
        end_time = ctx.message.created_at.timestamp()
        duration = end_time - session.start_time
        hours, remainder = divmod(int(duration), 3600)
        minutes, seconds = divmod(remainder, 60)
        human_readable = f"{hours:02} hours: {minutes:02} minutes: {seconds:02} seconds"
        break_reminder.stop()
        
        await ctx.send(f"Study session ended after {human_readable}")
        await ctx.send("Well done!")
        
        
@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

    
bot.run(BOT_TOKEN)