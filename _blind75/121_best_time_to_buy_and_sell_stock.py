#!/usr/bin/python3

# Time: O(n), iterates over input list once
# Space: O(1), stores a few ints

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        profit = 0
        while right < len(prices):
            # Update max profit
            if prices[right] - prices[left] > profit:
                profit = prices[right] - prices[left]
            # If new low point found, set it to next buy-in
            if prices[right] < prices[left]:
                left = right
            right += 1
        return profit
