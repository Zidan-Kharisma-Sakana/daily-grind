# https://leetcode.com/problems/jump-game-ii/
from collections import defaultdict
from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums))]
        dp[len(nums)-1] = 0        
        for idx in range(len(nums)-2, -1, -1):
            count = nums[idx]
            mn = 10000
            for i in range(idx+1, min(len(nums), idx+count+1)):
                if mn > dp[i]:
                    mn = dp[i]
            dp[idx] = mn+1
        return dp[0]
solution = Solution()

input = \
[2,3,0,1,4]
# [0,3,7,2,5,8,4,6,0,1]
# input = [[1]]
input2 = \
10
result = solution.jump(input)
print(result)

