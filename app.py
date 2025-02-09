
from datetime import datetime

# Track the start time of the app
start_time = datetime.now()

def get_uptime():
    # Calculate the time difference between now and start time
    uptime = datetime.now() - start_time
    uptime_str = str(uptime).split(".")[0]  # Format as hh:mm:ss
    return f"⏳ **Project Uptime**: {uptime_str}"
