from typing import List


class Solution:
    def checkUpperLeft(self, pointA, pointB):
        return pointA[0] <= pointB[0] and pointA[1] >= pointB[1]
    
    def checkInRec(self, pointA, pointB, pointC):
        return pointA[0] <= pointC[0] and pointC[0] <= pointB[0] and pointA[1] >= pointC[1] and pointC[1] >= pointB[1]
    
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        cnt = 0
        for i in range(n):
            for j in range(0, n):
                check = True
                if (i == j):
                    continue
                if (not self.checkUpperLeft(points[i], points[j])):
                    check = False
                else:
                    for k in range(0, n):
                        if (k == i or k == j):
                            continue
                        elif (self.checkInRec(points[i], points[j], points[k])):
                            check = False
                            break
                if (check):
                    cnt += 1  
        return cnt
    
s = Solution()
points = [[3,1],[1,3],[1,1]]
print(s.numberOfPairs(points))