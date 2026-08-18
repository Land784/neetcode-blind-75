from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid),len(grid[0])
        islands = 0

        def dfs(r,c):
            stack = [(r,c)]
            while stack:
                row,col =  stack.pop()
                if not (0 <= row < rows and 0 <= col < cols) or grid[row][col] != "1":
                    continue
                grid[row][col] = "0"
                for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                    stack.append((row+dr,col + dc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r,c)
        return islands

        