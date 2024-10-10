# https://leetcode.com/problems/valid-parentheses/description/
from collections import defaultdict
from typing import List
from heapq import heapify, heappop

class Solution:
    def isValid(self, s: str) -> bool:
        op = ["{", "[", "("]
        cl = ["}", "]", ")"]
        st = []
        for curr in st:
            if len(st) > 0 and st[-1] in op and curr in cl:
                if op.index(st[-1]) == cl.index(curr):
                    st.pop()
                    continue
            st.append(curr)
        return len(st) == 0

input1 = \
    "(]"
input2 = \
    3
result = Solution().isValid(input1)
print(result)