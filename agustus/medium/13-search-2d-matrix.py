# https://leetcode.com/problems/search-a-2d-matrix/
from collections import defaultdict
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cRows,cCols = len(matrix), len(matrix[0])
        if target < matrix[0][0] or target > matrix[cRows-1][cCols-1]:
            return False
        lR,rR= 0, cRows-1
        lC, rC = 0, cCols-1
        while True:
            if lR > rR or lC > rC:
                return False
            mR = (rR + lR) // 2        
            if matrix[mR][0] <= target <= matrix[mR][cCols-1]:
                mC = (lC + rC) // 2
                if target == matrix[mR][mC]:
                    return True
                elif lC == rC:
                    return False
                
                if target < matrix[mR][mC]:
                    if rC == mC:
                        rC -= 1
                    else:
                        rC = mC
                else:
                    if lC == mC:
                        lC +=1
                    else:
                        lC = mC
                    
            else:
                if target > matrix[mR][cCols-1]:
                    if lR == mR:
                        lR+=1
                    else:
                        lR = mR
                elif target < matrix[mR][0]:
                    if rR == mR:
                        mR-=1
                    rR = mR                


solution = Solution()

input = \
    [[1],[3]]
# [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# [0,3,7,2,5,8,4,6,0,1]
# input = [[1]]
input2 = \
2
result = solution.searchMatrix(input, input2)
print(result)

