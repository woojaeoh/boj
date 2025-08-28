import sys
from collections import defaultdict
from collections import deque
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N , M , V = map(int, input().split()) #N은 정점의 수, M은 간선의 수 , V는 출발 노드.
graph = defaultdict(list)

for _ in range(M):
    a ,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for k in graph:
    graph[k].sort()
    

def bfs(start_v):
    visited_bfs=[start_v] #새로운 리스트로 덮어씌움.
    queue = deque()
    queue.append(start_v) 
    
    while queue:
        cur_v = queue.popleft()
        for v in graph[cur_v]:
            if v not in visited_bfs:
                visited_bfs.append(v)
                queue.append(v)

    return visited_bfs

visited_dfs = []


#dfs는 재귀 이용. 깊게 탐색 후 돌아오기
def dfs(start_v):
    visited_dfs.append(start_v)
    for v in graph[start_v]:
        if v not in visited_dfs:
            dfs(v)

dfs(V)
print(*visited_dfs)


print(*bfs(V))
 