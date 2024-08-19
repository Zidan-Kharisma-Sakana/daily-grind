# https://leetcode.com/problems/diameter-of-binary-tree/description/
from typing import List, Optional
from utils.helper import TreeNode, Helper

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def recurse(curr: Optional[TreeNode]) -> int:
            if not curr:
                return -1, -1
            LmaxLength, LmaxDepth = recurse(curr.left)
            RmaxLength, RmaxDepth = recurse(curr.right)
            maxLength = max(LmaxLength, RmaxLength, (LmaxDepth + RmaxDepth+2))
            maxDepth = max(LmaxDepth, RmaxDepth) + 1
            return maxLength, maxDepth

        return recurse(root)[0]
input = \
[1,2]

input = Helper.list_to_tree(input)
s = Solution()
Helper.print_tree(input)

result = s.diameterOfBinaryTree(input)
print(result)