class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = [1] * (length + 2)
        postfix = [1] * (length + 2)
        output = []

        for i in range(0, length):
            prefix[i+1] = prefix[i] * nums[i]

        for i in range(length, 0, -1):
            postfix[i] = postfix[i+1] * nums[i-1]

        for i, num in enumerate(nums):
            output.append(prefix[i] * postfix[i+2])

        return output
