# https://leetcode.com/problems/valid-parenthesis-string/
from collections import defaultdict
from typing import List
from heapq import heapify, heappop

class Solution:
    def checkValidString(self, s: str) -> bool:
        d = defaultdict(bool)
        def recurse(idx, balance, dp):
            if idx == len(s):
                return balance == 0
            if balance < 0:
                return False
            if f"{idx}:{balance}" in dp:
                return dp[f"{idx}:{balance}"]
            flag = False
            if s[idx] == "(":
                flag = recurse(idx+1, balance+1, dp)
            elif s[idx] == ")":
                flag = recurse(idx+1, balance-1, dp)
            else:
                flag = recurse(idx+1, balance, dp) or \
                    recurse(idx+1, balance-1, dp) or \
                    recurse(idx+1, balance+1, dp)
            dp[f"{idx}:{balance}"] = flag
            return flag
        return recurse(0, 0, d)
input1 = \
    "(*))"
# input2 = \
#     4
result = Solution().checkValidString(input1)
print(result)