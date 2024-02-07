#!/usr/bin/python3

# Time: O(n), iterates over whole array
# Space: O(n), stores ints that have been seen before -> this is all in the worst case

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen_set = set()
        for n in nums:
            if n in seen_set:
                return True
            seen_set.add(n)
        return False
