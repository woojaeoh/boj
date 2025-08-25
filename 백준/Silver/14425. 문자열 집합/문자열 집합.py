import sys 

input =sys.stdin.readline

n, m = map(int,input().split())

memo={}
for _ in range(n):
    str = input()
    memo[str]=True

count =0
for _ in range(m):
    str = input()
    if str in memo:
        count +=1

print(count) 
         

