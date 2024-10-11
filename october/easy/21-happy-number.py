# https://leetcode.com/problems/happy-number/
from collections import defaultdict
from typing import List
from heapq import heapify, heappop

class Solution:
    def isHappy(self, n: int) -> bool:
        num = set()
        while n not in num:
            if n == 1:
                return True
            num.add(n)
            temp = 0
            while True:
                if n < 10:
                    temp += n * n
                    break
                lastDigit = n % ((n // 10) * 10)
                temp += lastDigit * lastDigit
                n = n // 10
            n = temp
        return False

input1 = \
    2
input2 = \
    3
result = Solution().isHappy(input1)
print(result)