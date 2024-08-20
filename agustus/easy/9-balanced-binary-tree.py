# https://leetcode.com/problems/balanced-binary-tree/description/
from typing import List, Optional
from utils.helper import ListNode, Helper, TreeNode
from typing import List
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def recurse(curr: Optional[TreeNode], step: int):
            if not curr:
                return step
            left = recurse(curr.left, step+1)
            right = recurse(curr.right, step+1)
            if abs(left-right) > 1:
                return -1
            return max(left, right)
        return recurse(root, 0) >= 0

input = \
[]


input = Helper.list_to_tree(input)
Helper.print_tree(input)
# input2 = Helper.list_to_linked_list(input2)

s = Solution()
result = s.isBalanced(input)
# result = Helper.linked_list_to_list(result)
print(result)