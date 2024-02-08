#!/usr/bin/python3

# Time: O(n), iterates over length of array at most 3 times
# (counting frequency, storing frequencies assuming each number happens only once, collecting k most frequent)
# Space: O(n), stores occurences, frequency counts, results that grow linearly with n in worst case

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count occurences
        counts = {}
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)
        
        # Max frequency is length of nums
        freq = [[] for _ in range(len(nums))]
        # Store occurence frequency
        for n, count in counts.items():
            freq[count - 1].append(n)
        
        # k most frequent
        result = []
        for f in reversed(freq):
            if k == len(result):
                return result
            result += f

        return result