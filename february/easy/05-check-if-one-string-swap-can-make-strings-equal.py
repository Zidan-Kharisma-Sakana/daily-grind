# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description
from typing import List
import math
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2): return False
        if s1 == s2: return True
        suspectIdx = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                suspectIdx.append(i)
        if len(suspectIdx) > 2 or len(suspectIdx) == 1:
            return False
        [idx1, idx2] = suspectIdx
        s1 = list(s1)
        s1[idx1], s1[idx2] = s1[idx2], s1[idx1]
        return ''.join(s1) == s2
        

input1 = \
"kucing"

input2 = \
"kucgni"

s = Solution()
result = s.areAlmostEqual(input1, input2)
print(result)