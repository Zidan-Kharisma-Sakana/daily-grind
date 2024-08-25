# https://leetcode.com/problems/same-tree/
from typing import List, Optional
from utils.helper import ListNode, Helper, TreeNode
from typing import List
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def recurse(root1: Optional[TreeNode], root2: Optional[TreeNode]):
            if root1 and root2:
                if root1.val != root2.val:
                    return False
                l = recurse(root1.left, root2.left)
                r = recurse(root1.right, root2.right)
                return l and r
            elif not root1 and not root2:
                return True
            else:
                return False
        return recurse(p, q)

input = \
[]


input = Helper.list_to_tree(input)
Helper.print_tree(input)
# input2 = Helper.list_to_linked_list(input2)

s = Solution()
result = s.isBalanced(input)
# result = Helper.linked_list_to_list(result)
print(result)