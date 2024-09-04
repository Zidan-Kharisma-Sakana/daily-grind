# https://leetcode.com/problems/maximum-subarray/
from collections import defaultdict
from typing import List
from heapq import heapify, heappop

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx, curr = nums[0], nums[0]
        for idx in range(1, len(nums)):
            if curr < 0:
                curr = nums[idx]
            else:
                curr+= nums[idx]
            if curr > mx:
                mx = curr
        return mx

input1 = \
    [-2,1,-3,4,-1,2,1,-5,4]
input2 = \
    4
result = Solution().maxSubArray(input1)
print(result)