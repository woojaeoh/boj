def solution(data):
    answer=True
    
    countp=0
    county=0
    
    data=data.lower()
    
    
    for i in data:
        if i=='p':
            countp+=1
        if i=='y' :
            county+=1

    if countp!=county:
        answer=False

    return answer


