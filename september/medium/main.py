# https://leetcode.com/problems/valid-parenthesis-string/
from collections import defaultdict
from typing import List
from heapq import heapify, heappop

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        mx = 0
        currLowest, currHighest = nums[0], nums[0]
        pass
input1 = \
    [10,9,2,5,3,7,101,18]
# input2 = \
#     4
result = Solution().lengthOfLIS(input1)
print(result)