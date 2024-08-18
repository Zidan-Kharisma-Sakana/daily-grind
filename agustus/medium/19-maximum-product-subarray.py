# https://leetcode.com/problems/maximum-product-subarray/
from collections import defaultdict
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        positive = [0 for i in range(len(nums))]
        negative = [0 for i in range(len(nums))]
        positive[0] = max(nums[0], 0)
        negative[0] = min(nums[0], 0)
        for i in range(1, len(nums)):
            if nums[i] > 0:
                positive[i] = max(positive[i-1] * nums[i], nums[i])
                negative[i] = min(negative[i-1] * nums[i], nums[i])
            elif nums[i] < 0:
                positive[i] = max(negative[i-1] * nums[i], nums[i])
                negative[i] = min(positive[i-1] * nums[i], nums[i])
        return max(positive)
solution = Solution()

input = \
[-2,3, 0, -1, 4, -2]

result = solution.maxProduct(input)
print(result)

