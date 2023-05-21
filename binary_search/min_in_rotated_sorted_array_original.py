#!/usr/bin/python3

# Time: O(logn), uses a binary search pattern to search the list
# Space: O(1), stores a few integers

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        lowest = nums[left]
        while left <= right:
            middle = int((left + right) / 2)
            if nums[middle] < lowest:
                lowest = nums[middle]
            if nums[middle] > nums[right]:
                left = middle + 1
            elif nums[middle] < nums[left]:
                right = middle - 1
            elif lowest < nums[left]:
                return lowest
            else:
                return nums[left]
        return lowest
