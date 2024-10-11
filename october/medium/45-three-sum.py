# https://leetcode.com/problems/3sum/description/
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        pivot = 0
        output = []
        while pivot < len(nums) - 2 and nums[pivot] <= 0:
            while pivot > 0 and pivot < len(nums) and nums[pivot] == nums[pivot - 1]:
                pivot+=1
            left, right = pivot + 1, len(nums) - 1
            while left < right:
                total = nums[pivot] + nums[left] + nums[right]
                if total == 0:
                    output.append([nums[pivot], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1
            pivot += 1
        return output
    
input1 = \
    [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]


input2 = \
    3
print(Solution().threeSum(input1))