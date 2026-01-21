import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

N , M = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(N)]

dx =[-1, 1, 0, 0]
dy= [0, 0, -1, 1]

virus = []
empty = 0

for i in range(N):
    for j in range(N):
        if grid[i][j] == 2:
            virus.append((i, j))
        elif grid[i][j] == 0:
            empty += 1
            
            


answer=float('inf')

for scattered_virus in combinations(virus, M):
    
    visited=[[False]*N for _ in range(N)]
    
    q = deque()
    
    for x, y in scattered_virus:
        q.append((x,y,0))    
        visited[x][y] = True
                  
    count = 0
    max_time =0
     
    while q:
        x, y, time = q.popleft()
        
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_x < N and 0 <= next_y < N and not visited[next_x][next_y]:
                if grid[next_x][next_y] != 1: #벽이 아니라면
                    q.append((next_x, next_y, time+ 1))
                    visited[next_x][next_y] = True
                    
                    if grid[next_x][next_y] == 0:
                        count += 1
                        max_time = time + 1
                       
    if empty == count:
        answer =  min(answer, max_time)

                
print(-1 if answer == float('inf') else answer)