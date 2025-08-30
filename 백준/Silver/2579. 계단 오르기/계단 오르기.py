import sys
input = sys.stdin.readline
N = int(input()) # 6

cost= [0] + [int(input()) for _ in range(N)] # cost= [10,20,15,25,10,20] 

memo={}

#top-down: 재귀
def dp(n):
    # base case 설정
    if n == 0:
        return 0
    if n ==1:
        return cost[1]
    if n == 2:
        return cost[1] + cost[2]    
    if n not in memo :
        memo[n] = max( dp(n-3)+ cost[n-1] + cost[n], dp(n-2) + cost[n]) #memo에 없는 경우 메모리에 한번은 저장을 해놔야 한다.
    return memo[n]

print(dp(N))