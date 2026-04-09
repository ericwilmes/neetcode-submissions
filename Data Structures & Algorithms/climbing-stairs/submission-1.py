class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def dfs(curr):
            print(cache)
            if curr in cache:
                return cache[curr]
            if curr > n:
                cache[curr] = 0
                return 0
            if curr == n:
                cache[curr] = 1
                return 1

            left = dfs(curr + 1)
            right = dfs(curr + 2)

            res = left + right

            cache[curr] = res
            return res

        return dfs(0)