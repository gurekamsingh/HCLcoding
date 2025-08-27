# API Rate Limiter (HashMap + Sliding Window) Problem Statement:
# Let’s say you're working on a system that receives API calls from various users. 
# You’re tasked with building a function that simulates a rate limiter.
# You’ll be given a list of API requests. Each request is a tuple:

# (user_id: str, timestamp: int)
# Where timestamp is the number of seconds since epoch.

# Write a function that:
# Allows a maximum of 3 API calls per 10 seconds per user.
# Returns a list of booleans where each value represents whether that request was allowed (True) or rejected (False).

from collections import defaultdict, deque

# deque is basically a double-ended queue which allows appending and popping from both ends in O(1) time complexity
def rate_limiter(requests):
    user_logs = defaultdict(deque)  #  used deque because it is efficient for popping in time sensitive scenarios
    result = []

    for user_id, timestamp in requests:
        q = user_logs[user_id]  # deque for each user which stores all the timestamps of their requests
        while q and timestamp - q[0] >= 10:
            q.popleft() # Remove timestamps older than 10 seconds
        if len(q) < 3:  # If less than 3 requests in the last 10 seconds, allow the request
            q.append(timestamp)
            result.append(True)
        else:
            result.append(False)
    return result


# Time Complexity:
# O(n), where n = number of requests
#  Space Complexity:
# O(u·r), where u = number of users and r = max requests per user in the window
# Example usage:
requests = [    ("user1", 10), ("user2", 3), ("user2", 40), ("user2", 5),
    ("user1", 120), ("user1", 13), ("user1", 14), ("user1", 15)]
print(rate_limiter(requests))  # Output: [True, True, True, True, True, True, True, False