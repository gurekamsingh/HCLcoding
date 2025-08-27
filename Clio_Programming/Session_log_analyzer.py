# Problem: read a txt file which has user session info  Where:
# user_id: string
# timestamp: string in ISO 8601 format (e.g., 2025-08-26T13:45:00Z)
# # status: either login or logout 
# Calculate the longest session and which user has that longest session

from datetime import datetime
from collections import defaultdict

def get_user_highest_session(file_path):
    user_sessions = defaultdict(list)  # user_id -> list of (timestamp, status)

    with open(file_path, "r") as f:    # Read the file line by line
        for line in f:
            line = line.strip()        # Remove leading/trailing whitespace
            if not line: continue
            user_id, timestamp_str, status = line.strip(",")    # Split by comma
            timestamp = datetime.fromisoformat(timestamp_str.replace("z", "+00:00"))
            user_sessions[user_id].append((timestamp, status))  # mapping user_id to list of (timestamp, status)

    max_user = None
    max_time = 0


    for user, logs in user_sessions.items():  # for each user, sort the logs by timestamp
        logs.sort()
        total = 0

        for i in range(0, len(logs), 2):
            if i+1 < len(logs) and logs[i][0] == "login" and logs[i+1][1] == "logout":
                session = (logs[i+1][0] - logs[i][0]).total_seconds()/60   # in minutes
                total = total + session

        if total > max_time:
            max_time = total
            max_user = user
    return max_user, int(max_time)
    
# Time Complexity:

# Reading file: O(n)

# Sorting sessions per user: O(k log k), where k is number of logs per user

# Total: O(n + u·k log k)

# Space Complexity:

# O(n) for storing all sessions
