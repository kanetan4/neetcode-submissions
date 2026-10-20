import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.length = len(nums)
        self.h = nums
        heapq.heapify(self.h)
        while self.length > self.k:
            heapq.heappop(self.h)
            self.length -= 1

    def add(self, val: int) -> int:
        heapq.heappush(self.h, val)
        if len(self.h) > self.k:
            heapq.heappop(self.h)
        return self.h[0]
