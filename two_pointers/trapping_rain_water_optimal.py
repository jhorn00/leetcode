#!/usr/bin/python3

# Time: O(n), loops over list once performing constant operations
# Space: O(1), stores a few ints at a time

class Solution:
    def trap(self, height: List[int]) -> int:
        # init iterators, max, and result
        left = 0
        right = len(height) - 1
        maxLeft = height[left]
        maxRight = height[right]
        totalWater = 0
        # while we have not covered all locations water could pool
        while left < right:
            # each max represents our "walls", so act on the lowest wall
            if maxLeft < maxRight:
                # adding first skips the edge, wastes one loop on the max
                left += 1
                # set new max (could be same)
                maxLeft = max(height[left], maxLeft)
                # add water at location (could be 0)
                totalWater += maxLeft - height[left]
            else:
                # subtracting first skips the edge, wastes one loop on the max
                right -= 1
                # set new max (could be same)
                maxRight = max(height[right], maxRight)
                # add water at location (could be 0)
                totalWater += maxRight - height[right]
        # return
        return totalWater
