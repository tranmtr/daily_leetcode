from typing import List


class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [0 for _ in range(n)]
        if n == 1:
            dp[0] = costs[0] + 1
            return dp[0]
        elif n == 2:
            dp[0] = costs[0] + 1
            dp[1] = min(0 + 2 * 2, dp[0] + 1 * 1) + costs[1]
            return dp[1]
        else:
            dp[0] = costs[0] + 1
            dp[1] = min(0 + 2 * 2, dp[0] + 1 * 1) + costs[1]
            dp[2] = min(0 + 3 * 3, dp[0] + 2 * 2, dp[1] + 1 * 1) + costs[2]
            for i in range(3, n):
                dp[i] = min(dp[i - 3] + 9, dp[i - 2] + 4, dp[i - 1] + 1) + costs[i]
            return dp[-1]
