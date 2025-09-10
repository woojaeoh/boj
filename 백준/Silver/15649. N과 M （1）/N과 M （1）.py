import sys
from itertools import permutations

input =sys.stdin.readline
N, M = map(int, input().split())

cost = [ v+1 for v in range(N) ]


for i in permutations(cost, M):
    print(*i)
    