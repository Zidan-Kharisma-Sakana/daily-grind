# https://leetcode.com/problems/reverse-linked-list/
from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = None
        head = None
        while list1 and list2:
            if list2.val > list1.val:
                if curr:
                    curr.next = list1
                curr = list1
                list1 = list1.next
            else:
                if curr:
                    curr.next = list2
                curr = list2
                list2 = list2.next
            if not head:
                head = curr           
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        return head
input = \
[7,6,4,3,1]
input2 = \
2
s = Solution()
print(s.maxProfit(input))