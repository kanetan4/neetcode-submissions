class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        output = []
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevheight):
            if (r, c) in visit or r < 0 or c < 0 or r == rows or c == cols or heights[r][c] < prevheight:
                return
            visit.add((r, c))
            newheight = heights[r][c]
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                dfs(r+dx, c+dy, visit, newheight)


        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols-1, atl, heights[r][cols-1])
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows-1, c, atl, heights[rows-1][c])
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    output.append([r, c])
        return output
        