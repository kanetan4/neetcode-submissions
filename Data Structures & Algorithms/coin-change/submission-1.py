class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        length = len(coins)
        dp = [-1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            minstep = 99999999999
            for coin in coins:
                if coin <= i:
                    if dp[i-coin] != -1:
                        minstep = min(minstep, dp[i-coin] + 1)
                else: break
            if minstep != 99999999999: dp[i] = minstep
        return dp[-1]