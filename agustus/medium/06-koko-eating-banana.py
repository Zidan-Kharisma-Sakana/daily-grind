# https://leetcode.com/problems/koko-eating-bananas/description/
from typing import List
from collections import defaultdict, deque
from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def getTotalHours(n):
            p = 0
            for i in range(len(piles)):
                p += ceil(piles[i] / n)
            return p
        
        small, big = 1, max(piles)
        answer = -1
        while small <= big:
            mid = (small + big) // 2
            res = getTotalHours(mid)
            if res > h:
                small = mid + 1
            else:
                big = mid - 1
                answer = mid
            
        return answer
        
solution = Solution()

input = \
[30,11,23,4,20]
# input = [[1]]
input2 = \
5
result = solution.minEatingSpeed(input, input2)
print(result)

