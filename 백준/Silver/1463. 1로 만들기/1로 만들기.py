import sys

input = sys.stdin.readline
N = int(input())


memo = {
    1 : 0
    }


for x in range(2, N+1):
    best = memo[x-1]+1
    
    if x % 2 == 0:
        best = min(best , memo[x//2]+1 )
    if x % 3 == 0:
        best = min(best , memo[x//3]+1 )
    
    memo[x] = best 
    
print(memo[N])   

# 바텀 업 방식으로 수정  - N제한이 10의 6승이기에 재귀 깊이로 인한 메모리 초과 이슈?