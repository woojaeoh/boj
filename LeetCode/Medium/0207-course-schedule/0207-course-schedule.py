from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree =[0] * (numCourses)
        graph = [[] for _ in range(numCourses)]
        visited = []

        for u, v in prerequisites:
            indegree[u] += 1
            graph[v].append(u)

        q = deque()
        
        for v in range(numCourses):
            if indegree[v] == 0:
                q.append(v)

        while q:
            cur_v = q.popleft()
            visited.append(cur_v)

            for next_v in graph[cur_v]:
                indegree[next_v] -= 1

                if indegree[next_v] == 0:
                    q.append(next_v)

        for i in range(numCourses):
            if indegree[i] != 0:
                return False

        return True