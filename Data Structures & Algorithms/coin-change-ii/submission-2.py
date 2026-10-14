class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {} # index, amount: no. of solutions
        length = len(coins)

        def dfs(index, total):
            if total > amount:
                return 0 # no solutions for being OOB
            if (index, total) in cache: return cache[(index, total)]
            if total == amount:
                return 1 # exactly 1 solution for being equal
            
            count = 0
            for i in range(index, length):
                subcount = dfs(i, total+coins[i])
                count += subcount
            cache[(index, total)] = count

            return cache[(index, total)]
        
        return dfs(0, 0)