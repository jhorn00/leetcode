#!/usr/bin/python3

# Time: O(n), iterates over lists once
# Space: O(n), creates new list linear to length n and a constant number of pointers and values

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Input iterators/vars
        curr1 = l1
        curr2 = l2
        val1 = curr1.val
        val2 = curr2.val
        carry = 0
        # Result nodes
        current = ListNode()
        head = current
        # While one list still has digits
        while curr1 != None or curr2 != None:
            # Values and pointers
            if curr1 != None:
                val1 = curr1.val
                curr1 = curr1.next
            else:
                val1 = 0
            if curr2 != None:
                val2 = curr2.val
                curr2 = curr2.next
            else:
                val2 = 0

            # Add the elements
            sum = val1 + val2 + carry
            # If sum requires carried 1
            if sum >= 10:
                remainder = int(sum % 10)
                newNode = ListNode(remainder)
                current.next = newNode
                current = newNode
                carry = 1
            else:
                newNode = ListNode(sum)
                current.next = newNode
                current = newNode
                carry = 0

        # Handle trailing carry
        if carry == 1:
            newNode = ListNode(1)
            current.next = newNode
        
        return head.next
