from typing import List

# 71/73
# class Solution:
#     def prefixSum(self, mat: List[List[int]]):
#         cntRow = len(mat)
#         cntCol = len(mat[0])
#         arraySum = mat

#         for i in range(cntRow):
#             for j in range(cntCol):
#                 a, b, c = 0, 0, 0
#                 if (i - 1 >= 0):
#                     a = arraySum[i - 1][j]
#                 if (j - 1 >= 0):
#                     b = arraySum[i][j - 1]
#                 if (i - 1 >= 0 and j - 1 >= 0):
#                     c = arraySum[i - 1][j - 1]
#                 arraySum[i][j] += (a + b - c)
#         return arraySum



#     def numSubmat(self, mat: List[List[int]]) -> int:
#         arraySum = self.prefixSum(mat)
#         cntRow = len(mat)
#         cntCol = len(mat[0])
#         cntSubmat = 0
#         for sideHeight in range(1, cntRow + 1):
#             for sideWidth in range(1, cntCol + 1):
#                 oldCntSubmat = cntSubmat
#                 for i in range (cntRow - sideHeight + 1):
#                     for j in range (cntCol - sideWidth + 1):
#                         if (mat[i][j] == 0): 
#                             continue
#                         a, b, c = [0, 0, 0]
#                         if (i - 1 >= 0 and j - 1 >= 0):
#                             c = arraySum[i - 1][j - 1]
#                         if (i - 1 >= 0):
#                             b = arraySum[i - 1][j + sideWidth - 1]
#                         if (j - 1 >= 0):
#                             a = arraySum[i + sideHeight - 1][j - 1]
                        
#                         tmp = arraySum[i + sideHeight - 1][j + sideWidth - 1] - a - b + c
#                         if (tmp == sideHeight * sideWidth):
#                             cntSubmat += 1
#                 if (oldCntSubmat == cntSubmat): 
#                     cntCol = sideWidth
#         return cntSubmat


# pass
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        cntRow = len(mat)
        cntCol = len(mat[0])

        res = 0
        for i in range(cntRow):
            for j in range(cntCol):
                if (j >= 1 and mat[i][j] != 0):
                    mat[i][j] = mat[i][j - 1] + 1

                min_width_rec = mat[i][j]
                for k in range(i, -1, -1):
                    min_width_rec = min(min_width_rec, mat[k][j])
                    if (min_width_rec == 0):
                        break
                    res += min_width_rec
        return res


array = [[1,0,1],[1,1,0],[1,1,0]]

s = Solution()
print(s.numSubmat(array))