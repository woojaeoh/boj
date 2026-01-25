#움직임 -> 위 아래 
#힌트1. 로봇은 (0,0) (0,1)에서 시작. ->두 칸이 묶여있음.
#힌트2. 위 , 아래 이동 가능
#힌트3. 90도 회전도 가능. 그러나 중간에 벽이 있으면 안된다.
#힌트4. 최단거리 -> BFS 힌트
# 100*100* 4* 8
from collections import deque

def isValid(r1, c1, r2, c2, n, board):
    return 0<= r1 < n and  0<= c1 < n and 0<= r2 < n and  0<= c2 < n
def bfs(cur_pos ,n, board ):
     
    next_pos =[]
    pos =list(cur_pos)
    r1, c1, r2, c2 = pos[0][0] , pos[0][1], pos[1][0], pos[1][1]
        
    #상하좌우 검사
    for dr, dc in [(-1,0),(1,0),(0,-1), (0,1)]:
        nr1 , nc1, nr2, nc2  = r1 + dr, c1 + dc, r2 + dr, c2 + dc
        if isValid(nr1, nc1, nr2, nc2, n, board):
            if board[nr1][nc1] == 0 and board[nr2][nc2] ==0:
                
                next_pos.append(((nr1,nc1),(nr2,nc2)))
                
    #로봇이 세로로 누운경우 -> y좌표가 같다
    if c1 == c2:
        for i in [-1,1]:
            if isValid(r1 , c1 + i, r2, c2 + i, n , board):
                if board[r1][c1 + i] == 0 and board[r2][c2 + i] ==0:
                    next_pos.append(((r2, c2), (r2, c2 + i)))
                    next_pos.append(((r1, c1 + i), (r1, c1)))
        
        
    #로봇이 세로로 누운 경우
    if r1 == r2:
        for i in [-1, 1]:
            if isValid(r1 + i,c1, r2 + i, c2, n , board):
                if board[r1 + i][c1] ==0 and board[r2 + i][c2] ==0:
                    next_pos.append(((r1, c1), (r1 + i, c1)))
                    next_pos.append(((r2 + i, c2), (r2, c2)))
                
    return next_pos      
    
def solution(board):
    
    n = len(board)
    
    start = {(0,0), (0,1)} # set
    
    q = deque()
    q.append((start, 0))    
    visited ={frozenset(start)}
    
    while q:
        cur_pos ,dist= q.popleft()
        
        if (n-1, n-1) in cur_pos:
            return dist
        
        for next_pos in bfs(cur_pos, n, board):
            state = frozenset(next_pos)
            if state not in visited:
                q.append((next_pos, dist+1))
                visited.add(state)
        
    return -1