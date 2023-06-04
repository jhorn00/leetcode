#!/usr/bin/python3

# Time: O(n), must iterate over entire list once
# Space: O(n), must store each pointer in a hashmap (with int for seen)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # init variables
        current = head
        seen = {current:1}
        # while not at end of list
        while current:
            # if the next node has been seen (aka there is loop)
            if seen.get(current.next, 0) == 1:
                return True
            # if the next node is new
            seen[current.next] = 1
            current = current.next
        # did not find a loop
        return False
