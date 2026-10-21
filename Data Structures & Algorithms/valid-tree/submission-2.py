class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # fully connected and have no cycles
        adj = {x:set() for x in range(n)}
        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)
        visited = set()

        def dfs(i):
            if i in visited:
                return False
            visited.add(i)
            for j in adj[i]:
                adj[j].remove(i)
                if not dfs(j):
                    return False
            return True
        
        return dfs(0) and len(visited) == n