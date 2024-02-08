#!/usr/bin/python3

# Time: O(n), iterates over length of string once
# Space: O(1), stores only indices

class Solution:
    def isAlphanumeric(self, c):
        return (ord('0') <= ord(c) <= ord('9') or
                ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z'))
    
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not self.isAlphanumeric(s[left]):
                left += 1
            while left < right and not self.isAlphanumeric(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
