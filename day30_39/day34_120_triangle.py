from typing import List


# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         m = len(triangle)
#         dp = []
#         for i in range(0, m):
#             dp.append([])
#             for j in range(len(triangle[i])):
#                 dp[i].append(0)
#         dp[0][0] = triangle[0][0] 

#         for i in range(1, m):
#             for j in range(len(triangle[i])):
#                 if j == 0:
#                     dp[i][j] = dp[i - 1][j] + triangle[i][j]
#                 elif j == len(triangle[i]) - 1:
#                     dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
#                 else:
#                     dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
#         return min(dp[-1])


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1].copy()
        m = len(triangle)
        for i in range(m - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
        return dp[0]

S = Solution()
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(S.minimumTotal(triangle))