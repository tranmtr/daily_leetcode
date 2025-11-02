from typing import List


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        arr = [[0 for j in range(n)] for i in range(m)]
        
        for x, y in walls:
            arr[x][y] = -1
        for x, y in guards:
            arr[x][y] = 2

        for i in range(m):
            seen = False
            for j in range(n):
                if (arr[i][j] == 2):
                    seen = True
                elif (arr[i][j] == -1):
                    seen = False
                elif (seen):
                    if (arr[i][j] == 0):
                        arr[i][j] = 1
            
            seen = False
            for j in range(n - 1, -1, -1):
                if (arr[i][j] == 2):
                    seen = True
                elif (arr[i][j] == -1):
                    seen = False
                elif (seen):
                    if (arr[i][j] == 0):
                        arr[i][j] = 1

        for j in range(n - 1, -1 ,-1):
            seen = False
            for i in range(m):
                if (arr[i][j] == 2):
                    seen = True
                elif (arr[i][j] == -1):
                    seen = False
                elif (seen):
                    if (arr[i][j] == 0):
                        arr[i][j] = 1
            
            seen = False
            for i in range(m - 1, -1, -1):
                if (arr[i][j] == 2):
                    seen = True
                elif (arr[i][j] == -1):
                    seen = False
                elif (seen):
                    if (arr[i][j] == 0):
                        arr[i][j] = 1
        return sum(arr[i][j] == 0 for i in range(m) for j in range(n))