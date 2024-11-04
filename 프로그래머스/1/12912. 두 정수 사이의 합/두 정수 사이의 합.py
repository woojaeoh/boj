def solution(a, b):
    answer = 0
    list=[]
    if a<b:
        for i in range(a,b+1):
            list.append(i)
    else:
        for i in range(b,a+1):
            list.append(i)
            
    answer=sum(list)
    return answer