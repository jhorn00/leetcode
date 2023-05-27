#!/usr/bin/python3

# Time: O(n), iterates over list once
# Space: O(1), stores only a few pointers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if empty list
        if not head:
            return head
        # iterate over input list and produce reverse
        current = head
        previous = None
        while current is not None:
            # store previous
            old = previous
            # move the pointers before reversing next
            previous = current
            current = current.next
            # reverse next
            previous.next = old
        return previous
