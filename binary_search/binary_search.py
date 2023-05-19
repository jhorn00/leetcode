#!/usr/bin/python3

# Time: O(logn), only iterates over portion of the list, halving indices to cover each time (this will run log_2(n) times)
# Space: O(1), only stores a few integers

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            # python will not experience an overflow
            # to avoid overflow in other languages, do this: l + ((r - l) / 2)
            # take half the distance between right and left, then add it to left
            middle = int((left + right) / 2)
            if target > nums[middle]:
                left = middle + 1
            elif target < nums[middle]:
                right = middle - 1
            else:
                return middle
        return -1
