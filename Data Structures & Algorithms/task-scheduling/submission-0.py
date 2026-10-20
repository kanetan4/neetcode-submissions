import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        ready = [-value for value in count.values()]
        heapq.heapify(ready)
        waiting = deque()
        time = 0

        while ready or waiting:
            time += 1

            if ready:
                top = heapq.heappop(ready)
                top += 1
                if top < 0:
                    waiting.append((top, time+n))
            
            if waiting and waiting[0][1] == time:
                push = waiting.popleft()
                heapq.heappush(ready, push[0])
                

        return time