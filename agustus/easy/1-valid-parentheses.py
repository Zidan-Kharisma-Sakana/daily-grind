# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        opening = ["(", "{", "["]
        closures = [")", "}", "]"]
        couples = [("(", ")"), ("{", "}"), ("[", "]")]
        stack = []
        for idx, curr in enumerate(s):
            if len(stack) == 0:
                if curr in closures:
                    return False
                stack.append(curr)
            else:
                prev = stack[len(stack)-1]
                flag = False
                for couple in couples:
                    if prev == couple[0] and curr == couple[1]:
                        stack.pop()
                        flag = True
                        break
                if not flag:
                    stack.append(curr)
        return len(stack) == 0

input = \
"(){[]}"
s = Solution()
print(s.isValid(input))