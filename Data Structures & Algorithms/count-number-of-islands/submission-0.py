class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        len_y = len(grid)
        len_x = len(grid[0])

        def ite(x, y):
            print(x, y)
            if x >= len_x or y >= len_y or y < 0 or x < 0 or grid[y][x] == "0":
                print("continued")
                return
            
            grid[y][x] = "0"

            ite(x+1, y)
            ite(x, y+1)
            ite(x-1, y)
            ite(x, y-1)

        for y in range(len_y):
            for x in range(len_x):
                if grid[y][x] == '1':
                    islands += 1
                    ite(x, y)

        return islands