# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = set()
        pointer = 0
        for i in range(len(nums)):
            if nums[i] not in unique:
                nums[pointer] = nums[i]
                pointer+=1
                unique.add(nums[i])
        return pointer
    
input = \
[1, 1, 2, 3, 7, 8, 2]


s = Solution()
result = s.removeDuplicates(input)
print(result)