#!/usr/bin/python3
# Did not have premium to submit this, but it is rather simple.

class Solution:
    def encode(self, strs):
        # Create string where there is a number before a delimiter *before*
        # the actual string starts (avoids string containing our delimiter)
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s):
        res = []
        i = 0
        
        # Read up until delimiter to get number
        # Use that number to read num of characters after delimiter
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            
        return res
