from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        stack = deque() # tuple of index i, j, minute eg. (2, 2, 0)
        fresh, time = 0, 0
        height, width = len(grid), len(grid[0])
        visited = [[False] * width for _ in range(height)]
        
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1: fresh += 1
                if grid[i][j] == 2: stack.append((i, j, 0))

        while len(stack) > 0:
            i, j, minute = stack.popleft()
            if i < 0 or j < 0 or i >= height or j >= width or visited[i][j] or grid[i][j] == 0:
                continue
            
            visited[i][j] = True
            if grid[i][j] == 1: fresh -= 1
            time = max(minute, time)
            stack.append((i-1, j, minute+1))
            stack.append((i, j-1, minute+1))
            stack.append((i+1, j, minute+1))
            stack.append((i, j+1, minute+1))
        
        return time if fresh == 0 else -1