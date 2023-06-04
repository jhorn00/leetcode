#!/usr/bin/python3

# Time: O(n), iterates over linked-list once, then over the nodes 2 at a time.
# Effectively it loopes over the list one and a half times.
# Space: O(n), stores list of all node pointers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # init variables
        current = head
        reorg = []
        # create list for quick reorg
        while current:
            reorg.append(current)
            current = current.next
        left = 0
        right = len(reorg) - 1
        while left < right:
            reorg[right].next = reorg[left].next
            reorg[left].next = reorg[right]
            left += 1
            right -= 1
        reorg[left].next = None
