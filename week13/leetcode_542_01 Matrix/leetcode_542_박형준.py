# 구글링
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m = len(mat)
        n = len(mat[0])  # it's promised there will be at least one zero

        # scan from left-top
        for i, row in enumerate(mat):
            for j, ele in enumerate(row):
                if ele:
                    top = mat[i - 1][j] + 1 if i > 0 else float('inf')
                    left = mat[i][j - 1] + 1 if j > 0 else float('inf')
                    mat[i][j] = min(top, left)

        # scan from right-bottom
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                ele = mat[i][j]
                if ele:
                    bottom = mat[i + 1][j] + 1 if i < m - 1 else float('inf')
                    right = mat[i][j + 1] + 1 if j < n - 1 else float('inf')
                    mat[i][j] = min(ele, bottom, right)

        return mat
