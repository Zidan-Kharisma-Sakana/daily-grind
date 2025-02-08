# https://leetcode.com/problems/longest-palindromic-substring/
from typing import List, Optional, Tuple


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1: return s
        dp = [] # indexes of the start of possible pallindrome that ended in i
        for i in range(len(s)):
            dp.append([i])
        
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                dp[i].append(i-1)
            for start in dp[i-1]:
                if start - 1 < 0:
                    continue
                if s[start-1] == s[i]:
                    dp[i].append(start-1)
            
        maximum = ""
        for i in range(len(dp)):
            for j in range(len(dp[i])):
                length = i - dp[i][j] + 1
                if length > len(maximum):
                    maximum = s[dp[i][j]:i+1]
        return maximum
        

input1 = \
"babad"

result = Solution().longestPalindrome(input1)
print(result)