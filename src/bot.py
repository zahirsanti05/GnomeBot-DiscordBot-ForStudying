from discord.ext import commands
import discord
from dotenv import load_dotenv
import os
from utils.session import Session
from utils.startSession import start_session
from utils.endSession import end_session
from utils.break_reminder import break_reminder
from utils.tasks import add_Task
from utils.tasks import complete_Task
from utils.tasks import delete_task
from utils.tasks import view_tasks
from utils.tasks import clear_tasks

# Load .env
load_dotenv()

# Set discord token and channel id
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))


bot = commands.Bot(command_prefix = "!", intents = discord.Intents.all())

# Start a session method
session = Session()

# on_ready refers to when the bot is on and ready to operate
# The bot sends a message to the user promting that it is ready for use in both the terminal and discord channel
@bot.event
async def on_ready():
    print("Hello Study! Bot is ready")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Hello Study Buddy! Bot is ready to study!")

# Cimple command to say hello to the bot
@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

# Command to start a study session in est Local time
@bot.command()
async def startSession(ctx):
    await start_session(ctx, session)
    break_reminder.start(bot, CHANNEL_ID)
    
# Command to end a study session and return amount spent studying
@bot.command()
async def endSession(ctx):
    await end_session(ctx, session)
    break_reminder.stop()

# Command to add a task to a an array and return the array in order given
@bot.command()
async def addTask(ctx, *, task: str):
    await add_Task(ctx, task)

# Command to view tasks, if empty promt the user
@bot.command()
async def viewTasks(ctx):
    await view_tasks(ctx)

# Command to add a task to a completed dictionary that hold both the completed task and
# The amount of time it took to finish from when a session was started
# BUG: if task was completed before starting a session, it returns the max session amount
@bot.command()
async def completeTask(ctx, *, task: str):
    await complete_Task(ctx, task, session)

# Command that deletes a task from the array of tasks and returns the remaining tasks.
@bot.command()
async def deleteTask(ctx, *, task: str):
    await delete_task(ctx, task)

# Command that clears all tasks in the array tasks
@bot.command()
async def clearTasks(ctx):
    await clear_tasks(ctx)
    
bot.run(BOT_TOKEN)