# Problem Statement:

# You’re given a log file with lines like:
# user1 clicked
# user2 clicked
# user1 clicked

# Write code to read the file and return the top user by number of clicks.
# If there’s a tie, return all such users in a list.

from collections import defaultdict

def top_user(logfile):
    user_clicks = defaultdict(int)   # using defaultdict to store user clicks


    with open (logfile, "r") as f:
        for line in f:
            line  = line.strip()
            if not line: continue
            parts = line.split()
            if len(parts) == 2 and parts[1] == 'clicked':
                user_clicks[parts[0]] += 1  # Increment click count for the user

    if not user_clicks:
        return []
    
    max_clicks = max(user_clicks.values())

    for user, clicks in user_clicks.items():
        if clicks == max_clicks:
            return user


# Time Complexity:
# O(n), where n = number of lines in the file
# Space Complexity:
# O(u), where u = number of unique users

# Example usage:
logfile = r"C:\Users\Gurekam\Desktop\University of Windsor\HCLcoding\Clio_Programming\Userclicks.txt"
print(top_user(logfile))  # Output: user1