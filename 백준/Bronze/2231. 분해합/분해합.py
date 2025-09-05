import sys

input = sys.stdin.readline
n = int(input())

generator = 0
for v in range(n):
    generator += v
    for i in str(v):
        generator += int(i)
    
    if generator == n:
        print(v)
        break
    else:
        generator = 0
        

if generator ==0:
    print(0)