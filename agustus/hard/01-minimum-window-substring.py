# https://leetcode.com/problems/minimum-window-substring/description/
from collections import defaultdict
from typing import List
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        if s == t:
            return s
        d1 = defaultdict(int)
        for c in t:
            d1[c] += 1
        d2 = defaultdict(int)
        l, r = 0, 0
        mn = s
        flag = False
        def check(d1, d2):
            for k in d1:
                if d2[k] == 0:
                    return False
                if d1[k] > d2[k]:
                    return False
            return True


        while r<len(s):
            c = s[r]
            if c in d1:
                # try to add c to d2
                d2[c] += 1
                while True:
                    if s[l] not in d1:
                        l+=1
                    elif d2[s[l]] <= d1[s[l]]:
                        break
                    else:
                        d2[s[l]] -= 1
                        l+=1
                if (r-l+1) <= len(mn) and check(d1, d2):
                    flag = True
                    mn = s[l:r+1]
            r+=1
        # return r, l
        return mn if flag else ""
    
solution = Solution()

input = \
'abc'
input2 = \
'ac'

result = solution.minWindow(input, input2)
print(result)

