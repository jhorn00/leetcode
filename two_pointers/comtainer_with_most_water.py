#!/usr/bin/python3

# Time: O(n), will iterate over the array once
# Space: O(1), will store only the current maxArea, two indices, and a temporary area
# for each set of heights
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # init indices and maxArea
        left = 0
        right = len(height) - 1
        maxArea = 0
        # while valid container
        while left < right:
            # calculate current area
            area = (right - left) * min(height[left], height[right])
            # if new max, record it
            if area > maxArea:
                maxArea = area
            # shift right and left based on height to maximize area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea
