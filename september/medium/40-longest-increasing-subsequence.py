# https://leetcode.com/problems/longest-increasing-subsequence/
from collections import defaultdict
from typing import List
from heapq import heapify, heappop

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lst = [nums[0]]
        def findFirst(x: int):
            l, r = 0, len(lst)-1
            while l <= r:
                m = (l+r) // 2
                if lst[m] == x:
                    return m
                elif lst[m] > x:
                    r = m - 1
                else:
                    l = m + 1
            return l
        
        for i in range(1, len(nums)):
            if nums[i] > lst[-1]:
                lst.append(nums[i])
            else:
                lst[findFirst(nums[i])] = nums[i]
        return len(lst)
input1 = \
    [10,9,2,5,3,7,101,18]
# input2 = \
#     4
result = Solution().lengthOfLIS(input1)
print(result)