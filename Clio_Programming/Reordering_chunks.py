# Problem Statement:
# You are given a string like this:
# "AB-CD-EF-GH-IJ"
# and a rule: for every group of 2 characters, move it to the end of the string.

# So for example:
# Input: "ABCD" → Output: "CDAB"
# Input: "ABCDEF" → Output: "EFABCD"
# Input: "123456" → Output: "345612"
# Now, implement a function that takes a string s and an integer k, and performs this k-character chunk rotation to the end.




def rotate_chunks(s, k):
    s = s.replace("-", "")  # remove hyphens if needed
    if k <= 0 or k >= len(s):
        return s
    return s[k:] + s[:k]














# Time Complexity:
# O(n), where n = length of the string      
# Space Complexity:
# O(n) for the new string
# Example usage:
s = "AB-CD-EF-GH-IJ"
k = 2
print(rotate_chunks(s, k))  # Output: "CDEFGHIJAB"