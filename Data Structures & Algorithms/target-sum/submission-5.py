from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        length = len(nums)
        dp = [defaultdict(int) for i in range(length+1)]
        dp[0][0] = 1 # (0 items, sum to 0): 1 way

        for i in range(length):
            for currsum, ways in dp[i].items():
                dp[i+1][currsum-nums[i]] += ways
                dp[i+1][currsum+nums[i]] += ways
        return dp[-1][target]
        
        # cache = defaultdict(int) # key: value = (index, sum): ways
        # length = len(nums)

        # def dfs(i, total):
        #     if i == length:
        #         if total == target: return 1
        #         else: return 0
        #     if (i, total) in cache: 
        #         return cache[(i, total)]
            
        #     cache[(i, total)] = dfs(i+1, total+nums[i]) + dfs(i+1, total-nums[i])
        #     return cache[(i, total)]

        # return dfs(0, 0)

