from collections import defaultdict
import heapq

def solution(n, s, a, b, fares):
    
    graph = defaultdict(list)
    for u,v,w in fares:
        graph[u].append((v, w))
        graph[v].append((u, w))
        
    def dijkstra(start, end):
        
        costs= [float('inf')]*(n+1)
        pq = []
        heapq.heappush(pq, (0, start))
        costs[start] = 0 
        
        while pq:
            cur_cost, node = heapq.heappop(pq)    
            
            if cur_cost > costs[node] :
                continue
            
            for next_node, weight in graph[node]:
                
                next_cost = weight + cur_cost
                if next_cost < costs[next_node]:
                    
                    costs[next_node] = next_cost
                    heapq.heappush(pq, (next_cost, next_node))
                    
        return costs
    
    result = float('inf')
    
    for i in range(1, n+1):
        go_i = dijkstra(s, i)
        go_a = dijkstra(i, a)
        go_b = dijkstra(i, b)
        
        result = min(result, go_i[i] + go_a[a] + go_b[b])
        
    return result
        
    
 
