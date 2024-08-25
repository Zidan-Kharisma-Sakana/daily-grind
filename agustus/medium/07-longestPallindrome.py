from typing import List
from collections import defaultdict, deque
from math import ceil
class Solution:
    def longestPalindrome(self, s: str) -> str:
        idx = 0
        if len(s) < 2:
            return s
        dp = defaultdict(list)
        for i in range(len(s)):
            dp[i].append(i)
        
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                dp[i].append(i-1)
            for startOfPal in dp[i-1]:
                if startOfPal - 1 < 0:
                    break
                if s[startOfPal-1] == s[i]:
                    dp[i].append(startOfPal-1)
        
        max = ""
        for k in dp:
            i = dp[k]
            if i[0] - i[-1] >= len(max):
                max = s[i[-1]:i[0]+1]
        return max
        
solution = Solution()

input = \
"ac"
# input = [[1]]
input2 = \
5
result = solution.longestPalindrome(input)
print(result)

