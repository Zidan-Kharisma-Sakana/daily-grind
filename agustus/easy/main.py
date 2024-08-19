# https://leetcode.com/problems/reverse-linked-list/
from typing import List, Optional
# Definition for singly-linked list.
from helper import Helper
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        prev, next, curr = None, None, head
        while curr :
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev
input = \
[7,6,4,3,1]
input2 = \
2
s = Solution()
print(s.maxProfit(input))