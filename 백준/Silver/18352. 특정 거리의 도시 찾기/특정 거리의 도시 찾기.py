from collections import deque
n,m,k,x=map(int,input().split())

graph=[[]for _ in range(n+1)]

for _ in range(m):
  a,b=map(int,input().split())
  graph[a].append(b)

#거리정보 -1로 초기화
distance=[-1]*(n+1)
#현재 노드x를 0으로 선언
distance[x]=0

q=deque([x])

#큐가 빌 때 까지 bfs반복
while q:
  now=q.popleft()

  for i in graph[now]:
    if distance[i]==-1:
        distance[i]=distance[now]+1
        q.append(i)  


check=False
for i in range(1,n+1):
  if distance[i]==k:
    print(i)
    check=True

if check==False:
  print(-1)


