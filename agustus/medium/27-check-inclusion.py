# https://leetcode.com/problems/permutation-in-string/
from collections import defaultdict
from typing import List
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dA = defaultdict(int)
        for s in s1:
            dA[s] += 1
        l, r = 0, 0
        flag = False
        dB = defaultdict(int)
        
        def twoDictSame(d1, d2):
            if len(d1) != len(d2):
                return False
            for k in d1:
                if d1[k] != d2[k]:
                    return False
            return True
        
        while r < len(s2) and not flag:
            s = s2[r]
            dB[s] += 1
            if twoDictSame(dA, dB):
                flag = True
            if s not in dA:
                dB = defaultdict(int)
            else:
                while dB[s] > dA[s]:
                    dB[s2[l]] -= 1
                    l+=1
            r+=1
        return flag
            
solution = Solution()

input = \
'acd'
input2 = \
'dcda'

result = solution.checkInclusion(input, input2)
print(result)

