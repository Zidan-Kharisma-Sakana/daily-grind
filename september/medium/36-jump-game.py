# https://leetcode.com/problems/jump-game/
from collections import defaultdict
from typing import List
from heapq import heapify, heappop

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mx = 0
        idx = 0
        while mx < len(nums) - 1:
            if idx > mx:
                return False
            mx = max(mx, nums[idx] + idx)
            idx+=1
        return True

input1 = \
    [2,3,1,1,4]
# input2 = \
#     4
result = Solution().canJump(input1)
print(result)