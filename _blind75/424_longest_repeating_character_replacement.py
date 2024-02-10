#!/usr/bin/python3

# Time: O(n), iterates over whole string at most twice
# Space: O(1), stores a few ints and a map with at most 26 pairs

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        longest = 0
        max_count = 0
        counts = {}
        while right < len(s):
            # Handle right side of window
            if s[right] not in counts:
                counts[s[right]] = 1
            else:
                counts[s[right]] += 1
            # Update character with most occurances
            max_count = max(max_count, counts[s[right]])
            # If we need too many replacements, shift left side
            while right - left + 1 - max_count > k:
                counts[s[left]] -= 1
                left += 1
            # Handle new longest
            if right - left + 1 > longest:
                longest = right - left + 1
            right += 1
        return longest