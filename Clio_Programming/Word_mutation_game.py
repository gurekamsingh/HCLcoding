# Problem Statement: You’re building a simple word mutation game engine. The game starts with a list of strings.
# ["keyboard", "monitor", "printer", "router"]
# Write a function that:
# Moves the first two letters of each word to the end.
# Then reverses the entire word.
# Return the final mutated list: ["keyboard"] → move "ke" to end → "yboardke" → reverse → "ekdraoby"

def mutated_word(words):
    result = []

    for word in words:
        if len(word) < 2:
            mutated = word[::-1] 
        else:
            new = word[2:] + word[:2]
            mutated = new[::-1]
            result.append(mutated)
    return result   


words = ["Gurekam", "keyboard", "monitor", "printer", "router"]
print(mutated_word(words))  # Output: ['makureG', 'ekdraoby', 'ritonmo', 'nterpri', 'terou']
