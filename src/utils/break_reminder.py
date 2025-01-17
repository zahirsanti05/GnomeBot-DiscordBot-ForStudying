from discord.ext import tasks
from utils.tasks import remind_task

# method to remind the user to take a brake after a certain amount of minutes
# The user picks the break reminder time
@tasks.loop(count=2) # discord method to loop this method a certain amount of times (not counting loop 0)
async def break_reminder(ctx, bot, CHANNEL_ID, take_break_reminder):
    # Skip the first loop as this will return the time if we dont return
    
    if break_reminder.current_loop == 0:
        return
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(f"# Take a Break! You've been studying for {take_break_reminder} minute(s).")
    await remind_task(ctx)

async def update_break_time(ctx, new_break_time):
    break_reminder.change_interval(minutes=new_break_time)
    
    await ctx.send(f"New break time has been changed to {new_break_time} minute(s)")