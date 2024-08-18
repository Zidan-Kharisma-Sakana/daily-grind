# https://leetcode.com/problems/palindromic-substrings/
from collections import defaultdict
from typing import List
class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [1 for _ in s]
        for i in range(1, len(s)):
            count = 0
            # As if the middle is idx-0.5
            if s[i-1] == s[i]:
                l, r = i-1, i
                while 0<=l < r < len(s):
                    if s[l] == s[r]:
                        count += 1
                        l-=1
                        r+=1
                    else:
                        break
            l, r = i-1, i+1
            while 0<=l < r< len(s):
                if s[l] == s[r]:
                    count += 1
                    l-=1
                    r+=1
                else:
                    break
            dp[i] += count
        return sum(dp)
solution = Solution()

input = \
"aaad"

input2 = \
0
result = solution.countSubstrings(input)
print(result)

