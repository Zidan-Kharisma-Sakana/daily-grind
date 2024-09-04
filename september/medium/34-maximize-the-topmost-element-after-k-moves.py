# https://leetcode.com/problems/maximize-the-topmost-element-after-k-moves/
from collections import defaultdict
from typing import List
from heapq import heapify, heappop

class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            if k%2 != 0:
                return -1
            return nums[0]
        
        if k == 0:
            return nums[0]
        if k == len(nums):
            return max(nums[:-1])
        if k > len(nums):
            return max(nums)
        if k == 1:
            return nums[1]
        m = max(nums[:k-1])
        m = max(m, nums[k])
        return m  

input1 = \
    [5,2,2,4,0,6]
input2 = \
    4
result = Solution().canCompleteCircuit(input1, input2)
print(result)