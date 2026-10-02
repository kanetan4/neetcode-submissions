class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        height = len(grid)
        width = len(grid[0])
        seen = [[False] * width for _ in range(height)]
        count = 0

        def dfs(i, j): # this takes in index of the current grid
            if i >= height or i < 0 or j < 0 or j >= width or grid[i][j] == "0" or seen[i][j]:
                return
            seen[i][j] = True # marks this as seen
            
            dfs(i-1, j)
            dfs(i, j-1)
            dfs(i+1, j)
            dfs(i, j+1)
            return

        for i in range(height):
            for j in range(width):
                if grid[i][j] == "1" and not seen[i][j]:
                    dfs(i, j)
                    count += 1
                    print(i,j,count)
        return count
