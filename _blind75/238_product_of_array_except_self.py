#!/usr/bin/python3

# Time: O(n), iterates over list (almost) twice
# Space: O(1), excluding the output array

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        # multiply for 1 to end of list (products left of element)
        for i in range(1, len(nums)):
            result[i] = nums[i - 1] * result[i - 1]
        
        # multiply elements of list in reverse order (products right of element)
        post = 1
        for i in reversed(range(len(nums))):
            result[i] = result[i] * post
            post *= nums[i]
        
        return result