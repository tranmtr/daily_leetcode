from typing import List


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
    
grid = [[0,1,0],[1,0,1]]
s = Solution()
print(s.minimumArea(grid))