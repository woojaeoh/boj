import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
N = int(input())

INF = 5001
memo={
    0:0
}

def dp(n):
    
    if n < 0 :
        return INF     
    
    if n not in memo:
        memo[n] = min( dp(n-5) + 1, dp(n-3) + 1)
        
    return memo[n]


if dp(N) < INF:
    print(dp(N))
else:
    print(-1)