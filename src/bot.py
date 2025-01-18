import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from utils.session import Session
from utils.startSession import start_session
from utils.endSession import end_session
from utils.break_reminder import break_reminder, update_break_time
from utils.tasks import add_Task, complete_Task, delete_task, view_tasks, clear_tasks, view_completed_tasks

# Load .env
load_dotenv()

# Set discord token and channel id
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))


bot = commands.Bot(command_prefix = "!", intents = discord.Intents.all())

# Start a session method
# session sets if a session is active (bool) and when this session started (int)
# :is_active: bool [false]
# :start_time: int [0]
session = Session()


@bot.event
async def on_ready():
    """
    'on_ready' refers to when the bot is on and ready to operate.
    The bot sends a message to the user promting that it is ready for 
    use in both the terminal and discord channel.
    """
    print("Hello Study! Bot is ready")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Hello Study Buddy! Bot is ready to study!")

@bot.command()
async def hello(ctx):
    """
    Command to say hello to the bot.
    
    Args:
        ctx (_type_): discord API context
    """
    await ctx.send("Hello!")
    
@bot.command()
async def helpCommands(ctx):
    """
    Command that returns all commands study bot currently supports.
    
    Args:
        ctx (_type_): discord API context
        :rtype: str
    """
    helpPrint = "Here is the list of commands:\n"
    cnd_Help = ["!startSession", 
                "!endSession", 
                "!updateBreak", 
                "!addTask", 
                "!viewTasks", 
                "!deleteTask", 
                "!completeTask", 
                "!viewCompletedTasks", 
                "!clearTasks"]
    
    # itterate through cnd_Help and add the command to the string: helpPrint
    for command in cnd_Help:
        helpPrint += f"{command}\n"
    
    await ctx.send(helpPrint)
                    
@bot.command()
async def startSession(ctx, break_time: int = 30):
    """
    Command to start a study session in est Local time.
    Additionally, the user decided the break reminder time interval  .
     
    Args:
        ctx (_type_): discord API context
        break_time (int, optional): Sets the number of minutes until study bot reminds the user to take a break. Defaults to 30 if no input from user.
    """
    # start a new study session by using the session
    await start_session(ctx, session)
    await ctx.send(f"Break reminder set for every {break_time} minute(s).")
    
    # Discord API method to change the interval in @tasks.loop()
    break_reminder.change_interval(minutes=break_time)
    # start a new loop in break reminder with the given break time
    break_reminder.start(ctx, bot, CHANNEL_ID, break_time)

@bot.command()
async def updateBreak(ctx, newBreakTime: int = 30):
    """
    Command to update the break timer that was mentioned in 'startSession' by stoping the current timer and starting another.
    Call update_break_time from tasks.py.
    
    Args:
        ctx (_type_): discord API context
        newBreakTime (int, optional): New break timer in minutes provided by the user. Defaults to 30 if no input from user.
    """
    # Stop the current break reminder loop
    break_reminder.cancel()
    
    # change reminder interval and infrom the user
    await update_break_time(ctx, newBreakTime)
    
    # start a new loop with the new break timer
    break_reminder.start(ctx, bot, CHANNEL_ID, newBreakTime)

@bot.command()
async def endSession(ctx):
    """
    Command to end a study session and return amount spent studying.
    
    Args:
        ctx (_type_): discord API context
    """
    # Checks if there is not a session active and calculates the duration of the session
    await end_session(ctx, session)
    # Stop the current break reminder loop
    break_reminder.cancel()

@bot.command()
async def addTask(ctx, *, task: str):
    """
    Command to add a task to a an array and return the array in order given.
    
    Args:
        ctx (_type_): discord API context.
        task (str): A string of a task the user wants to add to a list of tasks
    """
    # adds the task to an array 'tasks'
    await add_Task(ctx, task)

@bot.command()
async def viewTasks(ctx):
    """
    Command to view tasks, if empty promt the user.
    
    Args:
        ctx (_type_): discord API context
    """
    # Returns the array 'tasks' as a string
    await view_tasks(ctx)

# Command to add a task to a completed dictionary that hold both the completed task and
# The amount of time it took to finish from when a session was started
@bot.command()
async def completeTask(ctx, *, task: str):
    """
    Command to add a task to a completed dictionary that holds both the completed task and
    The amount of time it took to finish from when a session was started.
    If empty, promt the user
    
    Args:
        ctx (_type_): discord API context
        task (str): A string of a task the user wants to add to a list of completed tasks
    """
    # Adds the task to a dictionary where the key is the task and the completion time is the value
    await complete_Task(ctx, task, session)

@bot.command()
async def viewCompletedTasks(ctx):
    """
    Command to view completed tasks, if empty promt the user.
    
    Args:
        ctx (_type_): discord API context
    """
    # Returns the dictionary 'completedTasks' as a string
    await view_completed_tasks(ctx)

@bot.command()
async def deleteTask(ctx, *, task: str):
    """
    Command that deletes a task from the array 'tasks' and returns the remaining tasks.
    If empty, promt the user

    Args:
        ctx (_type_): discord API context
        task (str): A string of a task the user wants to delete from their list of tasks
    """
    await delete_task(ctx, task)

@bot.command()
async def clearTasks(ctx):
    """
    Command that clears all tasks from the array 'tasks'.
    If tasks is empty, promt the user

    Args:
        ctx (_type_): discord API context
    """
    # tasks.clear()
    await clear_tasks(ctx)
    
bot.run(BOT_TOKEN)