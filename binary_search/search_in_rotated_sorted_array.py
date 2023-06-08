#!/usr/bin/python3

# Time: O(logn), still demonstrates binary search behavior where half the list is continually cut away.
# Space: O(1), requires only a few integers to be stored.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        # inclusive to account for len 1
        while left <= right:
            # set middle and check if target is found
            middle = (left + right) // 2
            if target == nums[middle]:
                return middle

            # left sorted region
            if nums[middle] >= nums[left]:
                # move right
                #if the target is greater than the middle or smaller than the left
                if target > nums[middle] or target < nums[left]:
                    left = middle + 1
                # move left
                # if the target is less than the middle and greater than the left
                else:
                    right = middle - 1

            # if not in left region, must be in right region
            else:
                # move left
                # if the target is smaller than middle or larger than the right
                if target < nums[middle] or target > nums[right]:
                    right = middle - 1
                # move right
                # if the target is larger than the middle and less than the right
                else:
                    left = middle + 1
        # not found
        return -1
