# https://leetcode.com/problems/search-in-rotated-sorted-array/
from collections import defaultdict
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        def recurse(left, right):
            if nums[left] <= nums[right]:
                return nums[left]
            if left + 1 == right and nums[left] > nums[right]:
                return nums[right]
            mid = (left + right) // 2
            if nums[left] < nums[mid]:
                return recurse(mid, right)
            return recurse(left, mid)
        return recurse(0, len(nums)-1)

solution = Solution()

input = \
[3,4,5,1,2]

input2 = \
0
result = solution.findMin(input)
print(result)

