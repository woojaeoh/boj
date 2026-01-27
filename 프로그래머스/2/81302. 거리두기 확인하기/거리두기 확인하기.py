from collections import deque

def solution(places):
    
    answer = []
    for place in places:
        answer.append(1 if check(place) else 0)
    
    return answer


def check(place):
    
    for i in range(5):
        for j in range(5):
            if place[i][j] == "P":
                if not bfs(place, i, j):
                    return False
    
    return True

def bfs(place,r, c):
    
    q = deque()
    q.append((r,c,0))
    visited =[[False]*5 for _ in range(5) ]
    visited[r][c] = True
    
    while q:
        cur_r, cur_c , dist  = q.popleft()
        
        for dr, dc in [(-1, 0), (1,0) , (0,-1), (0,1)]:
            next_r = cur_r + dr
            next_c = cur_c + dc
            next_dist = dist+1
        
            if next_dist > 2:
                continue   
                    
        
            if 0<= next_r < 5  and 0<=  next_c < 5 :
                if not visited[next_r][next_c]:
                    
                    if place[next_r][next_c] != "X":                        
                        if place[next_r][next_c] == "P":
                            return False
                        else:
                            q.append((next_r, next_c, dist+1))
                            visited[cur_r][cur_c] = True
                                                      
        
    return True
                    