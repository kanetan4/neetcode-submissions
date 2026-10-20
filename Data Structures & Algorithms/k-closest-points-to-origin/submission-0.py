import math, heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = [(math.sqrt(x[0] ** 2 + x[1] ** 2), x[0], x[1]) for x in points]
        heapq.heapify(distance)
        answer = []
        for i in range(k):
            smallest = heapq.heappop(distance)
            answer.append([smallest[1], smallest[2]])
        return answer