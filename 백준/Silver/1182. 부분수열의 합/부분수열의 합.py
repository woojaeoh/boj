import sys
from itertools import combinations
input = sys.stdin.readline

N, S = map(int,input().split())

cost = list(map(int, input().split()))
count=0
for v in range(N):
    for j in combinations(cost, v+1):
        if sum(j) == S:
            count += 1
        
print(count)
     
        