def solution(n):
    answer = 0
    
    for i in range(1,n+1):
        if i*i==n:
            answer=(i+1)*(i+1)
            break
            
        elif i*i>n:
            answer=-1
            break
            
    return answer