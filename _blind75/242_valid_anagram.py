#!/usr/bin/python3

# Time: O(n logn), sorting algorithm is n logn
# Space: O(1), excluding the input, nothing significant is stored

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s = sorted(s)
        t = sorted(t)

        for i in range(len(s)):
            if s[i] != t[i]:
                return False

        return True

# Time: O(n), iterates over length n twice
# Space: O(n), stores two pairs for each unique character in input strings -> this is up to length n

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict = {}
        t_dict = {}

        for i in range(len(s)):
            if s[i] in s_dict:
                s_dict[s[i]] += 1
            else:
                s_dict[s[i]] = 1
            if t[i] in t_dict:
                t_dict[t[i]] += 1
            else:
                t_dict[t[i]] = 1

        if s_dict != t_dict:
            return False
        return True
