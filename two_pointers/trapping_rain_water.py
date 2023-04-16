#!/usr/bin/python3

# Time: O(n), performs only a series of O(n) operations
# Space: O(n), stores a few lists of size n

class Solution:
    def trap(self, height: List[int]) -> int:
        totalWater = 0
        # splitting the list to find max is too slow, must iterate once each to populate lists
        # left side
        leftList = []
        tempMax = 0
        for h in height:
            leftList.append(tempMax)
            if h > tempMax:
                tempMax = h
        
        # right side
        rightList = []
        tempMax = 0
        for h in reversed(height):
            rightList.append(tempMax)
            if h > tempMax:
                tempMax = h
        rightList.reverse()

        # iterate over list for water calculation
        for currentIndex, currentValue in enumerate(height):
            # find the water that can be held in current location
            # the lower of the left and right peaks minus the current is what water can pool here
            minHeight = min(leftList[currentIndex], rightList[currentIndex])
            waterHere = minHeight - currentValue
            # if the water that can pool here is > 0, it should be added to total
            if waterHere > 0:
                totalWater += waterHere
        return totalWater
