from discord.ext import tasks

# method to remind the user to take a brake after a certain amount of minutes
# The user picks the break reminder time
@tasks.loop(count=2) # discord method to loop this method a certain amount of times (not counting loop 0)
async def break_reminder(bot, CHANNEL_ID, take_break_reminder):
    # Skip the first loop as this will return the time if we dont return
    if break_reminder.current_loop == 0:
        return
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(f"# Take a Break! You've been studying for {take_break_reminder} minute(s).")