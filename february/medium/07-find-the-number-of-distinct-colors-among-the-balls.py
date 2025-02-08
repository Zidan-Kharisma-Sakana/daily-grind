# https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls
from collections import defaultdict
from typing import List, Optional, Tuple

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls = defaultdict(int)
        colours = defaultdict(set)
        result = []
        num_of_active_colour = 0
        for query in queries:
            [ball_idx, colour_idx] = query
            # check what's current colour of ball
            old_colour_idx = balls[ball_idx]
            balls[ball_idx] = colour_idx
            # remove ball_idx in colours based on old colour idx, then if the set's empty decrease num_of_active_colour.
            if old_colour_idx > 0:
                old_colours = colours[old_colour_idx]
                old_colours.remove(ball_idx)
                if len(old_colours) == 0:
                    num_of_active_colour -= 1
            # add ball_idx, if it's previously empty, add num_of_active_colour
            new_colours = colours[colour_idx]
            if len(new_colours) == 0:
                num_of_active_colour += 1
            new_colours.add(ball_idx)
            # add to result
            result.append(num_of_active_colour)
        return result

input1 = \
[[0,1],[1,2],[2,2],[3,4],[4,5]]
result = Solution().queryResults(4, input1)
print(result)