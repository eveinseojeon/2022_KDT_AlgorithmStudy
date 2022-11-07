class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        dp = [[1] * (i + 1) for i in range(rowIndex + 1)]
        for row in range(2, rowIndex + 1):
            for j in range(1, row):
                dp[row][j] = dp[row - 1][j - 1] + dp[row - 1][j]
        return dp[rowIndex]
