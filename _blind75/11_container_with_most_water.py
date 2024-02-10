#!/usr/bin/python3

# Time: O(n), iterate over the list a max of one time
# Space: O(1), store a few ints

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        most_water = 0
        while left < right:
            # Update water if needed
            water = (right - left) * min(height[left], height[right])
            if water > most_water:
                most_water = water
            # shift the smaller of the two walls
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return most_water
