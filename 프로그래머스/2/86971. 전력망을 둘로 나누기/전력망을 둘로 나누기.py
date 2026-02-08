def solution(n, wires):
    answer = n
    
    
    def dfs(v, graph, visited):
        visited[v] = True
        count = 1
        for i in graph[v]:
            if not visited[i]:
                count += dfs(i, graph, visited)
                
        return count 

    for cut_u, cut_v in wires:
        
        graph =[[] for _ in range(n)]
        visited = [False] * n
        for u, v in wires:
            if (u, v) == (cut_u, cut_v) or (u, v) ==(cut_v, cut_u) :
                continue
            
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)
            
        answer = min(answer, abs(n - 2 *dfs(0, graph, visited)))
        
    return answer