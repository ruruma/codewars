# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
#
# Return the running sum of nums.


# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
from typing import List


def runningSum(nums: List[int]) -> List[int]:
    for position, number in enumerate(nums, 1):
        if position != len(nums):
            nums[position] = nums[position] + nums[position - 1]
        else:
            continue

    return nums


x = [1, 2, 3, 4]

print(runningSum(x))
