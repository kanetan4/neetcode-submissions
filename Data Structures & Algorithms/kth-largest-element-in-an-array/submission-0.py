import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = [-num for num in nums]
        heapq.heapify(h)
        for i in range(k): 
            top = heapq.heappop(h)
        return -top