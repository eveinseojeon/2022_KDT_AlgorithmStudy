class Solution():
    def numIslands(self, grid:list[list[str]]) -> int:
        
        dir_y = (0,0,-1,1)
        dir_x = (-1,1,0,0)
        def dfs(start:list[int],grid:list[list[str]]) -> list[list[str]]:
            y,x = start
            grid[y][x] = '*'
            for i in range(len(dy)):
                dy = y + dir_y[i]
                dx = x + dir_x[i]
                if dy >=0 and dx >= 0 and dy < len(grid) and dx < len(grid[0]):
                    if grid[dy][dx] == '1':
                        dfs([dy,dx],grid)
            return grid
        
        cnt = 0
        for i in range(len(grid)):      
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    cnt = cnt + 1
                    start = [i,j]
                    grid = dfs(start,grid)
        
        
        return cnt
        
grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
my_solution = Solution()
cnt = my_solution.numIslands(grid)                   
print(cnt) 