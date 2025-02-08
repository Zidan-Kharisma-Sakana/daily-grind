# https://leetcode.com/problems/zigzag-conversion/
from collections import defaultdict
from typing import List, Optional, Tuple


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        rows = defaultdict(list)
        currentRow = 0
        currentIdx = 0
        direction = 1
        while currentIdx < len(s):
            rows[currentRow].append(s[currentIdx])
            if currentRow + 1 == numRows:
                direction = -1
            elif currentRow == 0:
                direction = 1
            currentRow+=direction
            currentIdx+=1
        result = []
        for i in range(len(rows)):
            row = rows[i]
            for j in range(len(row)):
                result.append(row[j])
        return "".join(result)

input1 = \
"PAYPALISHIRING"

result = Solution().convert(input1, 3)
print(result)