# https://leetcode.com/problems/binary-search/description/
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return -1

input = \
[-1,0,3,5,9,12]
input2 = \
2
s = Solution()
print(s.search(input, input2))