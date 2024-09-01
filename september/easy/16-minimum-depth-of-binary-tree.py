# https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from utils.helper import ListNode, Helper, TreeNode


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if not root.left and not root.right:
            return 1
        depthLeft = self.minDepth(root.left)
        depthRight = self.minDepth(root.right)
        if depthLeft == 0:
            return depthRight + 1
        elif depthRight == 0:
            return depthLeft + 1
        return min(depthLeft, depthRight) + 1

input = \
[3,9,20,None,None,15,7]
# input2 = \
#     [3,1,2]
input = Helper.list_to_tree(input)
# input2 = Helper.list_to_tree(input2)
Helper.print_tree(input)
# Helper.print_tree(input2)
# input2 = Helper.list_to_linked_list(input2)

s = Solution()
result = s.minDepth(input)
print(result)
# Helper.print_tree(result)

# result = Helper.linked_list_to_list(result)
# print(result)