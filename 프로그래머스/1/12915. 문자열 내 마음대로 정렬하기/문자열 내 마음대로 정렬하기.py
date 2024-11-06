def solution(strings, n):
    answer=[]
    # strings의 n번째 문자열로 비교한다.
    # u, e ,a 
    # n번째 문자열로 정렬
    answer=sorted(strings,key=lambda x: (x[n],x))
    
    
    return answer