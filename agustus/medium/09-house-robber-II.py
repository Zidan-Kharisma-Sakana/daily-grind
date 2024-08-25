from typing import List
from collections import defaultdict, deque
from math import ceil
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp_inc = nums[0]
        dp_inc_n0 = 0
        dp_ninc = 0
        dp_ninc_n0 = 0
        for idx in range(1, len(nums)-1):
            a = nums[idx] + dp_ninc
            b = nums[idx] + dp_ninc_n0
            c = max(dp_inc, dp_ninc)
            d = max(dp_inc_n0, dp_ninc_n0)
            dp_inc, dp_inc_n0, dp_ninc, dp_ninc_n0 = a,b,c,d

        lastIdx = len(nums) - 1
        b = nums[lastIdx] + dp_ninc_n0
        d = max(dp_inc_n0, dp_ninc_n0)

        return max(dp_inc, dp_inc_n0, dp_ninc, dp_ninc_n0, b, d)
        
solution = Solution()

input = \
[2,3,2]
# input = [[1]]
input2 = \
5
result = solution.rob(input)
print(result)

