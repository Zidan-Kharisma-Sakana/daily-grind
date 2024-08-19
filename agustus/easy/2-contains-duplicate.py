# https://leetcode.com/problems/contains-duplicate/description/
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        exists = set()
        for i in nums:
            if i in exists:
                return True
            exists.add(i)
        return False

input = \
[1,1,1,3,3,4,3,2,4,2]
s = Solution()
print(s.containsDuplicate(input))