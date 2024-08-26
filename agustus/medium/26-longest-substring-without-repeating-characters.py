# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
from collections import defaultdict
from typing import List
class Solution:
    def lengthOfLongestSubstring(self, ss: str) -> int:
        d = set()
        mx = 0
        l, r = 0, 0
        while r < len(ss):
            while ss[r] in d:
                d.remove(ss[l])
                l+=1
            d.add(ss[r])
            mx = max(mx, len(d))
            r+=1
        return mx
solution = Solution()

input = \
'abcabcbb'
input2 = \
1

result = solution.lengthOfLongestSubstring(input)
print(result)

