from collections import deque

def find_next_coordinate(n, board, cur_pos):

    next_pos = []
    pos = list(cur_pos)
    r1, c1, r2, c2 = pos[0][0] , pos[0][1], pos[1][0], pos[1][1]
    
        
    #상하좌우 먼저 검사
    for dr, dc in [(-1,0),(1,0), (0,-1), (0, 1)]:        
        nr1, nc1, nr2, nc2 = r1 + dr ,c1 + dc,  r2+dr , c2+ dc
        if 0 <= nr1 < n and 0 <= nc1 < n and 0 <= nr2 < n and 0 <= nc2 < n:
            if board[nr1][nc1] == 0 and board[nr2][nc2] == 0:
                next_pos.append([(nr1, nc1), (nr2, nc2)])
                
    #로봇이 가로로 뉘여진 경우
    if r1 == r2:
        for i in [-1, 1]:
            if 0 <= r1 + i < n and 0<= r2+i < n and 0<= c1 <n and 0<= c2 < n:
                if board[r1 + i][c1] == 0 and board[r2+i][c2] == 0:
                    next_pos.append([(r1+i, c1), (r1, c1)])
                    next_pos.append([(r2+i, c2), (r2, c2)])
                        
                    
    #로봇이 세로로 뉘여진 경우
    if c1 == c2:
        for i in [-1,1]:
            if 0 <= c1 + i < n and 0<= c2+i < n and 0<= r1 <n and 0<= r2 < n:
                if board[r1][c1+i] == 0 and board[r2][c2+i] == 0:
                    next_pos.append([(r1, c1+i), (r1, c1)])
                    next_pos.append([(r2,c2+i), (r2, c2)])
                          
                    
    return next_pos
                    
def solution(board):
    
    n = len(board)
    

    #초기 좌표
    
    start = {(0,0), (0,1)}
    
    q = deque()
    q.append((start, 0))
    visited = {frozenset(start)}
    
    while q:
        
        cur_pos, dist= q.popleft()
        
        if (n-1, n-1) in cur_pos:
            return dist
        
    
        for next_pos in find_next_coordinate(n, board, cur_pos):
            state = frozenset(next_pos)
            if state not in visited:
                q.append((next_pos, dist+1))
                visited.add(state)
                
    
    return -1