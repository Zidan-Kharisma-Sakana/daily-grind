# https://leetcode.com/problems/coin-change/description/
from collections import defaultdict
from typing import List
class Solution:
    def coinChange(self, c: List[int], amount: int) -> int:
        coins = []
        if amount == 0:
            return 0
        dp = [10000 for _ in range(amount+1)]
        dp[0] = 0
        for x in c:
            if x <= amount:
                coins.append(x)
                dp[x] = 1
        coins.sort(reverse=True)
        for coin in coins:
            for idx in range(coin+1, amount):
                dp[idx] = min(dp[idx], dp[idx-coin] + 1)
        minimal = 10000
        for i in range((amount // 2) + 1):
            minimal = min(minimal, dp[i]+dp[amount-i])
        return -1 if minimal > amount else minimal
    
solution = Solution()

input = \
[2,6,10, 31]
# [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# [0,3,7,2,5,8,4,6,0,1]
# input = [[1]]
# 443
input2 = \
31
result = solution.coinChange(input, input2)
print(result)

