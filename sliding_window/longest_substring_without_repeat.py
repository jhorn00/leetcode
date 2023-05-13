#!/usr/bin/python3

# Time: O(n), iterates over list once
# Space: O(n), stores a set of characters up to n length

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        longestLen = 0
        usedChars = set()
        # while window still valid
        while right < len(s):
            # if right character has been used, shift left edge until window no longer contains it
            while s[right] in usedChars:
                usedChars.discard(s[left])
                left += 1
            # if the right character is new, add to set
            if s[right] not in usedChars:
                usedChars.add(s[right])
                # update length
                longestLen = max(longestLen, len(usedChars))
            right += 1
        return longestLen
