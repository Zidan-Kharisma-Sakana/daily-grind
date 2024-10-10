# https://leetcode.com/problems/climbing-stairs/
from collections import defaultdict
from typing import List
from heapq import heapify, heappop

class Solution:
    def climbStairs(self, n: int) -> int:
        min1, min2 = 2,1
        if n == 1: return 1
        if n == 2: return 2
        for _ in range(3, n):
            new = min1 + min2
            min1, min2 = new, min1
        return min1 + min2

input1 = \
    4
input2 = \
    3
result = Solution().climbStairs(input1)
print(result)