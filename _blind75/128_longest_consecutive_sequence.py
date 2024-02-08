#!/usr/bin/python3

# Time: O(n), iterates over length n twice
# Space: O(n), stores set of length n

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        # For each value
        for n in num_set:
            # If it is the beginning of a sequence
            if n-1 not in num_set:
                current_len = 1
                # Increase length until sequence ends
                while n + 1 in num_set:
                    current_len += 1
                    n += 1
                # Update longest
                if current_len > longest:
                    longest = current_len
        return longest
