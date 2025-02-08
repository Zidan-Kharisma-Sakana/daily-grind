# https://leetcode.com/problems/integer-to-roman/description/
from collections import defaultdict
from typing import List, Optional, Tuple


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def intToRoman(self, num: int) -> str:
        romans = [
            ["I", 1],
            ["IV", 4],
            ["V", 5],
            ["IX", 9],
            ["X", 10],
            ["XL", 40],
            ["L", 50],
            ["XC", 90],
            ["C", 100],
            ["CD", 400],
            ["D", 500],
            ["CM", 900],
            ["M", 1000]
        ]
        result = ""
        while num > 0:
            last_idx = len(romans) - 1
            if num < romans[last_idx][1]:
                romans.pop()
            else:
                result += romans[last_idx][0]            
                num -= romans[last_idx][1]
        return result
        

input1 = \
58

result = Solution().intToRoman(input1)
print(result)