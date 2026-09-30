class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 2: return max(nums)
        
        dp = [0] * length
        dp[0], dp[1] = nums[0], nums[1]

        for i in range(2, length):
            dp[i] = max(dp[i-2], dp[i-1] - nums[i-1]) + nums[i]
        return max(dp[-1],dp[-2])