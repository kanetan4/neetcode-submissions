from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        height = len(grid)
        width = len(grid[0])
        visited = [[False] * width for _ in range(height)]
        stack = deque()
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 0:
                    stack.append((i, j, 0))

        while len(stack) > 0:
            curr = stack.popleft()
            i, j, step = curr
            if grid[i][j] == -1 or visited[i][j]: 
                continue
            visited[i][j] = True
            grid[i][j] = step

            if i-1 >= 0: stack.append((i-1, j, step+1))
            if j-1 >= 0: stack.append((i, j-1, step+1))
            if i+1 < height: stack.append((i+1, j, step+1))
            if j+1 < width: stack.append((i, j+1, step+1))
        return
