import sys
from collections import deque

input =sys.stdin.readline

N= int(input())

grid =[list(map(int,input().strip())) for _ in range(N)]
visited=[[False]*N for _ in range(N)]
answer=[]

dx =[-1, 1, 0, 0]
dy =[0, 0, -1, 1]

def bfs(x,y):
    count = 1
    queue = deque()
    visited[x][y] = True
    queue.append((x,y))
    while queue:
        cur_x,cur_y = queue.popleft()
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            if next_x >= 0 and next_x < N and next_y >=0 and next_y <N:
                if grid[next_x][next_y]== 1 and not visited[next_x][next_y]:
                         visited[next_x][next_y] = True
                         queue.append((next_x,next_y))
                         count += 1
    answer.append(count)

danji=0
for i in range(N):
    for j in range(N):
        if grid[i][j] == 1 and not visited[i][j]:
            bfs(i,j)
            danji +=1

answer.sort()
print(danji)
for i in answer:
    print(i)
            