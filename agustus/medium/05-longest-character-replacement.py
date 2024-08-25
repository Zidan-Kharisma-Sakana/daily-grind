# https://leetcode.com/problems/longest-repeating-character-replacement/description/
from typing import List
from collections import defaultdict, deque
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = [0 for _ in range(26)]
        chars = list(s)
        l, r = 0, 0
        mx = 0
        while r < len(chars):
            ordIdx = ord(chars[r]) - ord("A")
            d[ordIdx] += 1
            for x in d:
                mx = max(mx, x)
            if r - l + 1 > mx + k:
                ordIdxLeft = ord(chars[l]) - ord("A")
                d[ordIdxLeft] -= 1    
                l+=1
            r+=1
        return min(mx+k, len(chars))
        
solution = Solution()

input = \
"ABAA"
# input = [[1]]
result = solution.characterReplacement(input, 0)
print(result)

