from typing import List

MAX_CONST = 1000

class Solution:
    def position(self, grid, startRow, startCol, endRow, endCol, step, isSwap):
        if (not isSwap):
            for i in range(startRow, endRow, step):
                for j in range(startCol, endCol, step):
                    if (grid[i][j] == 1):
                        return (i, j)
        else:
            for j in range(startCol, endCol, step):
                for i in range(startRow, endRow, step):
                    if (grid[i][j] == 1):
                        return (i, j)
    def minimumArea(self, grid: List[List[int]]) -> int:
        cntRow = len(grid)
        cntCol = len(grid[0])
        top = self.position(grid, 0, 0, cntRow, cntCol, 1, False)[0]
        bottom = self.position(grid, cntRow - 1, cntCol - 1, -1, -1, -1, False)[0]
        left = self.position(grid, 0, 0, cntRow, cntCol, 1, True)[1]
        right = self.position(grid, cntRow - 1, cntCol - 1, -1, -1, -1, True)[1]

        res = (bottom - top + 1) * (right - left + 1)
        return res
    
    def checkHasOne(self, grid):
        cntRow = len(grid)
        cntCol = len(grid[0])
        for i in range(cntRow):
            for j in range(cntCol):
                if (grid[i][j]): 
                    return True
        return False

    def minimumTotalTwoRec(self, matrix, isRow):
        cntRow = len(matrix)
        cntCol = len(matrix[0])
        minTotal = MAX_CONST

        # divide by row
        if (isRow):
            for i in range(0, cntRow - 1):
                subMatrixAbove = matrix[: i + 1]
                subMatrixBelow = matrix[i + 1 :]

                if (self.checkHasOne(subMatrixAbove) and self.checkHasOne(subMatrixBelow)):
                    areaAbove = self.minimumArea(subMatrixAbove)
                    areaBelow = self.minimumArea(subMatrixBelow)

                    if (areaAbove + areaBelow < minTotal):
                        minTotal = areaAbove + areaBelow
        # divide by col
        else:
            for j in range(0, cntCol - 1):
                subMatrixLeft = [row[: j + 1] for row in matrix]
                subMatrixRight = [row[j + 1 :] for row in matrix]

                if (self.checkHasOne(subMatrixLeft) and self.checkHasOne(subMatrixRight)):
                    areaLeft = self.minimumArea(subMatrixLeft)
                    areaRight = self.minimumArea(subMatrixRight)

                    if (areaLeft + areaRight < minTotal):
                        minTotal = areaLeft + areaRight
        
        return minTotal

    def minimumSum(self, grid: List[List[int]]) -> int:
        cntRow = len(grid)
        cntCol = len(grid[0])

        minTotal = MAX_CONST

        # fixed rectangle above and divide the remainder by row
        for i in range(0, cntRow - 2):
            if (self.checkHasOne(grid[: i + 1])):
                areaAbove = self.minimumArea(grid[: i + 1])
                areaBelow = self.minimumTotalTwoRec(grid[i + 1 :], True)
                
                if (areaAbove + areaBelow < minTotal):
                    minTotal = areaAbove + areaBelow

        # fixed rectangle above and divide the remainder by col
        for i in range(0, cntRow - 1):
            if (self.checkHasOne(grid[: i + 1])):
                areaAbove = self.minimumArea(grid[: i + 1])
                areaBelow = self.minimumTotalTwoRec(grid[i + 1 :], False)
                
                if (areaAbove + areaBelow < minTotal):
                    minTotal = areaAbove + areaBelow
        
        # fixed rectangle below and divide the remainder by row
        for i in range(1, cntRow - 1):
            if (self.checkHasOne(grid[i + 1 :])):
                areaAbove = self.minimumTotalTwoRec(grid[: i + 1], True)
                areaBelow = self.minimumArea(grid[i + 1 :])

                if (areaAbove + areaBelow < minTotal):
                    minTotal = areaAbove + areaBelow
        
        # fixed rectangle below and divide the remainder by col
        for i in range(0, cntRow - 1):
            if (self.checkHasOne(grid[i + 1 :])):
                areaAbove = self.minimumTotalTwoRec(grid[: i + 1], False)
                areaBelow = self.minimumArea(grid[i + 1 :])

                if (areaAbove + areaBelow < minTotal):
                    minTotal = areaAbove + areaBelow

        # fixed rectangle left and divide the remainder by row
        for j in range(0, cntCol - 1):
            subMatrixLeft = [row[: j + 1] for row in grid]
            subMatrixRight = [row[j + 1 :] for row in grid]
            if (self.checkHasOne(subMatrixLeft)):
                areaLeft = self.minimumArea(subMatrixLeft)
                areaRight = self.minimumTotalTwoRec(subMatrixRight, True)

                if (areaLeft + areaRight < minTotal):
                    minTotal = areaLeft + areaRight

        # fixed rectangle left and divide the remainder by col
        for j in range(0, cntCol - 2):
            subMatrixLeft = [row[: j + 1] for row in grid]
            subMatrixRight = [row[j + 1 :] for row in grid]
            if (self.checkHasOne(subMatrixLeft)):
                areaLeft = self.minimumArea(subMatrixLeft)
                areaRight = self.minimumTotalTwoRec(subMatrixRight, False)

                if (areaLeft + areaRight < minTotal):
                    minTotal = areaLeft + areaRight
        
        # fixed rectangle right and divide the remainder by row
        for j in range(0, cntCol - 1):
            subMatrixLeft = [row[: j + 1] for row in grid]
            subMatrixRight = [row[j + 1 :] for row in grid]
            if (self.checkHasOne(subMatrixRight)):
                areaLeft = self.minimumTotalTwoRec(subMatrixLeft, True)
                areaRight = self.minimumArea(subMatrixRight)

                if (areaLeft + areaRight < minTotal):
                    minTotal = areaLeft + areaRight

        # fixed rectangle right and divide the remainder by col
        for j in range(1, cntCol - 1):
            subMatrixLeft = [row[: j + 1] for row in grid]
            subMatrixRight = [row[j + 1 :] for row in grid]
            if (self.checkHasOne(subMatrixRight)):
                areaLeft = self.minimumTotalTwoRec(subMatrixLeft, False)
                areaRight = self.minimumArea(subMatrixRight)

                if (areaLeft + areaRight < minTotal):
                    minTotal = areaLeft + areaRight

        return minTotal
s = Solution()
grid = [[0,0,0],[0,0,0],[0,0,1],[1,1,0]]
print(s.minimumSum(grid))