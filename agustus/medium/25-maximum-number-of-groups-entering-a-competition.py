# https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition/
from collections import defaultdict
from typing import List
class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        l, r = 0, len(grades)
        n = 0
        while l <= r:
            m = (l+r) // 2
            sum = m * (m+1) // 2
            if sum <= len(grades):
                n = m
                l = m + 1
            else:
                r = m -1
        return n
solution = Solution()

input = \
[10,6,12,7,3,5]
input2 = \
1

result = solution.maximumGroups(input)
print(result)

