# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
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
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def recursive(start, end):
            if end < 0 or start >= len(nums) or start > end:
                return None
            mid = (start + end) // 2
            midNode = TreeNode(nums[mid])
            # find left
            leftTree = recursive(start, mid - 1)
            # find right
            rightTree = recursive(mid+1, end)
            midNode.left = leftTree
            midNode.right = rightTree
            return midNode
        return recursive(0, len(nums)-1)

input = \
[1, 3, 6, 7]



# input2 = \
#     [3,1,2]
# input = Helper.list_to_tree(input)
# input2 = Helper.list_to_tree(input2)
# Helper.print_tree(input)
# Helper.print_tree(input2)
# input2 = Helper.list_to_linked_list(input2)

s = Solution()
result = s.sortedArrayToBST(input)
print(result)
Helper.print_tree(result)

# result = Helper.linked_list_to_list(result)
# print(result)