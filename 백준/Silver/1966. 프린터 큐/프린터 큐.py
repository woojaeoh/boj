import sys
from collections import deque

cases = int(sys.stdin.readline())

for _ in range(cases):
    n, m= map(int,sys.stdin.readline().split())
    priority = deque(map(int,sys.stdin.readline().split()))
    count = 0 #반복문을 제어하는 count
    
    while priority:
        max_num = max(priority) #가장 큰 수 확인
        front = priority.popleft()
        m -= 1
        
        if max_num  == front:
            count +=1
            if m < 0:
                print(count)
                break
        else:
            priority.append(front)
            if m < 0:
                m = len(priority)-1

#가장 큰 해결책: 구하려는 인덱스m에 대한 값을 pop한 후 맨 뒤에 append함으로써
# max값을
#해당 인덱스가 큐에서 몇번쨰의 중요도를 가지고 있는지 파악
        