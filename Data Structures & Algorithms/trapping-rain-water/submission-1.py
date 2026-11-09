class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        prefix = [0] * (length + 2)
        postfix = [0] * (length + 2)
        ans = 0

        for i in range(1,length):
            prefix[i] = max(prefix[i-1], height[i-1])
        for i in range(length,0,-1):
            postfix[i] = max(postfix[i+1], height[i-1])

        for i in range(length):
            current = min(prefix[i], postfix[i+2])
            if current > height[i]:
                ans += current - height[i]
        return ans