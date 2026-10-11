class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = []
        adjacencyList = { x:[] for x in range(numCourses)}
        for course, prereq in prerequisites:
            adjacencyList[course].append(prereq)
        print(adjacencyList)

        def dfs(num):
            if num in visited: 
                return False
            if adjacencyList[num] == []:
                return True
            
            visited.append(num)

            for prereq in adjacencyList[num]:
                if not dfs(prereq):
                    return False
            visited.remove(num)
            adjacencyList[num] = []
            return True

        for i in range(numCourses):
            if not dfs(i): return False
        return True

