# https://leetcode.com/problems/subtree-of-another-tree/description/
from typing import List, Optional
from utils.helper import ListNode, Helper, TreeNode
from typing import List
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def recurse(p: Optional[TreeNode], q: Optional[TreeNode]):
            if p and q:
                if p.val != q.val:
                    if q == subRoot:
                        l = recurse(p.left, q)
                        r = recurse(p.right, q)
                        return l or r
                    return False
                else:
                    # if the val is the same, but it might not be the correct root
                    if q == subRoot:
                        l = recurse(p.left, q)
                        r = recurse(p.right, q)
                        if l or r:
                            return True                        
                    l = recurse(p.left, q.left)
                    r = recurse(p.right, q.right)
                    return l and r                    
            elif not p and not q:
                return True
            else:
                return False
        return recurse(root, subRoot)

input = \
[3,4,5,1,None,2]


input2 = \
    [3,1,2]
input = Helper.list_to_tree(input)
input2 = Helper.list_to_tree(input2)
Helper.print_tree(input)
Helper.print_tree(input2)
# input2 = Helper.list_to_linked_list(input2)

s = Solution()
result = s.isSubtree(input, input2)
# result = Helper.linked_list_to_list(result)
print(result)