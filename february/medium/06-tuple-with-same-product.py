# https://leetcode.com/problems/tuple-with-same-product
from collections import defaultdict
from typing import List, Optional, Tuple


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        memo = defaultdict(int)
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                memo[nums[i] * nums[j]] += 1
        result = 0
        for product in memo:
            if memo[product] > 1:
                num = memo[product]
                result += ((num * (num - 1)) /2) * 8
        return result

input1 = \
[1,2,4,5,10]
result = Solution().tupleSameProduct(input1)
print(result)