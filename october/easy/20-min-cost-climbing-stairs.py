# https://leetcode.com/problems/min-cost-climbing-stairs/description/
from collections import defaultdict
from typing import List
from heapq import heapify, heappop

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        min2, min1 = [0, 0], [0, 0]
        if len(cost) < 2:
            return 0
        for idx in range(2, len(cost)):
            new = [min(min1)+ cost[idx-1], min(min2) + cost[idx-2]]
            min1, min2 = new, min1
        return min(min1)

input1 = \
    [1,100,1,1,1,100,1,1,100,1]
input2 = \
    3
result = Solution().minCostClimbingStairs(input1)
print(result)