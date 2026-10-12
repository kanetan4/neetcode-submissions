class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # DFS with sorting and copying
        output = [[]]
        seen = {} # hashmap with tuple as key, True as value
        current = []
        length = len(nums)
        nums.sort()

        def dfs(index):
            current.append(nums[index])
            if tuple(current) not in seen:
                copy = current[:]
                output.append(copy)
                seen[tuple(copy)] = True
                for i in range(index+1, length):
                    dfs(i)
            current.pop()
            return           
        
        for i in range(length):
            dfs(i)
        return output