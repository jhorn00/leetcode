#!/usr/bin/python3

# Time: O(n), iterates over linked-list once, then over the nodes 2 at a time.
# Effectively it loopes over the list one and a half times.
# Space: O(1), stores only a few temporary pointers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        # find halfway point
        slow = head
        fast = head.next
        # since fast moves 2 and slow moves 1,
        # fast will reach the end when slow is in the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half for insertions/merge
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halves
        first = head
        second = prev
        while second:
            # store next nodes
            tmp1 = first.next
            tmp2 = second.next
            # merge lists
            first.next = second
            second.next = tmp1
            # move to next nodes
            first = tmp1
            second = tmp2
