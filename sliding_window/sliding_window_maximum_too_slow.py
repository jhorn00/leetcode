#!/usr/bin/python3

# Time: O(
# Space: O(

def maxSlidingWindow(nums, k):
        # initialize window
        left = 0
        right = k - 1
        maxIndex = 0
        for i in range(left, right + 1):
            if nums[i] >= nums[maxIndex]:
                maxIndex = i
        print(maxIndex)
        print(left)
        print(right)
        # slide window
        result = []
        while right < len(nums):
            if nums[right] >= nums[maxIndex]:
                maxIndex = right
            elif maxIndex < left:
                maxIndex = left
                for i in range(left, right + 1):
                    print("i " + str(i))
                    if nums[i] >= nums[maxIndex]:
                        maxIndex = i
            result.append(nums[maxIndex])
            right += 1
            left += 1

        return result

# nums = [1,3,-1,-3,5,3,6,7]
nums = [1, -1]
k = 1
print(maxSlidingWindow(nums, k))