import sys
from collections import defaultdict, deque

#6 3 15
# 0 0 1 0 0 0
# 0 0 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 1 0
# 0 0 0 1 0 0
# 6 5
# 2 2 5 6
# 5 4 1 6
# 4 2 3 5

input = sys.stdin.readline

N, M, fuel = map(int, input().split()) #격자, 승객 수 , 초기 연료

graph = [list(map(int, input().split())) for _ in range(N)]

taxi_r , taxi_c = map(int, input().split()) #택시 출발 지점
taxi_r -= 1
taxi_c -= 1

passenger = {}

dx =[-1, 1, 0, 0]
dy =[0, 0, -1 ,1]

#코드 설계
# 현재 지점에서 가장 가까운 승객의 좌표를 찾아야 한다. -> find_shortest_passenger

def search_shortest_node_bfs(r, c): 
    
    if (r, c) in passenger:
        return r, c, 0
    
    visited =[[False] * N for _ in range(N)]
    candidate = []
    dist = float('inf')
        
    q = deque()
    q.append((r, c, 0))
    visited[r][c] = True
    
    while q:
        cur_r, cur_c, cur_cost = q.popleft()
        
        if dist < cur_cost: #더 큰 가중치는 더이상 탐색 x
            continue
                
        if (cur_r, cur_c) in passenger:
            candidate.append((cur_r, cur_c))
            dist =  min(dist, cur_cost)
            continue
                
        for i in range(4):
            next_r = cur_r + dx[i]
            next_c = cur_c + dy[i]
            
            if 0 <= next_r < N and 0 <= next_c < N:
                if graph[next_r][next_c] == 0 and not visited[next_r][next_c]:
                    visited[next_r][next_c] = True
                    q.append((next_r, next_c, cur_cost + 1))
    
    if len(candidate) == 0:
        return -1, -1, -1

    #candidate.sort(key=lambda x : (x[0], x[1]))
    candidate.sort()
    x, y = candidate[0]
        
                        
    return x, y ,dist


def from_passenger_to_destinaiton(r, c, dest_r, dest_c): #승객 -> 목적지
    
    visited = [[False]*N for _ in range(N)]
    
    q = deque()
    q.append((r, c, 0))
    visited[r][c] = True
    
    while q:
        cur_r, cur_c, cur_cost = q.popleft()
    
        if (cur_r, cur_c) == (dest_r, dest_c):
            return cur_cost
                
        for i in range(4):
            next_r = cur_r + dx[i]
            next_c = cur_c + dy[i]
            
            if 0<= next_r < N and 0 <= next_c < N:
                if graph[next_r][next_c] == 0 and not visited[next_r][next_c]:
                    visited[next_r][next_c] = True
                    q.append((next_r, next_c, cur_cost+1))              
    
    return -1



for num in range(M): #승객들의 출발지, 목적지를 저장.
    passenger_r , passenger_c, dest_r , dest_c = map(int, input().split()) #승객들의 출발지, 목적지 좌표
    passenger_r -= 1
    passenger_c -= 1
    dest_r -= 1
    dest_c -= 1
    
    dist = from_passenger_to_destinaiton(passenger_r, passenger_c, dest_r, dest_c)
    passenger[(passenger_r, passenger_c)] = (dest_r, dest_c, dist)
    #여기서 (passenger_r, passenger_c) -> dest_r, dest_c까지 얼마나 걸리는지 저장해놓기?
    
  
for _ in range(M):
    r, c, cost = search_shortest_node_bfs(taxi_r, taxi_c) #초기 택시 좌표로부터 
    
    if fuel -cost < 0 or (r,c,cost) == (-1,-1,-1):
        print(-1)
        exit()
    else:
        fuel -= cost
        taxi_r, taxi_c, cost = passenger[(r,c)]
        if cost == -1 or fuel < cost:
            print(-1)
            exit()
            
        fuel -= cost
        fuel += (cost * 2)
        
        del passenger[(r,c)]
        

print(fuel)
        
    


