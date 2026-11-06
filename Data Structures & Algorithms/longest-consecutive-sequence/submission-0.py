from collections import Counter

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = Counter(nums)
        if len(nums) == 0: return 0
        largest = 1
        for num in nums:
            if (num - 1) in count: continue
            cur, curcount = num, 1
            while cur + 1 in count:
                cur += 1
                curcount += 1
            largest = max(largest, curcount)

        return largest