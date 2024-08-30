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
    def longestPalindrome(self, s: str) -> int:
        d = defaultdict(int)
        for char in s:
            d[char]+=1
        res = 0
        for k in d:
            if d[k] % 2 == 0:
                res += d[k]
                d[k] = 0
            else:
                res += d[k] - 1
                d[k] = 1
            print(k, res)
        for k in d:
            if d[k] > 0:
                res+=1
                break
        return res

input = \
"abccccdd"


# input2 = \
#     [3,1,2]
# input = Helper.list_to_tree(input)
# input2 = Helper.list_to_tree(input2)
# Helper.print_tree(input)
# Helper.print_tree(input2)
# input2 = Helper.list_to_linked_list(input2)

s = Solution()
result = s.longestPalindrome(input)
# result = Helper.linked_list_to_list(result)
print(result)