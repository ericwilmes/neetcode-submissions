class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def dfs(curr):
            if curr in cache:
                return cache[curr]
            
            if curr > n:
                return 0
            if curr == n:
                return 1

            left = dfs(curr + 1)
            right = dfs(curr + 2)

            res = left + right

            cache[curr] = res
            return res

        return dfs(0)