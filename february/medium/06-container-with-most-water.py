# https://leetcode.com/problems/container-with-most-water/description/
from collections import defaultdict
from typing import List, Optional, Tuple

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        mx = 0
        while l < r:
            h = min(height[l], height[r])
            mx = max(mx, (r-l) * h)
            if height[l] > height[r]:
                r-=1
            else:
                l+=1
        return mx

input1 = \
[1,8,6,2,5,4,8,3,7]
result = Solution().maxArea(input1)
print(result)