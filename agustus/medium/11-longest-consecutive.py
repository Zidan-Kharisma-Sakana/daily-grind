from collections import defaultdict
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        mx = 0
        for num in nums:
            if (num - 1) not in nums:
                count = 0
                while (num+count) in nums:
                    count+=1
                mx = max(mx, count)
        return mx
solution = Solution()

input = \
[0,3,7,2,5,8,4,6,0,1]
# input = [[1]]
input2 = \
10
result = solution.longestConsecutive(input)
print(result)

