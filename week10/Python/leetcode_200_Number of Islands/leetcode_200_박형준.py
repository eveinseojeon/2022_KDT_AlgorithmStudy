class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[0] * n for _ in range(m)]

        def dfs(x, y):
            if visited[x][y]:
                return
            visited[x][y] = 1
            dx = [1, -1, 0, 0]
            dy = [0, 0, 1, -1]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if (0 <= nx < m) and (0 <= ny < n):
                    if (grid[nx][ny] == "1") and (visited[nx][ny] == 0):
                        dfs(nx, ny)
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and visited[i][j] == 0:
                    cnt += 1
                    dfs(i, j)

        return cnt
