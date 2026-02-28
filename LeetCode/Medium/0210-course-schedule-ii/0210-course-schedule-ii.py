from collections import deque, defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indegree =[0] * numCourses
        graph = defaultdict(list)
        visited = [False] * numCourses
        result = []

        for u,v in prerequisites:
            indegree[u] += 1
            graph[u].append(v)
            graph[v].append(u)

        q = deque()
        
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                visited[i] = True

        while q:
            node = q.popleft()
            result.append(node)
            for v in graph[node]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
                    visited[v] = True

        
        return result if len(result) == numCourses else []