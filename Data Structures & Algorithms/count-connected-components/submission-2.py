class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {x:set() for x in range(n)}
        visited, count = set(), 0
        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)
        
        def dfs(i):
            visited.add(i)
            for j in adj[i]:
                if j not in visited:
                    adj[j].remove(i)
                    dfs(j)
            return

        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        return count