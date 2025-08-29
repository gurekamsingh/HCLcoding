# Problem Statement:

# You're working on a utility script that sanitizes URL paths. 
# A path string may contain redundant slashes (//), . (current directory), and .. (parent directory). 
# Your task is to write a function normalize_path(path: str) -> str that returns the simplified canonical version of the path.
# Examples:

# Input: "/a/./b/../../c/" → Output: "/c"

def normalize_path(path: str) -> str:
    parts = path.split('/')
    stack = []
    for part in parts:
        if part == '' or part == '.':
            continue
        elif part == '..':
            if stack:
                stack.pop()
        else:
            stack.append(part)
    return '/' + '/'.join(stack)


# Time Complexity:
# O(n), where n = length of the path string 
# Space Complexity:
# O(n) for the stack in the worst case

# Example usage:
path = "/a/./b/../../c/"
print(normalize_path(path))  # Output: "/c"