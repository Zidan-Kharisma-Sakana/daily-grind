# https://leetcode.com/problems/word-break/
from collections import defaultdict
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [-1 for _ in range(len(s))]
        for idx in range(len(s)):
            for word in wordDict:
                if idx - (len(word)-1) < 0: continue
                firstCharIdx = idx - (len(word)-1)
                if firstCharIdx != 0 and dp[firstCharIdx-1] != 1: continue
                if s[firstCharIdx:idx+1] == word:
                    for i in range(firstCharIdx, idx):
                        dp[i] = max(dp[i], 0)
                    dp[idx] = 1
        return min(dp) >= 0
solution = Solution()

input = \
"abcd"

input2 = \
["a","abc","b","cd"]
result = solution.wordBreak(input, input2)
print(result)

