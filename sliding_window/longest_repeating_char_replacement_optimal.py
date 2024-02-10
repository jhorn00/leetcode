#!/usr/bin/python3

# Time: O(n), iterates over list at most twice
# Space: O(1), stores 4 ints, a char, and has a map with at most 26 pairs

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        longest = 1
        counts = dict()
        maxCount = 0
        # for each character
        while right < len(s):
            # update counts (0 param returns 0 if not there)
            c = s[right] # need this to access dict
            counts[c] = counts.get(c, 0) + 1
            # if this character is the most frequent character, update count
            maxCount = max(maxCount, counts[c])
            # if the window requires more replacements than available, shrink it as necessary
            while (right - left + 1) - maxCount > k:
                c = s[left] # need this to access dict
                counts[c] -= 1
                left += 1
            # set max length
            longest = max(longest, right - left + 1)
            # iterate
            right += 1
        return longest