#!/usr/bin/python3

# Time: O(n), iterates over input string at most twice
# Space: O(n), store the whole string at most

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        longest = 0
        seen = set()
        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            if s[right] not in seen:
                seen.add(s[right])
                longest = max(longest, len(seen))
            right += 1
        return longest
