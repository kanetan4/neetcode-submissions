class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output, current = [], []
        length = len(nums)

        def dfs(index):
            output.append(current[:])
            for i in range(index, length):
                if i > index and nums[i] == nums[i-1]:
                    continue
                current.append(nums[i])
                dfs(i+1)
                current.pop()
            return
        
        dfs(0)
        return output