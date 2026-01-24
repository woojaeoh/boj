import sys
from collections import deque

input = sys.stdin.readline

N, M, fuel = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

taxi_r, taxi_c = map(int, input().split())
taxi_r -= 1
taxi_c -= 1

passenger={} #승객의 시작위치 : 목적지를 저장하는 용도.

for _ in range(M):
    sr ,sc, dr, dc = map(int, input().split())
    passenger[(sr-1, sc-1)] = (dr-1, dc-1)
    


def find_passenger_bfs(r,c):
    
    q = deque()
    q.append((r,c,0)) # r, c, 좌표
    visited = [[False] * N for _ in range(N)]
    visited[r][c] =True
    candidate = []
    min_dist = float('inf')
    
    while q:
        cur_r, cur_c, dist = q.popleft()
        
        if min_dist < dist:
            continue
        
        if (cur_r, cur_c) in passenger:
            min_dist = min(min_dist, dist)
            candidate.append((min_dist,cur_r,cur_c))
            continue
        
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            next_r = cur_r + dx
            next_c = cur_c + dy        
            if 0 <= next_r < N and 0<= next_c < N:
                if not visited[next_r][next_c] and board[next_r][next_c] == 0:
                    q.append((next_r, next_c, dist + 1))
                    visited[next_r][next_c] = True
    
    if not candidate:
        print(-1)
        exit()
        
    candidate.sort()
    
    return candidate[0][1], candidate[0][2], candidate[0][0] # 갈 수 있는 가장 빠른 손님의 r, c, dist


def go_destination_bfs(r, c):
    
    q = deque()
    q.append((r,c,0)) # r, c, 좌표
    visited = [[False] * N for _ in range(N)]
    visited[r][c] =True
    dest_r , dest_c = passenger[(r,c)]
    while q:
        cur_r, cur_c, dist = q.popleft()
        
        if cur_r == dest_r and cur_c ==dest_c:
            return cur_r, cur_c, dist
        
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            next_r = cur_r + dx
            next_c = cur_c + dy        
        
            if 0 <= next_r < N and 0<= next_c < N:
                if next_r == dest_r and next_c ==dest_c:
                    return next_r, next_c, dist+1
                
                if not visited[next_r][next_c] and board[next_r][next_c] == 0:
                    q.append((next_r, next_c, dist + 1))
                    visited[next_r][next_c] = True
    
    return None, None, -1
    

#메인실행.
for i in range(M):
    start_r, start_c , dist_s = find_passenger_bfs(taxi_r, taxi_c)
   # print(i, fuel)
    (taxi_r, taxi_c) = (start_r, start_c)
 #   print(start_r, start_c)
    
    if fuel - dist_s >= 0:
        fuel-= dist_s
    else:
        print(-1)
        exit()
        
    dest_r, dest_c , dist_d = go_destination_bfs(taxi_r, taxi_c)
    if dist_d == -1:
        print(-1)
        exit()
    (taxi_r, taxi_c) = (dest_r, dest_c)
  #  print(taxi_r, taxi_c)
    
    
    if fuel >= dist_d:
        fuel -= dist_d
        fuel += dist_d *2
    else:
        print(-1)
        exit()
    
    del passenger[(start_r, start_c)]
    
#    print(passenger)

print(fuel)