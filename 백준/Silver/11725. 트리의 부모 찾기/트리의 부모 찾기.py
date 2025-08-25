import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 **6) #재귀 호출 깊이 제한 해제 (파이썬 기본 뎁쓰 1000)

N=int(input())
visited=[False]* (N+1)        
parent=[0]*(N+1)

graph=[[] for _ in range(N+1)]
for _ in range(N-1):
    n,m = map(int, input().split())
    graph[n].append(m)
    graph[m].append(n)

def dfs(graph,v,visited):
    visited[v]=True
    for i in graph[v]:
        if not visited[i]:
            parent[i] = v
            dfs(graph,i,visited)

    
dfs(graph,1,visited)

for i in range(2,N+1):
    print(parent[i])