# https://leetcode.com/problems/path-sum-iii/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
from typing import List, Optional
from utils.helper import Helper, TreeNode

class Solution:
    def pathSum(self, r: Optional[TreeNode], target: int) -> List[List[int]]:
        defD = defaultdict(int)
        def recurse(root:Optional[TreeNode], currSum: int):
            if root is None: 
                return 0
            currSum += root.val
            result = 0
            if currSum == target:
                result += 1
            if (currSum - target) in defD:
                result += defD[currSum - target]
            defD[currSum] += 1
            result += recurse(root.left, currSum) + recurse(root.right, currSum)
            defD[currSum] -= 1
            return result
            
        return recurse(r, 0)

input = \
[10,5,-3,3,2,None,11,3,-2,None,1]
# input2 = \
#     [3,1,2]
input = Helper.list_to_tree(input)
# input2 = Helper.list_to_tree(input2)
Helper.print_tree(input)
# Helper.print_tree(input2)
# input2 = Helper.list_to_linked_list(input2)

s = Solution()
result = s.pathSum(input, 8)
print(result)
# Helper.print_tree(result)

# result = Helper.linked_list_to_list(result)
# print(result)