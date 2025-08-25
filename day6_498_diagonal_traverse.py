from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        upward = True 
        res = [mat[0][0]]
        i = 0
        j = 0
        mul = m * n
        for _ in range(mul):
            if (i == m - 1 and j == n - 1):
                return res
            if (i == m - 1 and not upward):
                res.append(mat[i][j + 1])
                j += 1
                upward = not upward
            elif (j == n - 1 and upward):
                res.append(mat[i + 1][j])
                i += 1
                upward = not upward
            elif (i == 0 and upward):
                res.append(mat[i][j + 1])
                j += 1
                upward = not upward
            elif (j == 0 and not upward):
                res.append(mat[i + 1][j])
                i += 1
                upward = not upward
            elif (upward):
                res.append(mat[i - 1][j + 1])
                i -= 1
                j += 1
            elif (not upward):
                res.append(mat[i + 1][j - 1])
                i += 1
                j -= 1
        return res
    
s = Solution()
mat = [[1,2,3],[4,5,6],[7,8,9]]
print(s.findDiagonalOrder(mat))
        