class Solution:
    def numDecodings(self, s: str) -> int:
        length = len(s)
        dp = [0] * (length + 1)
        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1

        for index in range(2, length + 1):
            if s[index - 1] != "0": 
                dp[index] += dp[index-1]
            if 10 <= (int(s[index - 2]) * 10 + int(s[index - 1])) <= 26:
                dp[index] += dp[index - 2]

        return dp[-1]
