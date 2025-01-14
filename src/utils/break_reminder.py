from discord.ext import tasks

# Create the task loop
take_break_reminder = 10
@tasks.loop(minutes=take_break_reminder, count=2)
async def break_reminder(bot, CHANNEL_ID):
    if break_reminder.current_loop == 0:
        return
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(f"# Take a Break! You've been studying for {take_break_reminder} minutes.")