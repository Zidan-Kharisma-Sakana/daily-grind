# https://leetcode.com/problems/longest-palindrome/description/
from collections import defaultdict
from typing import List, Optional
from utils.helper import ListNode, Helper, TreeNode
from typing import List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        def rec(r: TreeNode, l: List):
            if r.left is not None:
                # travel kiri
                rec(r.left, l)
            l.append(r.val)
            if r.right is not None:
                # travel kanan
                rec(r.right, l)
        if root is not None:
            rec(root, lst)
        return lst

input = \
[1,2,3,4,5,None,8,None,None,6,7,9]



# input2 = \
#     [3,1,2]
input = Helper.list_to_tree(input)
# input2 = Helper.list_to_tree(input2)
Helper.print_tree(input)
# Helper.print_tree(input2)
# input2 = Helper.list_to_linked_list(input2)

s = Solution()
result = s.inorderTraversal(input)
# result = Helper.linked_list_to_list(result)
print(result)