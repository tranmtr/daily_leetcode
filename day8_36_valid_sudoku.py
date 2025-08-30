from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = 9
        n = 9

        for i in range(m):
            arr = [False, False, False, False, False, False, False, False, False, False]
            for j in range(n):
                if (board[i][j] != "."):
                    index = int(board[i][j])
                    if (not arr[index]):
                        arr[index] = True
                    else:
                        return False
        
        for j in range(n):
            arr = [False, False, False, False, False, False, False, False, False, False]
            for i in range(m):
                if (board[i][j] != "."):
                    index = int(board[i][j])
                    if (not arr[index]):
                        arr[index] = True
                    else:
                        return False
                
        for i in range(0, m, 3):
            for j in range(0, n, 3):
                arr = [False, False, False, False, False, False, False, False, False, False]
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        if (board[k][l] != "."):
                            index = int(board[k][l])
                            if (not arr[index]):
                                arr[index] = True
                            else:
                                return False
        
        return True


















board = [
    ["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]

s = Solution()
print(s.isValidSudoku(board))