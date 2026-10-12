class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        visited = {num:0 for num in nums}
        output = []
        
        def dfs(num, current):
            current.append(num)
            visited[num] += 1

            if len(current) == length:
                output.append(current[:])
            else: 
                for i in nums:
                    if visited[i] == 0:
                        dfs(i, current)
            current.pop()
            visited[num] -= 1

        for num in nums:
            dfs(num, [])
        return output