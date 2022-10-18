class Solution:
    def fib(self, n: int) -> int:
        dp = [0] * (n + 3)
        dp[1] = 1
        dp[2] = 1
        for i in range(n):
            dp[i + 2] = dp[i] + dp[i + 1]
        return dp[n]
