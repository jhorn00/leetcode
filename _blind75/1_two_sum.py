#!/usr/bin/python3

# Time: O(n), iterates over whole array max of two times
# Space: O(n), stores dict with at most n pairs (lists have max length of 2 because of problem constraints)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Build dict of numbers to their indices
        elements = {}
        for i in range(len(nums)):
            if nums[i] in elements:
                elements[nums[i]].append(i)
            else:
                elements[nums[i]] = [i]
        
        # For each number in the dict, see if it adds up to the target with any other number
        for key, value in elements.items():
            addend = target - key
            if addend in elements:
                # If there are two of the same number (we might reuse the same thing otherwise)
                if len(elements[addend]) == 2:
                    return value
                # If numbers are unique
                if key != addend:
                    return [value[0], elements[addend][0]]

        return [-1, -1]

# Time: O(n), iterates over whole array once
# Space: O(n), stores dict with at most n-1 pairs
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
