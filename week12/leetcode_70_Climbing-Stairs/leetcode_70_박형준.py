class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 3)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3
        for i in range(1, n):
            dp[i + 2] = dp[i] + dp[i + 1]
        return dp[n]
