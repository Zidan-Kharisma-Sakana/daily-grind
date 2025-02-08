# https://leetcode.com/problems/reverse-string-ii/
from typing import List
import math
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        numOfReversal = math.ceil(len(s) / (2 * k))
        result = ""
        for i in range(numOfReversal):
            minIndexReversed = i*2*k
            maxIndexReversed = min(minIndexReversed + k, len(s))
            reversedSub = s[minIndexReversed:maxIndexReversed]
            result += reversedSub[::-1]
            minIndex = maxIndexReversed
            maxIndex = min(minIndex + k, len(s))
            normalSub = s[minIndex:maxIndex]
            result += normalSub
        return result
    
input = \
"abcdefgs"


s = Solution()
result = s.reverseStr(input, 2)
print(result)