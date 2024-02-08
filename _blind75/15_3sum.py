#!/usr/bin/python3

# Time: O(n),
# Space: O(1), 

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        left = 0
        middle = left + 1
        right = len(nums) - 1
        for 