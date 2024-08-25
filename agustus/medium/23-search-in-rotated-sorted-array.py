# https://leetcode.com/problems/search-in-rotated-sorted-array/
from collections import defaultdict
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            # left portion
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid -1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid +1
                else:
                    r = mid - 1
        return -1

solution = Solution()

input = \
[ 5, 1, 3]
input2 = \
5

result = solution.search(input, input2)
print(result)

