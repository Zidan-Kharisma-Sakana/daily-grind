# https://leetcode.com/problems/single-number/
from collections import defaultdict
from typing import List
from heapq import heapify, heappop

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = nums[0]
        for i in range(1, len(nums)):
            n ^= nums[i]
        return n

input1 = \
    2
input2 = \
    3
result = Solution().singleNumber(input1)
print(result)