class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1

        min_so_far = prices[0]
        max_profit = 0

        for price in prices:
            max_profit = max(max_profit, price - min_so_far)
            min_so_far = min(min_so_far, price)

        return max_profit