# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
from collections import defaultdict
from typing import List
from heapq import heapify, heappop


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while numbers[l] + numbers[r] != target:
            if numbers[l] + numbers[r] > target:
                r-=1
            else:
                l+=1
        return [l+1, r+1]
    
input1 = \
[2,3,4]
# input2 = \
#     4
result = Solution().twoSum(input1, 6)
print(result)