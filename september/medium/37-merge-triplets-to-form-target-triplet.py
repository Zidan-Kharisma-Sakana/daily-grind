# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/
from collections import defaultdict
from typing import List
from heapq import heapify, heappop

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        mx = [0,0,0]
        for i in triplets:
            if i[0] > target[0] or i[1] > target[1] or i[2] > target[2]:
                continue
            mx = [max(mx[0], i[0]), max(mx[1], i[1]), max(mx[2], i[2])]
        return mx[0] == target[0] and mx[1] == target[1] and mx[2] == target[2]

input1 = \
    [[2,5,3],[1,8,4],[1,7,5]]
# input2 = \
#     4
result = Solution().mergeTriplets(input1, [2,7,5])
print(result)