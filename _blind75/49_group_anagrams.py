#!/usr/bin/python3

# Number of strings is n
# Length of each string is m
# O(nm logm)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = {}

        for string in strs: # n
            sorted_str = tuple(sorted(string)) # m logm
            if sorted_str in results:
                results[sorted_str].append(string)
            else:
                results[sorted_str] = [string]
        return results.values()
    
# Optimal:
# O(n m)
# This solution just iterates over the characters and each strings, counting them up and using that tuple
# as the hashmap key. This effectively reduces the complexity of the sorting portion of the solution.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()
