# Problem statement:
# Given an array nums containing n integers in the range [0, n] without any duplicates, return the single number in the range that is missing from nums.
# Follow-up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
# Example 1: Input: nums = [1,2,3]
# Output: 0

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        num_set = set(nums)
        n = len(nums)
        for i in range(n + 1):
            if i not in num_set:
                return i

# Time Complexity:
# O(n), where n is the length of the input array nums
# Space Complexity:
# O(n) for the set to store the numbers in nums
# Example usage:
nums = [0, 1, 4, 3]
solution = Solution()
print(solution.missingNumber(nums))  