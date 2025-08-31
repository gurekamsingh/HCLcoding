# Problem Statment:

# Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.
# There is a cycle in a linked list if at least one node in the list can be visited again by following the next pointer.
# Internally, index determines the index of the beginning of the cycle, if it exists. The tail node of the list will set it's next pointer to the index-th node. If index = -1, then the tail node points to null and no cycle exists.
# Note: index is not given to you as a parameter.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        seen = set()
        cur = head
        while cur:
            if cur in seen:
                return True
            seen.add(cur)
            cur = cur.next
        return False
    
# Time Complexity:
# O(n), where n is the number of nodes in the linked list   
# Space Complexity:
# O(n) in the worst case for the set to store visited nodes 

# Example usage:
head = ListNode(3)    
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next  # Creates a cycle here
solution = Solution()
print(solution.hasCycle(head)) 