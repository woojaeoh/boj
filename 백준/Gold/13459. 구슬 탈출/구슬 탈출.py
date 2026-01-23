import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

board = [input().rstrip() for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

rr = rc = br = bc =0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            rr, rc = i, j
        elif board[i][j] == 'B':
            br, bc = i, j
            
q = deque()
q.append((rr, rc, br, bc, 0))

visited =set()
visited.add((rr, rc,br,bc))

def move(r, c, dx, dy):
    count = 0
    while board[r+dx][c+dy] != '#' and board[r][c] != 'O': 
        r += dx
        c += dy
        count += 1
        
    return r, c, count

while q:
    cur_rr, cur_rc, cur_br ,cur_bc, depth = q.popleft()
    
    if depth >= 10:
        continue
    
    
    for i in range(4):
        next_rr, next_rc, cnt_r =  move(cur_rr, cur_rc, dx[i] , dy[i])
        next_br ,next_bc, cnt_b =  move(cur_br, cur_bc, dx[i] , dy[i])
        
        
        if board[next_br][next_bc] == 'O':
            continue
        
        if board[next_rr][next_rc] == 'O':
            print(1)
            exit()
        
        if next_rr == next_br and next_rc == next_bc:
            if cnt_r > cnt_b:
                next_rr -= dx[i]
                next_rc -= dy[i]
            else:
                next_br -= dx[i]
                next_bc -= dy[i]
                
        
        if (next_rr, next_rc, next_br, next_bc) not in visited:
            visited.add((next_rr, next_rc, next_br, next_bc))
            q.append((next_rr, next_rc, next_br, next_bc, depth + 1))
        
        
    
print(0)