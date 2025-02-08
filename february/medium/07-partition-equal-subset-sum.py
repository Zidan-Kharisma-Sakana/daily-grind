# https://leetcode.com/problems/partition-equal-subset-sum/
from collections import defaultdict
from typing import List, Optional, Tuple

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 1: return False
        the_sum = sum(nums)
        if the_sum % 2 == 1: return False
        half_sum = the_sum // 2
        seen = set()
        for i in range(len(nums)):
            current_seen = set()
            current_seen.add(nums[i])
            for j in seen:
                possible_sum = j + nums[i]
                if possible_sum <= half_sum:
                    current_seen.add(possible_sum)
            seen = seen.union(current_seen)
            if half_sum in seen:
                return True
        return False

input1 = \
[1,5,11,5]
result = Solution().canPartition(input1)
print(result)