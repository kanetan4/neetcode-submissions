class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {} # (index, sum): no. of ways to hit target
        length = len(nums)

        def dfs(index, current):
            if (index, current) in cache:
                return cache[(index, current)]
            elif index == length:
                if current != target:
                    return 0
                else:
                    return 1
            
            add = dfs(index+1, current+nums[index])
            remove = dfs(index+1, current-nums[index])
            cache[(index, current)] = add + remove
            return cache[(index, current)]

        return dfs(0, 0)