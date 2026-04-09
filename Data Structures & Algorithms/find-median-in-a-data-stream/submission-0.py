class MedianFinder:

    def __init__(self):
        self.lows = []
        self.his = []

    def addNum(self, num: int) -> None:
        if len(self.lows) == len(self.his):
            heapq.heappush_max(self.lows, heapq.heappushpop(self.his, num))
        else:
            heapq.heappush(self.his, heapq.heappushpop_max(self.lows, num))

    def findMedian(self) -> float:
        if len(self.lows) == len(self.his):
            return (self.lows[0] + self.his[0]) / 2
        return self.lows[0]
        