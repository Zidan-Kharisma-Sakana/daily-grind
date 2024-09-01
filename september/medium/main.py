# https://leetcode.com/problems/path-sum-iii/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional
from utils.helper import Helper, TreeNode

class Solution:
    def pathSum(self, r: Optional[TreeNode], target: int) -> List[List[int]]:
        def recurse(root: Optional[TreeNode], targetSum: int):
            if not root:
                return 0
            if not root.left and not root.right:
                return 1 if targetSum == root.val else 0
            ansFromLeft = recurse(root.left, targetSum-root.val) + recurse(root.left, target-root.val)
            ansFromRight = recurse(root.right, targetSum-root.val) + recurse(root.right, target-root.val)
            ansFromCurrent = 1 if targetSum == root.val else 0
            print(root.val, targetSum, ansFromLeft, ansFromRight, ansFromCurrent)
            return ansFromCurrent+ansFromLeft+ansFromRight
        return recurse(r, target)

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