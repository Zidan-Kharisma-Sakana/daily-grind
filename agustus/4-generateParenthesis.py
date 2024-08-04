# https://leetcode.com/problems/generate-parentheses/
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []
        def rec(s: List, opening, closure):
            if len(s) + opening + closure != n*2 or opening < 0 or closure < 0 or opening > closure:
                s.pop()
            elif opening == closure == 0:
                result.append("".join(s))
            else:
                l = len(s)
                s.append("(")
                rec(s, opening-1, closure)
                while len(s) > l:
                    s.pop()
                s.append(")")
                rec(s, opening, closure-1)
  
        rec(stack, n, n)
        return result

solution = Solution()

input = \
4
# input = [[1]]
result = solution.generateParenthesis(input)
print(result)

