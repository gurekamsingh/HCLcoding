# Problem Statement:
# You're building a Secret Santa assignment generator.
# You’re given a list of participant names. Your task is to assign each person someone else to give a gift to — no one should be assigned to themselves, and each person must be assigned exactly once.
# Write a function that returns a dictionary representing the Secret Santa assignments.

import random
from typing import List, Dict

def secret_santa_assignment(participants: List[str]) -> Dict[str, str]:
    """
    Generate Secret Santa assignments for a list of participants.
    Args:
        participants: List of participant names
    Returns:
        Dictionary mapping each person to who they should give a gift to
    Raises:
        ValueError: If less than 2 participants provided
    """
    if len(participants) < 2:
        raise ValueError("Need at least 2 participants for Secret Santa")
    
    n = len(participants)
    
    # Create a shuffled copy for randomness
    receivers = participants.copy()
    random.shuffle(receivers)
    
    # Fix any self-assignments by shifting
    for i in range(n):
        if participants[i] == receivers[i]:
            # Swap with next position (wrapping around if needed)
            next_pos = (i + 1) % n
            receivers[i], receivers[next_pos] = receivers[next_pos], receivers[i]
    
    # Create assignment dictionary
    return {giver: receiver for giver, receiver in zip(participants, receivers)}

# Example usage
if __name__ == "__main__":
    participants = ["Alice", "Bob", "Charlie", "Diana"]
    assignment = secret_santa_assignment(participants)
    
    print("Secret Santa Assignments:")
    for giver, receiver in assignment.items():
        print(f"{giver} → {receiver}")

# Time Complexity:
# O(n) where n is the number of participants, due to the shuffle and single pass
# Space Complexity:
# O(n) for storing the assignments in a dictionary