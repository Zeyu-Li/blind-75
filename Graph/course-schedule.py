class Solution:
    # detect cycles
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         visited = [False for _ in range(numCourses)]
        
#         # sort by first
#         prerequisites.sort(key=lambda x: x[0])
        
        
#         # construct graph first?
        
#         for prerequisite in prerequisites:
#             if visited[prerequisite[1]]:
#                 return False
#             visited[prerequisite[0]] = True
            
#         return True
        adjList = {i:[] for i in range(numCourses)}

        for course, prerequisite in prerequisites:
            adjList[course].append(prerequisite)

        visited = set()

        def dfs(course: int):
            if course in visited: return False
            if adjList[course] == []: return True

            visited.add(course)

            for prerequisite in adjList[course]:
                if not dfs(prerequisite): return False
            visited.remove(course)

            adjList[course] = []

            return True

        for courseNum in range(numCourses):
            if not dfs(courseNum): return False

        return True