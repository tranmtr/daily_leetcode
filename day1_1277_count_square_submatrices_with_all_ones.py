from typing import List

# ---------------- Solution 1 ----------------
# class Solution:
#     def countSquares(self, matrix: List[List[int]]) -> int:
#         cntRow = len(matrix)
#         cntCol = len(matrix[0])
#         side = 1
#         cntSquare = 0
#         while (True):
#             oldCntSquare = cntSquare
#             for i in range (cntRow - side + 1):
#                 for j in range (cntCol - side + 1):
#                     isOne = True
#                     for k in range(side):
#                         for m in range(side):
#                             if (matrix[i + k][j + m] == 0):
#                                 isOne = False
#                     if (isOne):
#                         cntSquare += 1
#             side += 1
#             if (oldCntSquare == cntSquare):
#                 return cntSquare

# ---------------- Solution 2 ----------------
class Solution:
    def prefixSum(self, matrix: List[List[int]]):
        cntRow = len(matrix)
        cntCol = len(matrix[0])
        arraySum = matrix

        for i in range(cntRow):
            for j in range(cntCol):
                a, b, c = 0, 0, 0
                if (i - 1 >= 0):
                    a = arraySum[i - 1][j]
                if (j - 1 >= 0):
                    b = arraySum[i][j - 1]
                if (i - 1 >= 0 and j - 1 >= 0):
                    c = arraySum[i - 1][j - 1]
                arraySum[i][j] += (a + b - c)
        return arraySum



    def countSquares(self, matrix: List[List[int]]) -> int:
        arraySum = self.prefixSum(matrix)
        cntRow = len(matrix)
        cntCol = len(matrix[0])
        side = 1
        cntSquare = 0
        while (True):
            oldCntSquare = cntSquare
            for i in range (cntRow - side + 1):
                for j in range (cntCol - side + 1):
                    if (matrix[i][j] == 0): 
                        continue
                    a, b, c = [0, 0, 0]
                    if (i - 1 >= 0 and j - 1 >= 0):
                        c = arraySum[i - 1][j - 1]
                    if (i - 1 >= 0):
                        b = arraySum[i - 1][j + side - 1]
                    if (j - 1 >= 0):
                        a = arraySum[i + side - 1][j - 1]
                    
                    tmp = arraySum[i + side - 1][j + side - 1] - a - b + c
                    if (tmp == side * side):
                        cntSquare += 1
            side += 1
            if (oldCntSquare == cntSquare):
                return cntSquare

array = [[0,1,1,1],[1,1,1,1],[0,1,1,1]]

s = Solution()
print(s.countSquares(array))