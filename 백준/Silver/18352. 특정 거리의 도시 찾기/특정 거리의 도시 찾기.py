import sys 
from collections import defaultdict, deque

input = sys.stdin.readline
graph = defaultdict(list)

N, M, K, X = map(int, input().split())   # N은 노드 수, M은 간선 수 , K는 거리 정보 , X는 출발 도시 번호

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    

dist=[-1]*(N+1)    
dist[X] = 0

q = deque()
q.append(X)

while q:
    cur = q.popleft()
    for next in graph[cur]:
        if dist[next] == -1:
            dist[next] = dist[cur]+1
            q.append(next)
            

ans = [v for v in range(1,N+1) if dist[v] == K]

if ans:
    ans.sort()
    for i in ans:
        print(i)
else:
    print(-1)
