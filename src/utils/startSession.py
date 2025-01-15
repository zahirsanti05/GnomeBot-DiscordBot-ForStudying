from pytz import timezone

# Method that starts a study session only if there isn't a session already active
# Uses the session method in session to set the start time for later use
async def start_session(ctx, session):
    if session.is_active:
        await ctx.send("A session is already active!")
        return
    
    session.is_active = True # Sets the state of the session as active (true)
    session.start_time = ctx.message.created_at.timestamp() # Sets the start time with when the session was created

    local_time = ctx.message.created_at.astimezone(timezone('US/Eastern'))
    human_readable = local_time.strftime("%I:%M %p")
    await ctx.send(f"New study session started at {human_readable}") # return the time in est