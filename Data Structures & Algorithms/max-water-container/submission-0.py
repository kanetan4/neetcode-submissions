class Solution:
    def maxArea(self, heights: List[int]) -> int:
        length = len(heights)
        l, r = 0, length - 1
        ans = 0

        while l < r:
            ans = max(ans, (r-l) * min(heights[r],heights[l]))
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
                r -= 1

        return ans