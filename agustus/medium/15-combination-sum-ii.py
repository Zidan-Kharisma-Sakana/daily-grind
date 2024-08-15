# https://leetcode.com/problems/combination-sum-ii/
# https://leetcode.com/problems/search-a-2d-matrix/
from collections import defaultdict
from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def recurse(idx, carry: List, total: int):
            if total == target:
                res.append(carry.copy())
            elif idx < len(candidates) and candidates[idx] + total <= target:
                for i in range(idx, len(candidates)):
                    if i > 0 and i > idx and candidates[i-1] == candidates[i]:
                        continue
                    carry.append(candidates[i])
                    total += candidates[i]
                    recurse(i+1, carry, total)
                    carry.pop()
                    total -= candidates[i]
        recurse(0, [], 0)
        return res
solution = Solution()

input = \
[2,5,2,1,2]
# [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# [0,3,7,2,5,8,4,6,0,1]
# input = [[1]]
input2 = \
5
result = solution.combinationSum2(input, input2)
print(result)

