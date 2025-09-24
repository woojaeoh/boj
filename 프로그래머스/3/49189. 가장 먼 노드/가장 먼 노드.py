from collections import deque

def solution(n, vertex):
    graph = [ [] for _ in range(n+1) ]
    
    for a,b in vertex:
        graph[a].append(b)
        graph[b].append(a)
    
    node1_tofar_list = []
    visited= [False]* (n+1)

    def bfs(count,node):
        q =deque()
        q.append((count,node))

        while q:
            c , cur_node = q.popleft()
            visited[cur_node] = True
            
            for i in graph[cur_node]:
                if not visited[i]:
                    q.append((c+1, i))
                    visited[i] = True
                    node1_tofar_list.append(c)
    bfs(0, 1)
    max_distance = max(node1_tofar_list)
    
    answer = node1_tofar_list.count(max_distance)
    return answer