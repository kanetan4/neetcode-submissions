class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        output = []
        length = len(nums)

        def dfs(index, current, total):
            if total == target:
                output.append(current)
                return
            for i in range(index, length):
                if total + nums[i] > target:
                    break
                copy = current.copy()
                copy.append(nums[i])
                dfs(i, copy, total+nums[i])

        dfs(0, [], 0)
        return output