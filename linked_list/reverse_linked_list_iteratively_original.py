#!/usr/bin/python3

# Time: O(n), iterates over list once
# Space: O(n), creates new list in reverse

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
        newHead = current
        previous = None
        while current is not None:
            # create new node with relevant values
            newNode = ListNode()
            newNode.val = current.val
            newNode.next = previous
            # update previous and new head
            previous = newNode
            newHead = newNode
            # move to next node
            current = current.next
        return newHead
