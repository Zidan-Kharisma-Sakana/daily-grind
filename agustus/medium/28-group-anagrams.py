# https://leetcode.com/problems/group-anagrams/
from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        k=[]
        for i in strs:
            l="".join(sorted(i))
            dic.setdefault(l,[]).append(i)
      
        return dic.values()
solution = Solution()

input = \
["eat","tea","tan","ate","nat","bat"]

input2 = \
'ac'

result = solution.groupAnagrams(input)
print(result)

