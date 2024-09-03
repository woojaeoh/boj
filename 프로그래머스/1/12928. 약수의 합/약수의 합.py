def solution(n):
    yaksu=[]
    for i in range(1,n+1):
        if n%i==0:
            yaksu.append(i)
            
    answer = sum(yaksu)
    return answer