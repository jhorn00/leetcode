#!/usr/bin/python3

# Time: O(n), iterates over list once
# Space: O(n), recursive calls will store each element

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
        
        # current so it is less confusing
        current = head

        # initialize new head to current in case this is end
        newHead = current
        # if not at the end of the list
        if current.next:
            # set new head to result of function (passes the real head along)
            newHead = self.reverseList(current.next)
            # set neighbor next to current (reverse link)
            current.next.next = current
        # current next is none so the end points to nothing
        # if not end, this will be set by neighbor above
        current.next = None

        return newHead
