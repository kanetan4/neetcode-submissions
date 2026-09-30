class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 3: return max(nums)

        dp1, dp2 = [0] * (length - 1), [0] * (length - 1)
        dp1[0], dp1[1] = nums[0], nums[1]
        dp2[0], dp2[1] = nums[1], nums[2]

        for i in range(2, length - 1):
            dp1[i] = max(dp1[i-2], dp1[i-1] - nums[i-1]) + nums[i]
        for j in range(3, length):
            dp2[j-1] = max(dp2[j-3], dp2[j-2] - nums[j-1]) + nums[j]
        return max(dp1[-1], dp1[-2], dp2[-1], dp2[-2])