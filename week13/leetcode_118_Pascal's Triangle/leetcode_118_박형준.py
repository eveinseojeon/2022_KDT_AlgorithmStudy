class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        dp = [[] for i in range(numRows)]
        dp[0] = [1]
        dp[1] = [1, 1]
        for row in range(2, numRows):
            dp[row] = [1] * (row + 1)
            for j in range(1, row):
                dp[row][j] = dp[row - 1][j - 1] + dp[row - 1][j]
        return dp
