class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        output = []
        length = len(candidates)

        def dfs(index, current, total):
            if total == target:
                output.append(current)
                return
            for i in range(index, length):
                if i > index and candidates[i] == candidates[i - 1]: 
                    continue    
                if total + candidates[i] > target:
                    break
                copy = current.copy()
                copy.append(candidates[i])
                dfs(i+1, copy, total+candidates[i])

        dfs(0, [], 0)
        return output