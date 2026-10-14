class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {} # (index, action): maxprofit
        length = len(prices)
        # buying state means that it hasnt bought anything, so it can only buy or wait
        # selling state means that it has bought smth, so it can only sell or wait

        def dfs(i, buying):
            if i >= length:
                return 0
            if (i, buying) in cache:
                return cache[(i, buying)]
            
            wait = dfs(i+1, buying)
            if buying:
                buy = dfs(i+1, not buying) - prices[i]
                cache[(i, buying)] = max(wait, buy)
            else:
                sell = dfs(i+2, not buying) + prices[i]
                cache[(i, buying)] = max(wait, sell)
            return cache[(i, buying)]

        return dfs(0, True)
