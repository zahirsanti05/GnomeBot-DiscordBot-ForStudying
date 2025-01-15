from discord.ext import tasks

# method to remind the user to take a brake after a certain amount of minutes
# want to chenge: let the user decide the break (maybe pass it though starting a seesion)
take_break_reminder = 30
@tasks.loop(minutes=take_break_reminder, count=2) # discord method to loop this method a certain amount of times (not counting loop 0)
async def break_reminder(bot, CHANNEL_ID):
    if break_reminder.current_loop == 0:
        return
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(f"# Take a Break! You've been studying for {take_break_reminder} minutes.")