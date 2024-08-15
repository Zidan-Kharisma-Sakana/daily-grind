# https://leetcode.com/problems/palindrome-partitioning/description/
# https://leetcode.com/problems/search-a-2d-matrix/
from collections import defaultdict
from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        def recurse(idx, carry: List):
            if idx == len(s):
                result.append(carry.copy())
            for i in range(idx, len(s)):
                if s[idx:i+1] == s[idx:i+1][::-1]:
                    carry.append(s[idx:i+1])
                    recurse(i+1, carry)
                    carry.pop()
        recurse(0, [])
        return result
solution = Solution()

input = \
"aab"
# [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# [0,3,7,2,5,8,4,6,0,1]
# input = [[1]]
input2 = \
2
result = solution.partition(input)
print(result)

