class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        one, two = cost[-2:]
        for i in range(n-3, -1, -1):
            c = cost[i]
            temp = one
            one = min(c + one, c + two)
            two = temp

        return min(one, two)