# https://leetcode.com/problems/count-number-of-bad-pairs/
from collections import defaultdict
from typing import List

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        result = 0
        count = defaultdict(int)
        for i in range(len(nums)):
            count[nums[i] - i] += 1
        for i in count:
            if count[i] > 1:
                result += (count[i] * (count[i] - 1)) // 2
        return ((len(nums) * (len(nums) -1)) // 2) - result

input = \
[5,4,3,2,1,0]

result = Solution().countBadPairs(input)
print(result)