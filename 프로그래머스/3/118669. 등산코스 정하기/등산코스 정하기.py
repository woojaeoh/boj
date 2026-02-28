import heapq
from collections import defaultdict
def solution(n, paths, gates, summits):
    
    #접근 방식 -> 출발점부터 5번까지 가는 경로중에 최소 값을 찾는다.
    #가는 가중치가 5,4 ,3,4 이면 그중 최대가 intensity이고
    #그 경로들의intensity중에 가장 최소치가 되는 값과, 산봉우리를 리턴해라.
    # 다중 진입점 다익스트라 -> 시작점을 모두 큐에 넣는다.
    graph = defaultdict(list)
    visited = [10000001] * (n+1)
    for i, j ,w in paths:
        graph[i].append((j,w))
        graph[j].append((i,w))
        
    summit_set = set(summits)
        
    pq =[]
    
    for gate in gates:
        heapq.heappush(pq, (0, gate))
        visited[gate] = 0
        
    while pq:
        cur_cost, node = heapq.heappop(pq)
        
        if cur_cost > visited[node] or node in summit_set:
            continue
            
        for next_v, cost in graph[node]:
            next_intensity = max(cur_cost, cost)
            if next_intensity < visited[next_v]:
                visited[next_v] =  next_intensity
                heapq.heappush(pq, (next_intensity, next_v))
           
    
    # visited[summits]중에 가장 작은 값과 그떄 summit을 찾는다
    result = [-1, 10000001]
    for summit in sorted(summit_set):
        if visited[summit] < result[1]:
            result[0] = summit
            result[1] = visited[summit]
    
        
    return result
        
                
        