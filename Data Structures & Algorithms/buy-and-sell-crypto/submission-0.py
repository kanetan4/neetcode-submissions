class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        l, r = 0, 1
        best = 0
        while r < length:
            current = prices[r] - prices[l]
            if current <= 0:
                l = r
            else:
                best = max(best, current)
            r += 1
        return best