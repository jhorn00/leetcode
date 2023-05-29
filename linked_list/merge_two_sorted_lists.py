#!/usr/bin/python3

# Time: O(n), iterate over at most total number of nodes from both lists, n
# Space: O(1), store only one node and 3 pointers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # handle empty cases
        if not list1:
            return list2
        if not list2:
            return list1
        # initialize pointers
        firstCurr = list1
        secondCurr = list2
        # result list
        result = ListNode()
        tail = result
        # append nodes to result list in order
        while firstCurr and secondCurr:
            if firstCurr.val < secondCurr.val:
                tail.next = firstCurr
                firstCurr = firstCurr.next
            else:
                tail.next = secondCurr
                secondCurr = secondCurr.next
            tail = tail.next
        # when one list runs out, add remaining nodes to result
        if firstCurr:
            tail.next = firstCurr
        else:
            tail.next = secondCurr
        # return first real node as head
        return result.next
