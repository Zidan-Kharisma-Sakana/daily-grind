# https://leetcode.com/problems/gas-station/
from collections import defaultdict
from typing import List
from heapq import heapify, heappop

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        acc = 0
        i = -1
        for idx in range(len(gas)):
            if acc + gas[idx] < cost[idx]:
                acc = 0
                i = -1
            else:
                if i == -1:
                    i = idx
                acc += gas[idx]
                acc -= cost[idx]
        for idx in range(i):
            if acc + gas[idx] < cost[idx]:
                return -1
            acc += gas[idx]
            acc -= cost[idx]
        return i
            

input1 = \
    [1,2,3,4,5]
input2 = \
    [3,4,5,1,2]
result = Solution().canCompleteCircuit(input1, input2)
print(result)