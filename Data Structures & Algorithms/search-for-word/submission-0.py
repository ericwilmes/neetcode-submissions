class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        y_len = len(board)
        x_len = len(board[0])
        visited = [[False] * x_len for _ in range(y_len)]

        def dfs(i, x, y):
            if x < 0 or x >= x_len or y < 0 or y >= y_len:
                return False
            if visited[y][x] or board[y][x] != word[i]:
                return False
            
            if i == len(word) - 1:
                return True
            
            visited[y][x] = True
            
            found = (
                dfs(i+1, x+1, y) or
                dfs(i+1, x-1, y) or
                dfs(i+1, x, y+1) or
                dfs(i+1, x, y-1)
            )
            
            visited[y][x] = False
            return found

        for y in range(y_len):
            for x in range(x_len):
                if dfs(0, x, y):
                    return True

        return False