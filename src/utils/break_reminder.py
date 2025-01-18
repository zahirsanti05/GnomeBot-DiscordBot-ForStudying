from discord.ext import tasks
from utils.tasks import remind_task

@tasks.loop(count=2) # discord method to loop this method a certain amount of times (not counting loop 0).
async def break_reminder(ctx, bot, CHANNEL_ID, take_break_reminder):
    """
    Method to remind the user to take a break after a certain amount of minutes.
    The user picks the break reminder time. Default to 30 if no user input.

    Args:
        ctx (_type_): discord API context.
        bot (BOT): Discord Bot class that detects prefix for commands and channel ID's among other features.
        CHANNEL_ID (int): channel in which the bot will respond to the user.
        take_break_reminder (int): Number of minutes in which the bot will remind the user to take a break
    
    Returns:
        str: Inform the user of the time that was set for a break reminder
    """
    # Skip the first loop as this will return the a break reminder immediately.
    if break_reminder.current_loop == 0:
        return
    # Get the channel ID and remind the user to take a break.
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(f"# Take a Break! You've been studying for {take_break_reminder} minute(s).")
    # Call remind_task to display all current uncompleted tasks.
    await remind_task(ctx)

async def update_break_time(ctx, new_break_time):
    """
    Method to update the amount of minutes to remind the user to take a break.
    Promt the user that the time has been changed
    
    Args:
        ctx (_type_): discord API context.
        new_break_time (int): Number of minutes in which the bot will remind the user to take a break
        
    Returns:
        str: Infoms the user of the new time that was set for a break reminder
    """
    break_reminder.change_interval(minutes=new_break_time)
    
    await ctx.send(f"New break time has been changed to {new_break_time} minute(s)")