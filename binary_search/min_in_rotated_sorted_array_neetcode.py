#!/usr/bin/python3

# Time: O(logn), uses a binary search pattern to search the list
# Space: O(1), stores a few integers

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        lowest = nums[left]
        while left <= right:
            # if current range is sorted, left is lowest
            if nums[left] < nums[right]:
                lowest = min(lowest, nums[left])
            # find middle, check if new low
            middle = int((left + right) / 2)
            lowest = min(lowest, nums[middle])
            # if middle is larger than the left, we want to check right since pivot is to the right
            if nums[middle] >= nums[left]:
                left = middle + 1
            # if middle is smaller than left, want to check left since pivot is between them
            else:
                right = middle - 1
        return lowest
