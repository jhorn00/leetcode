#!/usr/bin/python3

# Time: O(n), loop over array once
# Space: O(1), store only two integers

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        maxDiff = 0
        # move through array once
        for i in prices:
            # if new buy point found, store
            if i < minimum:
                minimum = i
            # if new sell point found, store profit
            else:
                maxDiff = max(maxDiff, i - minimum)
        return maxDiff
