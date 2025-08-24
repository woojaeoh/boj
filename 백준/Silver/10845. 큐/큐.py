import sys
from collections import deque

n = int(sys.stdin.readline())
queue =deque()

for _ in range(n):
    input = sys.stdin.readline().split()
    inst = input[0]
    
    if inst =="push":
        x = int(input[1])
        queue.append(x)
        
    elif inst == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
            
    elif inst == "size":
        print(len(queue))
            
    elif inst == "empty":
        if queue:
            print(0)
        else:
            print(1)
    
    elif inst ==  "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
            
    elif inst == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)





#queue.append()
#queue.popleft()