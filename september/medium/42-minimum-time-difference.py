# https://leetcode.com/problems/minimum-time-difference/description/
# https://leetcode.com/problems/longest-increasing-subsequence/
from collections import defaultdict
from typing import List
from heapq import heapify, heappop

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        cache = set()
        for timePoint in timePoints:
            hr, m = timePoint.split(":")[0], timePoint.split(":")[1]
            t = int(hr)*60 + int(m)
            if t in cache:
                return 0
            cache.add(t)
            cache.add(t+1440)
        cache = list(cache)
        cache.sort()
        mn = cache[-1] - cache[0]
        for idx in range(1, len(timePoints)+1):
            if cache[idx] - cache[idx-1] < mn:
                mn = cache[idx] - cache[idx-1]
        return mn
        pass

input1 = \
["05:31","22:08","00:35"]
# input2 = \
#     4
result = Solution().findMinDifference(input1)
print(result)