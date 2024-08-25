# https://leetcode.com/problems/same-tree/
from typing import List, Optional
from utils.helper import ListNode, Helper, TreeNode
from typing import List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        if not head:
            return False
        fast = head.next
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False

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