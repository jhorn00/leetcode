#!/usr/bin/python3

# Time: O(n), must loop over the string once
# Space: O(n), could store at most n characters in stack

# this can also be done with a map very easily

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            removed = c
            match c:
                case '(':
                    stack.append(')')
                case '{':
                    stack.append('}')
                case '[':
                    stack.append(']')
                case ')':
                    if len(stack) == 0:
                        return False
                    removed = stack.pop()
                case '}':
                    if len(stack) == 0:
                        return False
                    removed = stack.pop()
                case ']':
                    if len(stack) == 0:
                        return False
                    removed = stack.pop()
            if removed != c:
                return False
        if len(stack) > 0:
            return False
        return True
