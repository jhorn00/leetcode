#!/usr/bin/python3

# Time: O(26*n), iterates over list once (iterates over list of max size 26 at most ~n-26=n times)
# Space: O(1), stores 3 ints, a char, and has a map with at most 26 pairs

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        longest = 1
        counts = dict()
        # for each character
        while right < len(s):
            # update counts (0 param returns 0 if not there)
            c = s[right] # need this to access the dict
            counts[c] = counts.get(c, 0) + 1
            # if the window requires more replacements than available, shrink it as necessary
            while (right - left + 1) - max(counts.values()) > k:
                c = s[left]
                counts[c] -= 1
                left += 1
            # set max length
            longest = max(longest, right - left + 1)
            # iterate
            right += 1
        return longest