import sys
from collections import deque

input = sys.stdin.readline

N, M , fuel = map(int, input().split()) # 6, 3, 15 

grid  = [list(map(int, input().split())) for _ in range(N)] #좌표

taxi_r, taxi_c = map(int, input().split()) # 택시의 처음 위치
taxi_r-=1 #시작위치를 인덱스에 맞춰준다.
taxi_c-=1

# 승객 정보: {출발지: 목적지}
passengers = {}
for _ in range(M):
    sr, sc, dr, dc = map(int, input().split())
    passengers[(sr - 1, sc - 1)] = (dr - 1, dc - 1)


dx = [-1, 1, 0 , 0]
dy = [0, 0 , -1, 1]


def isValid(x, y, visited):
    return 0 <= x < N and 0<= y < N and grid[x][y] != 1 and not visited[x][y]


#현재 위치에서 가장 빠르게 갈 수 있는 승객을 찾는 BFS
def shortest_passengers_find(start_r, start_c, grid, passengers, fuel):
    q = deque()
    q.append((start_r,start_c, 0))
    
    visited = [[False]*N for _ in range(N)]
    visited[start_r][start_c] = True
    min_dist = None
    candidate=[]
    
    while q:
        r , c, dist = q.popleft()
        
        # if fuel <=  dist:
        #     break
        if fuel <  dist:
            break
        
        if min_dist is not None and min_dist < dist:
            continue
            
        
        if (r, c) in passengers:
            candidate.append((r,c))
            min_dist = dist
            continue
        
        
        for i in range(4):
            next_x = r + dx[i]
            next_y = c + dy[i]
            if isValid(next_x, next_y, visited):
                q.append((next_x, next_y, dist + 1))
                visited[next_x][next_y] = True
                
    if not candidate:
        return None, None, -1
    candidate.sort()
    px, py = candidate[0]      
    
    if min_dist is None:
        print(-1)
        exit()  
        
    return px, py, min_dist 
            
#출발지에서 목적지로    
def go_destination(r, c, passengers, fuel):

    q = deque()
    q.append((r, c, 0))
    visited =[[False]*N for _ in range(N)]
    visited[r][c] = True
    
    while q:
        cur_r, cur_c, dist = q.popleft()
        
        if dist > fuel:
            continue
        dest_r, dest_c = passengers[(r, c)]
        if cur_r == dest_r and cur_c == dest_c:
            return cur_r, cur_c, dist
        
        for i in range(4):
            next_x = cur_r + dx[i]
            next_y = cur_c + dy[i]
            if isValid(next_x, next_y, visited):
                q.append((next_x, next_y, dist + 1))
                visited[next_x][next_y] = True

    return None, None, -1

for _ in range(M):
    
    cur_r , cur_c, goto_passenger_used_fuel = shortest_passengers_find(taxi_r, taxi_c, grid, passengers, fuel)
    if goto_passenger_used_fuel == -1:
        print(-1)
        exit()
    fuel -= goto_passenger_used_fuel
    taxi_r , taxi_c = cur_r, cur_c
 #   print("1번")
    x, y , goto_destination_used_fuel  = go_destination(taxi_r, taxi_c, passengers, fuel)
    
    if goto_destination_used_fuel == -1:
        print(-1)
        exit()
 #   print("2번")
    taxi_r , taxi_c = x, y
    
    if fuel - goto_destination_used_fuel >= 0:
        fuel -= goto_destination_used_fuel
        fuel += goto_destination_used_fuel * 2
    else:
 #       print("3번")
        print(-1)
        exit()


    del passengers[(cur_r, cur_c)]
    
    if not passengers:
        break

print(fuel)


