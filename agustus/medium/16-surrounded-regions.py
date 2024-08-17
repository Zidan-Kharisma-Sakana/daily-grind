# https://leetcode.com/problems/surrounded-regions/
from collections import defaultdict
from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # for x in board:
        #     print(x)
        # print("-"*50)
        maxRow, maxCol = len(board), len(board[0])
        def dfs(row, col, mark):
            if board[row][col] != "O":
                return
            board[row][col] = str(mark)
            dirs = [(1,0), (0, 1), (-1,0), (0, -1)]
            for x,y in dirs:
                if 0 <= row+y < maxRow and 0 <= col+x < maxCol:
                    dfs(row+y, col+x, mark)
                    
        numOfIslands = 0
        for rowIdx in range(len(board)):
            for colIdx in range(len(board[0])):
                if board[rowIdx][colIdx] == "O":
                    numOfIslands+=1
                    dfs(rowIdx, colIdx, numOfIslands) # will find connected regions, and mark it with digit
        notSurrounded = set()
        for colIdx in range(maxCol):
            if board[0][colIdx].isdigit():
                notSurrounded.add(board[0][colIdx])
            if board[maxRow-1][colIdx].isdigit():
                notSurrounded.add(board[maxRow-1][colIdx])
        for rowIdx in range(maxRow):
            if board[rowIdx][0].isdigit():
                notSurrounded.add(board[rowIdx][0])
            if board[rowIdx][maxCol-1].isdigit():
                notSurrounded.add(board[rowIdx][maxCol-1])
                
        for rowIdx in range(len(board)):
            for colIdx in range(len(board[0])):
                if board[rowIdx][colIdx].isdigit():
                    if board[rowIdx][colIdx] in notSurrounded:
                        board[rowIdx][colIdx] = "O"
                    else:
                        board[rowIdx][colIdx] = "X"
        
        # for x in board:
        #     print(x)
        
    
solution = Solution()

input = \
[["X","X","X","X"],
 ["X","O","O","X"],
 ["X","X","O","X"],
 ["X","O","O","X"]]

# [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# [0,3,7,2,5,8,4,6,0,1]
# input = [[1]]
input2 = \
"SEE"
result = solution.solve(input)
print(result)

