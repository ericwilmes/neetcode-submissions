class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        biggest = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            if r >= rows or r < 0 or c >= cols or c < 0 or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            return dfs(r+1, c) + dfs(r, c+1) + dfs(r-1, c) + dfs(r, c-1) + 1

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != 1:
                    continue
                biggest = max(biggest, dfs(row, col))

        return biggest