class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort()
        summary = sum(nums)
        if summary % 2 != 0: return False # if total is odd cannot return
        half = summary / 2

        # build decision tree to try to find half, cache results
        cache = {} # use set of the number as keys, if exist means false
        def dfs(start, total):
            if total == half: return True
            if total > half or start == len(nums): return False
            
            result = dfs(start + 1, total + nums[start]) or dfs(start + 1, total)
            cache[(start, total)] = result
            return result
            

        return dfs(0, 0)
