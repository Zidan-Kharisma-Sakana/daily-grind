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
        
        while groupSize > 0 and len(d) > 0:
            print(hand)
            if hand[0] not in d:
                heappop(hand)
            else:
                start = hand[0]
                for i in range(groupSize):
                    if d[start+1] == 0:
                        return False
                    d[start+1] -= 1
        return True
            

input1 = \
    [1,2,3,6,2,3,4,7,8]
input2 = \
    3
result = Solution().isNStraightHand(input1, input2)