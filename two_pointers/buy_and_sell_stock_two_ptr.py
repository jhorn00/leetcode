#!/usr/bin/python3

# Time: O(n), loop over array once
# Space: O(1), store only a few integers

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 0
        maxDiff = 0
        while right < len(prices):
            # if right side is lower buy point, shift left
            if prices[right] < prices[left]:
                left = right
            # if left side is lower and new max is found, adjust max
            elif prices[right] - prices[left] > maxDiff:
                maxDiff = prices[right] - prices[left]
            # always move right
            right += 1
        return maxDiff
