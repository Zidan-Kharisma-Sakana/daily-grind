# https://leetcode.com/problems/jump-game-ii/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
from typing import List, Optional
from utils.helper import Helper, TreeNode

class Solution:
    def jump(self, nums: List[int]) -> int:
        mx, jmp = 0,0
        l, r = 0,0
        while mx < len(nums) - 1:
            for idx in range(l, r+1):
                if nums[idx]+idx > mx:
                    mx = nums[idx]+idx
            l,r = r+1, mx
            jmp+=1
        return jmp
    

input = \
[2,3,1,1,4]


# input2 = \
#     [3,1,2]
# input = Helper.list_to_tree(input)
# input2 = Helper.list_to_tree(input2)
# Helper.print_tree(input)
# Helper.print_tree(input2)
# input2 = Helper.list_to_linked_list(input2)

s = Solution()
result = s.jump(input)
print(result)
# Helper.print_tree(result)

# result = Helper.linked_list_to_list(result)
# print(result)