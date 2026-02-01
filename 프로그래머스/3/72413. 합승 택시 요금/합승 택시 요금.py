from collections import defaultdict
import heapq

def solution(n, s, a, b, fares):
 
    graph = defaultdict(list)
    for i, j ,w in fares:
        graph[i].append((j, w))
        graph[j].append((i, w))
        
    def dijkstra(start):
        
        costs = [float('inf')] * (n+1)
        pq = []
           
        heapq.heappush(pq, (0, start))
        costs[start] = 0
        
        while pq:
            cur_cost, node = heapq.heappop(pq)      
            
            if cur_cost > costs[node]:
                continue
                
            for next_node , cost in graph[node]:
                next_cost = cur_cost + cost
                
                if next_cost < costs[next_node]:
                    costs[next_node] = next_cost
                    heapq.heappush(pq, (next_cost , next_node))
        
        
        return costs  
    
  
    #final + 다익스트라_alone 2번각각 중에 최소
    result = float('inf')
    dist_from_s = dijkstra(s)               
    dist_from_a = dijkstra(a)
    dist_from_b = dijkstra(b)
    
    for i in range(1, n+1):
        result = min(result, dist_from_s[i] + dist_from_a[i] + dist_from_b[i])                
        
    return result
