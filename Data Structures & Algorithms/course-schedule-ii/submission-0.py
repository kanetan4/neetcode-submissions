class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {x:[] for x in range(numCourses)} # course: List[prerequisites]
        for prereq in prerequisites:
            adj[prereq[0]].append(prereq[1])
        
        visit, cycle = set(), set()
        output = []

        def dfs(i):
            if i in cycle:
                return False
            if i in visit:
                return True
            cycle.add(i)
            for prereqs in adj[i]:
                if not dfs(prereqs):
                    return False
            cycle.remove(i)
            visit.add(i)
            output.append(i)
            return True

        for i in range(numCourses):
            if not dfs(i): return []
        return output