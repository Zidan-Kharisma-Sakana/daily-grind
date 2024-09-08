# https://leetcode.com/problems/partition-labels/description/
from collections import defaultdict
from typing import List
from heapq import heapify, heappop

class Solution:
    def partitionLabels(self, string: str) -> List[int]:
        chars = [[-1,-1] for _ in range(26)]
        for i in range(len(string)):
            s = string[i]
            char = ord(s) - ord('a')
            if chars[char][0] < 0:
                chars[char][0] = i
            chars[char][1] = i
        result = []
        fast, slow = 0, -1
        for i in range(len(string)):
            s = string[i]
            char = ord(s) - ord('a')
            if chars[char][1] > fast:
                fast = chars[char][1]
            if i == fast:
                result.append(fast-slow)
                slow = i
        
        return result
input1 = \
    "ababcbacadefegdehijhklij"
# input2 = \
#     4
result = Solution().partitionLabels(input1)
print(result)