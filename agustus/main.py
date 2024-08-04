from typing import List
from collections import deque

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        i = 0
        while i < len(nums) and nums[i] <= 0 and i - 2 < len(nums):
            if i == 0 or nums[i-1] != nums[i]:
                j = i + 1
                k = len(nums) - 1
                while j < k < len(nums):
                    res = nums[j] + nums[k]
                    if nums[j] == nums[j-1] and j > i + 1:
                        j+=1
                    elif res > nums[i] * -1:
                        k -= 1
                    elif res < nums[i] * -1:
                        j += 1
                    else:
                        result.append([nums[i], nums[j], nums[k]])
                        j+=1
            i+=1
        return result

solution = Solution()

input = \
[0,0,0]
# input = [[1]]
result = solution.threeSum(input)
print(result)