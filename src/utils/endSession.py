
# Method to end the current session as well as stoping the break reminder
# returns the amount of time studying by using the session time and converting it to a human readable time
async def end_session(ctx, session):
    if not session.is_active:
        await ctx.send("There is no active session")
        return
    
    session.is_active = False # set session to false in case user tries to end a session twice
    
    end_time = ctx.message.created_at.timestamp() # get the end time from when the session was ended
    duration = end_time - session.start_time # get the total duration of the session by subtracting the end time with the starting time
                                             # when the session was created
                                             
    # get the hours and remainder for minutes then calculate minutes and seconds. Then format in hours, minutes, and seconds
    hours, remainder = divmod(int(duration), 3600)
    minutes, seconds = divmod(remainder, 60)
    human_readable = f"{hours:02} hours: {minutes:02} minutes: {seconds:02} seconds"
    
    # tell the user the session has ended and send the duration of the session
    await ctx.send(f"Study session ended after {human_readable}")
    await ctx.send("Well done!")
