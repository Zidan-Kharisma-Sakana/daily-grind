# https://leetcode.com/problems/top-k-frequent-elements/
from collections import defaultdict
from typing import List
from heapq import heapify, heappop


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        record = defaultdict(int)
        frequencies = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            record[num] += 1
        for num in record:
            frequencies[record[num]].append(num)
        result = []
        mx = len(nums)
        while len(result) < k:
            if len(frequencies[mx]) > 0:
                result.extend(frequencies[mx])
            mx -= 1
        return result[:k]
    
input1 = \
[1,1,1,2,2,3]
# input2 = \
#     4
result = Solution().topKFrequent(input1, 2)
print(result)