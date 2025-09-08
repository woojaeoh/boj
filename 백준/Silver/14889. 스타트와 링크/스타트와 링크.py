import sys

input = sys.stdin.readline
n = int(input())

ability = [list(map(int, input().split())) for _ in range(n)]

visited =[False for _ in range(n)]

min_gap = 200000

def backtracking(L, idx):
    global min_gap
    
    if L == n//2:
        team_start = 0
        team_rink = 0
       
        for i in range(n):
            for j in range(n): 
                if visited[i] and visited[j]:
                    team_start += ability[i][j]
                if not visited[i] and not visited[j]:
                    team_rink += ability[i][j]
        min_gap = min(min_gap,abs(team_start-team_rink))                    
        return
    
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            backtracking(L+1, i+1)
            visited[i] = False
            
backtracking(0,0)
print(min_gap)