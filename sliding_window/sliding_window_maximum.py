#!/usr/bin/python3

# Time: O(n), iterates over list once
# Space: O(n), stores queue of max size n along with a couple ints

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxQueue = deque() # indices so we can track position in window
        left = 0
        right = 0
        result = []
        while right < len(nums):
            # remove smaller numbers (larger nums bubbling toward the top/left of the queue)
            while maxQueue and nums[maxQueue[-1]] < nums[right]:
                maxQueue.pop()
            
            # always append the new value, it is either the new max, or smaller than the max and belongs in queue after it
            maxQueue.append(right)

            # remove max number when it falls out of the window
            if maxQueue[0] < left:
                maxQueue.popleft()
            
            # only move left and give max nums once window has reached max width k
            if (right + 1) >= k:
                result.append(nums[maxQueue[0]])
                left += 1
            
            # always shift right
            right += 1

        return result
