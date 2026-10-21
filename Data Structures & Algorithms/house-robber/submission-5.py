class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [0 for _ in range(length+1)]
        dp[1] = nums[0]

        for i in range(1, length):
            dp[i+1] = max(dp[i-1]+nums[i], dp[i])
        return dp[-1]
