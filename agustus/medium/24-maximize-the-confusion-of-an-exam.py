# https://leetcode.com/problems/maximize-the-confusion-of-an-exam/description/
from collections import defaultdict
from typing import List
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l, r = 0, 0
        mx = 0
        d = {}
        d["T"] = 0
        d["F"] = 0
        while r < len(answerKey):
            d[answerKey[r]] += 1
            mx = max(mx, d[answerKey["T"]], d[answerKey["F"]])
            if r - l >= mx + k:
                d[answerKey[l]] -= 1
                l+=1
            r+=1
        return min(mx+k, len(answerKey))

solution = Solution()

input = \
'TTFTTFTT'
input2 = \
1

result = solution.search(input, input2)
print(result)

