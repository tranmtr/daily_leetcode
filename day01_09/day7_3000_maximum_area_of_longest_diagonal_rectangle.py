from typing import List


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxDiagonalSquare = 0
        maxArea = 0
        n = len(dimensions)

        for i in range(n):
            tmpDiagonalSquare = dimensions[i][0] ** 2 + dimensions[i][1] ** 2
            if (tmpDiagonalSquare > maxDiagonalSquare):
                maxDiagonalSquare = tmpDiagonalSquare
                maxArea = dimensions[i][0] * dimensions[i][1]
            elif (tmpDiagonalSquare == maxDiagonalSquare and maxArea < dimensions[i][0] * dimensions[i][1]):
                maxDiagonalSquare = tmpDiagonalSquare
                maxArea = dimensions[i][0] * dimensions[i][1]
        
        return maxArea
        
dimensions = [[9,3],[8,6]]
s = Solution()
print(s.areaOfMaxDiagonal(dimensions))