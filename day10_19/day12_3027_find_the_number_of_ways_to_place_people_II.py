from typing import List


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda item: (item[0], -item[1]))
        n = len(points)
        cnt = 0
        for i in range(n - 1):
            maxY2 = -1000000001
            for j in range(i + 1, n):
                if (points[i][1] >= points[j][1] and maxY2 < points[j][1]):
                    cnt += 1
                    maxY2 = points[j][1]
        return cnt

S = Solution()

points = [[6,2],[4,4],[2,6]]

print(S.numberOfPairs(points))