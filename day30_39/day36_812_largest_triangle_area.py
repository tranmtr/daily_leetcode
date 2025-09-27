import math
from typing import List


# class Solution:
#     def distance(self, point1, point2):
#         return math.sqrt(pow((point1[0] - point2[0]), 2) + pow(point1[1] - point2[1]), 2)
#     def area(self, a, b, c):
#         p = (a + b + c) / 2
#         return math.sqrt(p * (p - a) * (p - b) * (p - c))
#     def check(self, a, b, c):
#         return a + b > c and a + c > b and b + c > a
#     def largestTriangleArea(self, points: List[List[int]]) -> float:
#         n = len(points)
#         result = 0
#         for i in range(0, n - 2):
#             for j in range(i + 1, n - 1):
#                 for k in range(j + 1, n):
#                     a = self.distance(points[i], points[j])
#                     b = self.distance(points[i], points[k])
#                     c = self.distance(points[j], points[k])
#                     if (not self.check(a, b, c)):
#                         continue
#                     result = max(result, self.area(a, b, c))
#         return result

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        result = 0
        n = len(points)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    tmp = 1/2 * abs((points[j][0] - points[i][0]) * (points[k][1] - points[i][1]) - (points[k][0] - points[i][0]) * (points[j][1] - points[i][1]))
                    result = max(result, tmp)
        return result