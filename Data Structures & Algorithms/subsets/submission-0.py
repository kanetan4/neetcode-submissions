class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        length = len(nums)
        
        def dfs(current, index):
            if index >= length: return
            for i in range(index, length):
                new = current.copy()
                new.append(nums[i])
                output.append(new)
                dfs(new, i+1)
        
        dfs([], 0)
        return output