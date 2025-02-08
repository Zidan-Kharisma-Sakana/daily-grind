# https://leetcode.com/problems/add-two-numbers/
from typing import List, Optional, Tuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def countNodeLength(self, l: Optional[ListNode]) -> int:
        if l is None:
            return 0
        head = l
        count = 0
        while head:
            count +=1
            head = head.next
        return count

    def addTwoNumbers(self, l_one: Optional[ListNode], l_two: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        l1, l2 = l_one, l_two
        returned_node = l_one
        if self.countNodeLength(l_one) < self.countNodeLength(l_two):
            l1, l2 = l_two, l_one
            returned_node = l_two
        
        while l1 and l2:
            sum = l1.val + l2.val + carry
            carry = 0
            if sum > 9:
                carry = (sum - sum % 10) // 10
                sum = sum % 10
            l1.val = sum
            l2.val = sum
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            sum = l1.val + carry
            carry = 0
            if sum > 9:
                carry = (sum - sum % 10) // 10
                sum = sum % 10
            l1.val = sum
            l1 = l1.next
        
        if carry > 0:
            last_node = returned_node
            while last_node.next:
                last_node = last_node.next
            last_node.next = ListNode(carry)

        return returned_node
        
        
        
        
            


l1 = ListNode(1, ListNode(2, ListNode(3)))
l2 = ListNode(4, ListNode(9, ListNode(6)))

result = Solution().addTwoNumbers(l1, l2)

while result:
    print(result.val)
    result = result.next