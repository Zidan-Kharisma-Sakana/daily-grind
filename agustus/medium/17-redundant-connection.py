# https://leetcode.com/problems/redundant-connection/description/
from collections import defaultdict
from typing import List
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        headLocation = [i for i in range(len(edges)+1)]
        listOfMembers = [[i] for i in range(len(edges)+1)]
        for fr, to in edges:
            print(fr, to)
            if headLocation[fr] == headLocation[to]:
                return [[fr, to]]
            headFr, headTo = headLocation[fr], headLocation[to]
            # if the member is a head, then reassign headLocation of its members
            for member in listOfMembers[headTo]:
                headLocation[member] = headFr
                listOfMembers[headFr].append(member)
    
solution = Solution()

input = \
[[1,2],[1,3],[2,3]]

# [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# [0,3,7,2,5,8,4,6,0,1]
# input = [[1]]
input2 = \
"SEE"
result = solution.findRedundantConnection(input)
print(result)

