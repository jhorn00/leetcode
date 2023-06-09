#!/usr/bin/python3

# Time: O(n), iterates over list once
# Space: O(1), stores one new node and a few pointers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # initialize pointers with left one before head so it is one behind
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # move right over by n
        while n > 0:
            right = right.next
            n -= 1

        # move until end of list
        while right:
            left = left.next
            right = right.next

        # delete nth
        left.next = left.next.next

        # return head (could be None from deletion above)
        return dummy.next
