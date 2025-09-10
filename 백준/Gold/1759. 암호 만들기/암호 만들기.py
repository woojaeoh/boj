import sys
from itertools import combinations

input = sys.stdin.readline

L, C = map(int,input().split()) #4 , 6 

password = list(input().split())
password.sort()

vowels = set("aeiou")

for comb in combinations(password, L):
    vcs, cons =0, 0
    for k in comb:
        if k in vowels:
            vcs +=  1
        else:
            cons += 1
    if vcs >=1 and cons>=2:
        print(''.join(comb))
