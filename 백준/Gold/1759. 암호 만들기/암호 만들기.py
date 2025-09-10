import sys
from itertools import combinations

input = sys.stdin.readline

L, C = map(int,input().split()) #4 , 6 

password = list(input().split())
password.sort()

vowels = set("aeiou")


#password_poten = combinations(password, L)
def backtracking(idx, curr, vow, cons): #백트래킹 -> 재귀
       
    if len(curr) == L:
        if vow >=1 and cons >=2:
            print(''.join(curr))
        return
            
    for i in range(idx ,C):
        ch = password[i]
        if ch in vowels:
            backtracking(i+1, curr + [ch], vow+1, cons)
        else:
            backtracking(i+1, curr + [ch], vow, cons+1)
    

backtracking(0, [], 0, 0)