#!/usr/bin/python3

# Time: O(n), iterates over list once
# Space: O(1), stores 3 pointers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # init pointers
        first = head
        second = head
        secondPrev = head
        # move first pointer out lenth n
        for i in range(n - 1):
            first = first.next
        # while the first is still valid
        while first:
            # if first is at the last node, remove second node
            if not first.next:
                # nth is head
                if second == head:
                    return second.next
                # nth is not head
                secondPrev.next = second.next
                return head
            # shift pointers
            first = first.next
            secondPrev = second
            second = second.next
        # return new list
        return head
