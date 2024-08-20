# https://leetcode.com/problems/merge-two-sorted-lists/description/
from typing import List, Optional
from utils.helper import ListNode, Helper

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        curr = None
        while list1 or list2:
            if not list1 and list2:
                if curr:
                    curr.next = list2
                else:
                    curr = list2
                break
            if list1 and not list2:
                if curr:
                    curr.next = list1
                else:
                    curr = list1
                break
            if list1.val < list2.val:
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
        
        if not head:
            head = curr
        return head
input = \
[10, 13, 100]

input2 = \
[-1, 0, 11, 12, 99, 101]

input = Helper.list_to_linked_list(input)
input2 = Helper.list_to_linked_list(input2)

s = Solution()
result = s.mergeTwoLists(input, input2)
result = Helper.linked_list_to_list(result)
print(result)