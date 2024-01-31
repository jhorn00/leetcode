#!/usr/bin/python3

# Time: O(n), iterate over the string once (half, but still linear)
# Space: O(n), store string of length n and a few ints
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # The easiest way to solve this is to convert to string
        x_string = str(x)

        length = len(x_string)
        left = 0
        right = length - 1

        # Start at both ends and compare each element
        while left <= right:
            if x_string[left] != x_string[right]:
                return False
            left += 1
            right -= 1
        return True
