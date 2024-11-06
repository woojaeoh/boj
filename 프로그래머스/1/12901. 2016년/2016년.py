def solution(a, b):
    #2016년 a월 b일은 어떤 날인지?
    #2016년은 윤년
    #2016년 a월 b일은 실제로 있는 날 ex) 13월 26일 , 2월 45일 X
    
    day=["THU","FRI","SAT","SUN","MON","TUE","WED"]
    month_day=[31,29,31,30,31,30,31,31,30,31,30,31]
    weekday=7
    total_day=0
    
    if a>1:
        for i in range(a-1):
            total_day+=month_day[i]
            
    total_day+=b
    result=total_day%weekday
    return day[result]
        
        
    
    
    
    return answer