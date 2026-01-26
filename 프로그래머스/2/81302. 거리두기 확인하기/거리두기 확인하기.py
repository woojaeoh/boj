from collections import deque

def solution(places):
    result = []     
    for place in places:
        result.append((1 if check(place) else 0 ))
        
    return result


def check(place):
    for r in range(5):
        for c in range(5):
            if place[r][c] == "P":
                if not bfs(r, c, place):
                    return False
    
    return True



def isValid(x, y, place, visited):
    return 0<= x <5 and 0<= y< 5 and place[x][y] != "X" and not visited[x][y]


def bfs(start_r, start_c, place):
    
    visited =[[False ]*5 for _ in range(5)]
    q = deque()
    q.append((start_r, start_c, 0))
    visited[start_r][start_c] = True
    
    while q:
        r, c, dist = q.popleft()
    
        #직선거리 방문처리
        for dr, dc in [(-1,0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc

            if not isValid(nr, nc, place, visited):
                continue
                
            if dist > 1:
                continue
            
            if place[nr][nc] == "P":
                return False
            
            visited[nr][nc] = True
            q.append((nr, nc, dist+1))
                
            
    
#     #대각선 방문처리
#     #좌상
#     if isValid(r, c-1, place) and isValid(r-1, c, place):
#         if isValid(r-1,c-1, place):
#             visited[r-1][c-1] = True
    
#     #상우
#     if isValid(r-1, c, place) and isValid(r, c+1, place):
#         if isValid(r-1,c+1, place):
#             visited[r-1][c+1] = True
    
#     #우하
#     if isValid(r, c+1, place) and isValid(r+1, c, place):
#         if isValid(r+1,c+1, place):
#             visited[r+1][c+1] = True
            
#     #하좌
#     if isValid(r+1, c, place) and isValid(r, c-1, place):
#         if isValid(r+1,c-1, place):
#             visited[r+1][c-1] = True
    
    
    return True
            