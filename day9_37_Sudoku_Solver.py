from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, N = 3, 9
        solve = False
        rows = [[0] * (N + 1) for _ in range(N)]
        cols = [[0] * (N + 1) for _ in range(N)]
        boxes = [[0] * (N + 1) for _ in range(N)]

        def canPutInPlace(num, indexRow, indexCol):
            if (rows[indexRow][num] + cols[indexCol][num] + boxes[(indexRow // 3) * 3 + indexCol // 3][num] == 0):
                return True
            return False

        def putNum(num, indexRow, indexCol):
            rows[indexRow][num] = 1
            cols[indexCol][num] = 1
            boxes[(indexRow // 3) * 3 + indexCol // 3][num] = 1
            board[indexRow][indexCol] = str(num)
        
        def removeNum(num, indexRow, indexCol):
            rows[indexRow][num] = 0
            cols[indexCol][num] = 0
            boxes[(indexRow // 3) * 3 + indexCol // 3][num] = 0
            board[indexRow][indexCol] = "."

        def placeNextNumbers(indexRow, indexCol):
            nonlocal solve
            if indexRow == N - 1 and indexCol == N - 1:
                solve = True
            elif indexCol == N - 1:
                backtracking(indexRow + 1, 0)
            else:
                backtracking(indexRow, indexCol + 1)

        def backtracking(indexRow, indexCol):
            nonlocal solve
            if board[indexRow][indexCol] == '.':
                for i in range(1, 10):
                    if canPutInPlace(i, indexRow, indexCol):
                        putNum(i, indexRow, indexCol)
                        placeNextNumbers(indexRow, indexCol)
                        if not solve:
                            removeNum(i, indexRow, indexCol)
            else:
                placeNextNumbers(indexRow, indexCol)

        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    putNum(int(board[i][j]), i, j)
        backtracking (0, 0)
        
    

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
s = Solution()
s.solveSudoku(board)
