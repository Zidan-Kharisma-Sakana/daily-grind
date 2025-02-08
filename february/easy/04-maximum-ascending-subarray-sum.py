# https://leetcode.com/problems/maximum-ascending-subarray-sum
from typing import List
import math
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        highest = nums[0]
        cum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                highest = max(highest, cum)
                cum = 0
            cum += nums[i]
        highest = max(highest, cum)
        return highest
input = \
[12,17,15,13,10,11,12]


s = Solution()
result = s.maxAscendingSum(input)
print(result)