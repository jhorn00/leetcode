#!/usr/bin/python3

# Time: O(n + m), loop over string s once and string t once
# Space: O(1), store a couple maps of max size 26 and a few ints and floats

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        # create maps
        targets, window = {}, {}
        for c in t:
            targets[c] = targets.get(c, 0) + 1

        # init helper vars
        have = 0
        need = len(targets)
        indices = [-1, -1]
        indicesLen = float("infinity")
        left = 0

        # slide the window and look for target characters
        for right in range(len(s)):
            # current char
            c = s[right]
            # update current window
            window[c] = 1 + window.get(c, 0)

            # check if we have a target character
            # if there is a target character and we have the right amount of it, increase have count
            if c in targets and window[c] == targets[c]:
                have += 1

            # if we have what we need, narrow the window from the left to look for the best result
            while have == need:
                # update result indices if it is a new smallest window
                if (right - left + 1) < indicesLen:
                    indices = [left, right]
                    indicesLen = right - left + 1
                # remove left character from window
                window[s[left]] -= 1
                # if we removed a target character and no longer have what we need, update have
                if s[left] in targets and window[s[left]] < targets[s[left]]:
                    have -= 1
                left += 1
        left, right = indices
        if indicesLen != float("infinity"):
            return s[left:right + 1]
        else:
            return ""
