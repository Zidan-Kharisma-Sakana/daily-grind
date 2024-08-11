from typing import List
from collections import deque

class Solution:
    def initDp(self, heights: List[List[int]]):
        pacificDP = [[False for _ in i ] for i in heights]
        atlanticDP = [[False for _ in i ] for i in heights]
        return pacificDP, atlanticDP
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacificDP, atlanticDP = self.initDp(heights)
        for r in range(len(heights)):
            self.dfs(pacificDP, r, 0, r, 0, heights)
            self.dfs(atlanticDP, r, len(heights[0])-1, r, len(heights[0])-1, heights)
                    
        for c in range(len(heights[0])):
            self.dfs(pacificDP, 0, c, 0, c, heights)
            self.dfs(atlanticDP, len(heights)-1, c, len(heights)-1, c, heights)
        result = []
        for row_idx in range(len(heights)):
            for col_idx in range(len(heights[0])):
                if pacificDP[row_idx][col_idx] and atlanticDP[row_idx][col_idx]:
                    result.append([row_idx, col_idx])
        return result
    
    def dfs(self, matrix, row, col, prevRow, prevCol, heights):
        if not (0 <= row < len(heights) and 0 <= col < len(heights[0])):
            return
        if matrix[row][col]:
            return
        if heights[prevRow][prevCol] > heights[row][col]:
            return
        matrix[row][col] = True
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            self.dfs(matrix, row+dr, col+dc, row, col, heights)

solution = Solution()
input = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# input = [[1]]
result = solution.pacificAtlantic(input)
print(result)