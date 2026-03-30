class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        output = r
        while l <= r:
            m = (l + r) // 2

            hours = self.total_hours(piles, m)
            if hours <= h:
                output = m
                r = m-1
            else:
                l = m+1
        return output

    
    def total_hours(self, piles, val):
        return sum(math.ceil(v / val) for v in piles)