# Problem Statement:
# You’re working on a file indexing service. You’re given a nested folder structure represented as a dictionary.

# Each key is a folder name, and its value is either:
# A list of files (leaf node), or
# Another dictionary (representing subfolders)
# Write a function that returns the maximum depth of the folder structure.


def max_depth_folder(structure, current_depth = 1):
    if not isinstance(structure, dict):
        return current_depth
    
    max_depth = current_depth
    
    for key in structure:  # iterate through each key(folder name) in the dictionary
        child = structure[key]  # get the value of the key which might be a list of files or another dictionary
        if isinstance(child, dict):
            max_depth = max(max_depth, max_depth_folder(child, current_depth + 1))
    return max_depth



# Time Complexity:
# O(n), where n = total number of folders and files
# Space Complexity:
# O(h), where h = height of the folder structure (due to recursion stack)















# Example usage:
folder_structure = {
    "root": {   
        "folder1": {
            "subfolder1": ["file1.txt", "file2.txt"],
            "subfolder2": {
                "subsubfolder1": ["file3.txt"]
            }
        },
        "folder2": ["file4.txt"],
        "folder3": {
            "subfolder3": {
                "subsubfolder2": {
                    "subsubsubfolder1": ["file5.txt"]
                }
            }
        }
    }}
print(max_depth_folder(folder_structure))  # Output: 5