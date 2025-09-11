import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int,input().split()) # 4 2

cost =[v+1 for v in range(N)]

for v in combinations(cost,M):
    print(*v)
