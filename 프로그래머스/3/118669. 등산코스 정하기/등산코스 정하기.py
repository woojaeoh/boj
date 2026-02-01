import heapq
from collections import defaultdict
def solution(n, paths, gates, summits):
    
    graph = defaultdict(list)
    for i ,j ,w in paths:
        graph[i].append((w, j))
        graph[j].append((w, i))
    
    costs = [float('inf')] * (50001)
    heap = []
    
    for gate in gates:
        heapq.heappush(heap, (0, gate))
        costs[gate] = 0
        
    set_summit = set(summits)
        
    while heap:
        weight, node = heapq.heappop(heap) #가중치 , 노드
        
        # 기존에 방문한 경로보다 가중치가 작은 경우 -> 중단(갈 필요 X)
        if costs[node] < weight  or node in set_summit: # 이미 산봉우리에 도착한 경우 -> 중단
            continue
            
        for next_weight, next_node in graph[node]:
            new_intensity = max(weight, next_weight)
            if new_intensity < costs[next_node] :
                heapq.heappush( heap, (new_intensity , next_node))
                costs[next_node] = new_intensity
    
    result = [0, 100000001]
    for summit in sorted(summits):
        if costs[summit] < result[1]:
            result = [summit, costs[summit]]
            
    
    return result
        
                
        