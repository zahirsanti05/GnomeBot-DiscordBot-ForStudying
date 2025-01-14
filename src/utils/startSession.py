from pytz import timezone

async def start_session(ctx, session):
    if session.is_active:
        await ctx.send("A session is already active!")
        return
    session.is_active = True
    session.start_time = ctx.message.created_at.timestamp()

    local_time = ctx.message.created_at.astimezone(timezone('US/Eastern'))
    human_readable = local_time.strftime("%I:%M %p")
    await ctx.send(f"New study session started at {human_readable}")