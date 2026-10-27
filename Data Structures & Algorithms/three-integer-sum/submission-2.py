class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        length = len(nums)
        for i in range(length):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            total = 0 - nums[i]
            l, r = i+1, length-1
            while l < r:
                temp = nums[l] + nums[r]
                if temp == total:
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif temp < total:
                    l += 1
                else:
                    r -= 1
            
        return output