# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx, highest, lowest = 0, prices[0], prices[0]
        for i in range(1, len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
                highest = 0
            elif prices[i] > highest:
                highest = prices[i]
                mx = max(highest-lowest, mx)
        return mx

input = \
[7,6,4,3,1]
input2 = \
2
s = Solution()
print(s.maxProfit(input))