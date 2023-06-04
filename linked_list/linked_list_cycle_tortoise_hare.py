#!/usr/bin/python3

# Time: O(n), must iterate over max of roughly n nodes
# Space: O(1), only stores two pointers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # init variables
        slowPointer = head
        fastPointer = head
        # while not at end of list
        while fastPointer and fastPointer.next:
            # move fast by two
            fastPointer = fastPointer.next.next
            # move slow by one
            slowPointer = slowPointer.next
            # if the pointers are at the same node, meaning fast caught up (there is loop)
            if slowPointer is fastPointer:
                return True
        # list was empty or fast reached end
        return False
