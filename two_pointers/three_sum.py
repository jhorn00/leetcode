#!/usr/bin/python3

# Time: O(n^2), since we sort and operate on list of n size, n times
# Space: O(1), only a few ints are stored no matter size n (ignoring sort complexity). With sort it should be O(n)
class Solution:
    # This assumes all inputs have a solution
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # result
        result = []
        # sort list to use two-sum algo
        nums.sort()
        for firstIndex in range(0, len(nums) - 3):
            # if we already did the number, skip since nothing will be new
            if firstIndex > 0 and nums[firstIndex - 1] == nums[firstIndex]:
                continue
            # set remaining list to search
            lesserAddend = firstIndex + 1
            greaterAddend = len(nums) - 1
            # Work through list until invalid result (index1 >= index2) occurs
            while lesserAddend < greaterAddend:
                # calc sum
                currentSum = nums[firstIndex] + nums[lesserAddend] + nums[greaterAddend]
                # adjust addends
                if currentSum > 0:
                    greaterAddend -= 1
                elif currentSum < 0:
                    lesserAddend += 1
                else:
                    # add solution and adjust two-sum search
                    result.append([nums[firstIndex], nums[lesserAddend], nums[greaterAddend]])
                    lesserAddend += 1
                    while nums[lesserAddend] == nums[lesserAddend - 1] and lesserAddend < greaterAddend:
                        lesserAddend += 1
        return result
