import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split()) # 7 7 

grid = [ list(map(int, input().split())) for _ in range(N) ]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]



def bfs(x, y, visited):
    
    
    q =deque()
    q.append((x,y))
    visited[x][y] = True
      
    while q:
        cur_x , cur_y = q.popleft()
        
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            
            if 0 <= next_x < N and 0 <= next_y < M and not visited[next_x][next_y] and grid[next_x][next_y] != 1:
                q.append((next_x, next_y))
                visited[next_x][next_y] = True 
            

isValid = set()

for i in range(N):
    for j in range(M):
        if grid[i][j] == 0:
            isValid.add((i,j))
            
                
max_safe = 0

for walls in combinations(isValid,3):
    
    count = 0 
    
    visited = [ [False] * M for _ in range(N) ]
    
    grid[walls[0][0]][walls[0][1]] = 1 
    grid[walls[1][0]][walls[1][1]] = 1
    grid[walls[2][0]][walls[2][1]] = 1
    
    visited[walls[0][0]][walls[0][1]] = True
    visited[walls[1][0]][walls[1][1]] = True
    visited[walls[2][0]][walls[2][1]] = True
    
    
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 2 and not visited[i][j]:
                bfs(i, j, visited)
    
    
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and grid[i][j] == 0:
                count+=1
            
    max_safe = max(max_safe, count)
    
    grid[walls[0][0]][walls[0][1]] = 0 
    grid[walls[1][0]][walls[1][1]] = 0
    grid[walls[2][0]][walls[2][1]] = 0
    
    

print(max_safe)



    
            

