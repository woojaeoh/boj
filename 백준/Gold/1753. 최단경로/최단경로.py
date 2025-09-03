import sys, heapq
from collections import defaultdict

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

graph = defaultdict(list)
for _ in range(E):
    u, v , w = map(int,input().split())
    graph[u].append((w, v))
    
INF = 10**18

def dijkstra (start):
    
    dist =[INF]*(V+1)
    dist[start] = 0
    pq =[]
    heapq.heappush(pq,(0, start))
    
    while pq:
        cur_cost , cur_v = heapq.heappop(pq)
        for cost , next_v in graph[cur_v]:
            next_cost = cur_cost + cost
            if next_cost < dist[next_v]:
                dist[next_v] = next_cost
                heapq.heappush(pq, (next_cost, next_v))
    return dist
    
dist = dijkstra(K)

for i in range(1, V+1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])
