from typing import List
from collections import defaultdict, deque
from math import ceil
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp_included = nums[0]
        dp_not_included = 0
        for idx in range(1, len(nums)):
            dp_included, dp_not_included = nums[idx] + dp_not_included, max(dp_included, dp_not_included)
        return max(dp_not_included, dp_included)
        
solution = Solution()

input = \
[5, 1, 1, 12]
# input = [[1]]
input2 = \
5
result = solution.rob(input)
print(result)

