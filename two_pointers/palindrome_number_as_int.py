#!/usr/bin/python3

# Time: O(n), iterates over each digit of x linearly
# Space: O(n), stores each digit in a list as well as a few ints
# Solving without string conversion
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negatives cannot be palindromes
        if x < 0:
            return False

        # Fetch each digit
        digits = []
        while x != 0:
            remainder = int(x % 10)
            digits.append(remainder)
            x = int(x / 10)

        # Check for palindrome
        left = 0
        right = len(digits) - 1
        while left <= right:
            if digits[left] != digits[right]:
                return False
            left += 1
            right -= 1

        return True
