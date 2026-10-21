class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        maxproduct, minproduct = 1, 1

        for num in nums:
            if num == 0: 
                maxproduct, minproduct = 1, 1
                continue
            currmax, currmin = maxproduct, minproduct
            maxproduct = max(num * currmax, num * currmin, num)
            minproduct = min(num * currmax, num * currmin, num)
            result = max(maxproduct, result)
        return result

