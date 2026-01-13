from collections import deque
def solution(queue1, queue2):
    
    count = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    length = len(queue1) * 3

    
    s1 = sum(q1)
    s2 = sum(q2)    
    
    while count < length*3:        
        
        if s1 == s2:
            return count
            
        if s1 > s2:
            x = q1.popleft()
            q2.append(x)
            s1 -= x
            s2 += x
        else:
            x = q2.popleft()
            q1.append(x)
            s2 -= x
            s1 += x
        count +=1
       
    return -1