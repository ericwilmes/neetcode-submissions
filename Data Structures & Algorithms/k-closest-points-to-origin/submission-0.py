class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = []
        x1, y1 = 0, 0
        for point in points:
            x2, y2 = point
            dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

            heapq.heappush(q, (dist, point))

        return [heapq.heappop(q)[1] for _ in range(k)]