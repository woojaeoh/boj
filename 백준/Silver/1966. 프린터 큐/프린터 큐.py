import sys
from collections import deque

input =sys.stdin.readline
cases = int(input())

for _ in range(cases):
    n, m= map(int,input().split())
    priority = list(map(int,input().split()))
    
    q = deque(enumerate(priority))
    
    target =sorted(priority, reverse=True)
    
    count = 0 #반복문을 제어하는 count
    
    while True:
        i, p = q[0]
        
        if p  == target[count]:
            q.popleft()
            count +=1
            if i == m:
                print(count)
                break
        else:
            idx,pri = q.popleft()
            q.append((idx,pri))