import sys
from collections import deque

input = sys.stdin.readline

N, M  = map(int, input().split())

grid = [input().rstrip() for _ in range(N)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# R과 B의 좌표 저장
rx = ry = bx = by = 0
for i in range(N):
    for j in range(M):
        if grid[i][j] == 'R':
            rx, ry = i, j
        elif grid[i][j] == 'B':
            bx, by = i, j

def move(x, y , dx, dy):
    
    count = 0
    while grid[x + dx][y + dy] != "#" and grid[x][y] != 'O':
        x += dx
        y += dy
        count += 1
        
    return x, y, count
    

q = deque()
q.append((rx, ry, bx, by , 0))
visited = set()
visited.add((rx, ry, bx, by))

while q:
    
    cur_rx, cur_ry, cur_bx, cur_by, depth = q.popleft()
    
    if depth >= 10:
        continue
       
    for i in range(4):
        
        next_rx, next_ry, cnt_r = move(cur_rx, cur_ry , dx[i], dy[i])
        next_bx, next_by, cnt_b = move(cur_bx, cur_by , dx[i], dy[i])
        
        if grid[next_bx][next_by] == 'O':
            continue
        
        if grid[next_rx][next_ry] == 'O':
            print(1)
            exit()
            
        
        if next_rx == next_bx and next_ry == next_by:
            if cnt_r > cnt_b:
                next_rx -= dx[i]
                next_ry -= dy[i]
            else:
                next_bx -= dx[i]
                next_by -= dy[i]
                
        if (next_rx, next_ry, next_bx, next_by) not in visited:
            visited.add((next_rx, next_ry, next_bx, next_by))
            q.append((next_rx, next_ry, next_bx, next_by, depth+1))
            
print(0)
                
                