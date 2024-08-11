# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        s = numbers[left] + numbers[right]
        while s != target:
            if s > target:
                right-=1
            else:
                left+=1
            s = numbers[left] + numbers[right]

        return [left+1, right+1]

solution = Solution()
input = \
[2,7,11,15]

# input = [[1]]
result = solution.twoSum(input, 9)
print(result)