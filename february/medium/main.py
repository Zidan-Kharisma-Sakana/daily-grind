# https://leetcode.com/problems/clear-digits/description
from collections import defaultdict
import heapq
from typing import List

class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for i in s:
            if i.isnumeric() and len(stack) > 0:
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)

input = \
"cba34"

result = Solution().clearDigits(input)
print(result)

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)