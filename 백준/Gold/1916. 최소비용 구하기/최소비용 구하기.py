import sys, heapq
from collections import defaultdict 

input = sys.stdin.readline

N = int(input())
M = int(input())

graph= [[]for _ in range(N+1)]

for _ in range(M):
    u, v, w = map(int,input().split())
    graph[u].append((w,v))
    
s, e  = map(int, input().split())

INF = 10**8

dist= [INF] * (N+1)

def dijkstra(start, end):
    dist[start] = 0
    pq=[]
    heapq.heappush(pq, (0, start))
    
    while pq:
        cur_cost , cur_v  = heapq.heappop(pq)
        if dist[cur_v] != cur_cost:
            continue
          
        if cur_v == end:
            return cur_cost
        
        for cost, next_v in graph[cur_v]:
            next_cost = cur_cost + cost
            if next_cost < dist[next_v]:
                dist[next_v] = next_cost
                heapq.heappush(pq, (next_cost, next_v))
        
    
dijkstra(s, e)
print(dist[e])





