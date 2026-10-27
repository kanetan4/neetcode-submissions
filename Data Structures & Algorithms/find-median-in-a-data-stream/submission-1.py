import heapq

class MedianFinder:

    def __init__(self):
        self.large = []
        self.small = []

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)
        
        if len(self.large) > len(self.small) + 1:
            top = heapq.heappop(self.large)
            heapq.heappush(self.small, -top)
        elif len(self.small) > len(self.large) + 1:
            top = heapq.heappop(self.small)
            heapq.heappush(self.large, -top)

    def findMedian(self) -> float:
        if len(self.large) == len(self.small):
            return (self.large[0] - self.small[0]) / 2
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return -self.small[0]

        