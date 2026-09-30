from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sorted_count = sorted(count.items(), key = lambda item:item[1], reverse=True)
        return [sorted_count[x][0] for x in range(k)]