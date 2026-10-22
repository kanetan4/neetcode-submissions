from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = defaultdict(int) # key: value = (index, sum): ways
        length = len(nums)

        def dfs(i, total):
            if i == length:
                if total == target: return 1
                else: return 0
            if (i, total) in cache: 
                return cache[(i, total)]
            
            cache[(i, total)] = dfs(i+1, total+nums[i]) + dfs(i+1, total-nums[i])
            return cache[(i, total)]

        return dfs(0, 0)

