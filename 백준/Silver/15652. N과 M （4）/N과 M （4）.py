import sys
input = sys.stdin.readline

N, M = map(int,input().split()) # 4 2

cost =[v+1 for v in range(N)]

def backtracking(idx, curr):
    
    if len(curr) == M:
        print(*curr)
        return
    
    for i in range(idx, N):
        curr.append(i+1)
        backtracking(i, curr)
        curr.pop()
        
backtracking(0, [])