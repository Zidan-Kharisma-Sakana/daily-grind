# https://leetcode.com/problems/hand-of-straights/description/
from collections import defaultdict
from typing import List
from heapq import heapify, heappop

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        d = defaultdict(int)
        for i in hand:
            d[i]+=1
        heapify(hand)
        while groupSize > 0 and len(d) > 0 and len(hand) > 0:
            if d[hand[0]] == 0:
                heappop(hand)
            else:
                start = heappop(hand)
                for i in range(groupSize):
                    if d[start+i] == 0:
                        print(start, i)
                        print(d[start+i])
                        return False
                    d[start+i] -= 1
        return True
            

input1 = \
    [1,8,4,6,2,3,3,7,2]
input2 = \
    3
result = Solution().isNStraightHand(input1, input2)
print(result)