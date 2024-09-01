# https://leetcode.com/problems/symmetric-tree/description/
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def recLeft(r: Optional[TreeNode], l: List):
            if not r:
                l.append(-1)
                return
            if not r.left and not r.right:
                l.append(r.val)
                return
            recLeft(r.left, l)
            recLeft(r.right, l)
            l.append(r.val)
            
        def recRight(r: Optional[TreeNode], l: List):
            if not r:
                l.append(-1)
                return
            if not r.left and not r.right:
                l.append(r.val)
                return
            recRight(r.right, l)
            recRight(r.left, l)
            l.append(r.val)
        
        lLeft = []
        lRight = []
        recLeft(root.left, lLeft)
        recRight(root.right, lRight)
        # print(lLeft)
        # print(lRight)
        if len(lLeft) != len(lRight): return False
        for i in range(0, len(lLeft)):
            if lLeft[i] != lRight[i]: return False
        return True

input = \
[5,4,1,None,1,None,4,2,None,2,None]

# input2 = \
#     [3,1,2]
input = Helper.list_to_tree(input)
# input2 = Helper.list_to_tree(input2)
Helper.print_tree(input)
# Helper.print_tree(input2)
# input2 = Helper.list_to_linked_list(input2)

s = Solution()
result = s.isSymmetric(input)
print(result)
# Helper.print_tree(result)

# result = Helper.linked_list_to_list(result)
# print(result)