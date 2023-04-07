#!/usr/bin/python3

# Time: O(n), iterate over the list a max of one time
# Space: O(1), store two index ints and a sum int
class Solution:
    # This assumes all inputs have a solution
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lesserAddend = 0
        greaterAddend = len(numbers) - 1
        # Work through list until invalid result (index1 >= index2) occurs
        while lesserAddend < greaterAddend:
            currentSum = numbers[lesserAddend] + numbers[greaterAddend]
            if currentSum > target:
                greaterAddend = greaterAddend - 1
            elif currentSum < target:
                lesserAddend = lesserAddend + 1
            else:
                return [lesserAddend + 1, greaterAddend + 1]
