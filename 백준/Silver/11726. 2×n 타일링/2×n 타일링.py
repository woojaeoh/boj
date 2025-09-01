import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
n = int(input())

memo={}

def dp(n):
    
    if n == 1 :
        return 1
    
    if n ==2 :
        return 2
    
    if n not in memo:
        memo[n] = dp(n-1) + dp(n-2)
    
    return memo[n]
    
    
print(dp(n)%10007)