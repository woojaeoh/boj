from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = [] #결과 반환용

        indegree =[0] * (numCourses)
        graph = [[] for _ in range(numCourses)]
        visited =[]

        for i, j in prerequisites:
            indegree[i] += 1
            graph[j].append(i)

        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            cur_v = q.popleft()
            result.append(cur_v)

            for node in graph[cur_v]:
                indegree[node] -= 1
                
                if indegree[node] == 0 :
                    q.append(node)

        print(result)

        return result if len(result) == numCourses else []


        



        