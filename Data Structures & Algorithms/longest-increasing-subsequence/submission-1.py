class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i, num in enumerate(nums):
            highest = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    highest = max(dp[j] + 1, highest)
            dp[i] = highest

        return max(dp)