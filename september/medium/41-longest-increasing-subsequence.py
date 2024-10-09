# https://leetcode.com/problems/longest-increasing-subsequence/
from collections import defaultdict
from typing import List
from heapq import heapify, heappop

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        dp_without = [0 for _ in range(len(s))]
        dp_with = [0 for _ in range(len(s))]
        dp_without[0] = 1
        def isValid(x: str):
            if x.isdigit():
                return 0 < int(x) <= 26
            return False
        
        for i in range(1, len(s)):
            if s[i-1:i+1] == "00":
                return 0 # impossible
            if isValid(s[i]):
                dp_without[i] = dp_without[i-1] + dp_with[i-1]
            if isValid(s[i-1]+s[i]):
                dp_with[i] = dp_without[i-1]
        return dp_without[-1] + dp_with[-1]
input1 = \
    "226"
# input2 = \
#     4
result = Solution().numDecodings(input1)
print(result)