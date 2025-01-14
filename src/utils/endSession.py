# endSession.py
async def end_session(ctx, session):
    if not session.is_active:
        await ctx.send("There is no active session")
        return
    session.is_active = False
    end_time = ctx.message.created_at.timestamp()
    duration = end_time - session.start_time
    hours, remainder = divmod(int(duration), 3600)
    minutes, seconds = divmod(remainder, 60)
    human_readable = f"{hours:02} hours: {minutes:02} minutes: {seconds:02} seconds"
    await ctx.send(f"Study session ended after {human_readable}")
    await ctx.send("Well done!")
