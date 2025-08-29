import sys 
from collections import deque

input =sys.stdin.readline

M, N = map(int, input().split()) # 6, 4

apple =[list(map(int,input().split())) for _ in range(N)]
dist=[[-1]*M for _ in range(N)]
q = deque()

# 초기 익은 과일(1)들을 모두 큐에 넣고 시작일(0일)로 설정
for r in range(N):
    for c in range(M):
        if apple[r][c] == 1:
            q.append((r, c))
            dist[r][c] = 0  # 시작점은 0일
            
dx =[-1,1,0,0]
dy =[0,0,-1,1]

while q:
    cur_x , cur_y = q.popleft()
    for i in range(4):
        next_x = cur_x + dx[i]
        next_y = cur_y + dy[i]
        if next_x >=0 and next_x <N and next_y >=0 and next_y < M:
            if apple[next_x][next_y] == 0:
                apple[next_x][next_y] = 1
                q.append((next_x, next_y))
                dist[next_x][next_y] = dist[cur_x][cur_y]+ 1
                
                    

if any(0 in row for row in apple):
    print(-1)
else: 
    ans= 0 # -1은 자동 무시
    for i in range(N):
        for j in range(M):
            if ans< dist[i][j]:
                ans= dist[i][j]
                
    print(ans)
            
    


