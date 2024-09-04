# https://leetcode.com/problems/path-sum-ii/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional
from utils.helper import ListNode, Helper, TreeNode


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = self.recurse(root, targetSum)
        return [a[::-1] for a in res]

    def recurse(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        if not root.left and not root.right:
            if targetSum == root.val:
                return [[root.val]]
            return []
        ansFromLeft = self.recurse(root.left, targetSum-root.val)
        ansFromRight = self.recurse(root.right, targetSum-root.val)
        result = []
        for ans in ansFromLeft:
            ans.append(root.val)
            result.append(ans)
        for ans in ansFromRight:
            ans.append(root.val)
            result.append(ans)
        return result

input = \
[5,4,8,11,None,13,4,7,2,None,None,None,5,1]
# input2 = \
#     [3,1,2]
input = Helper.list_to_tree(input)
# input2 = Helper.list_to_tree(input2)
Helper.print_tree(input)
# Helper.print_tree(input2)
# input2 = Helper.list_to_linked_list(input2)

s = Solution()
result = s.pathSum(input, 22)
print(result)
# Helper.print_tree(result)

# result = Helper.linked_list_to_list(result)
# print(result)