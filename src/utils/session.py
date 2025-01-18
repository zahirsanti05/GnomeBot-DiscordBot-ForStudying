from dataclasses import dataclass

# Simple session that tracks if there is a session active and a start time
# NOTE: start_time gets called with session.start_time followed with ctx.message.created_at.timestamp()
@dataclass
class Session:
    """
    Simple session that tracks if there is a session active and a start time
    NOTE: start_time gets called with session.start_time followed with ctx.message.created_at.timestamp()
    """
    is_active: bool = False
    start_time: int = 0