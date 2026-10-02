class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        count = 0
        height = len(grid)
        width = len(grid[0])
		
        def dfs(i, j):
            if i < 0 or j < 0 or i >= height or j >= width or grid[i][j] == 0:
                return 0
            counter = 1
            grid[i][j] = 0
            counter += dfs(i-1, j)
            counter += dfs(i, j-1)
            counter += dfs(i+1, j)
            counter += dfs(i, j+1)
            return counter
		
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    curr = dfs(i, j)
                    count = max(curr, count)
                    print(count)
        return count
