def solution(a, b):
    #아이디어 1. 
    answer = ''
    day=["THU","FRI","SAT","SUN","MON","TUE","WED"]
    month_days=[31,29,31,30,31,30,31,31,30,31,30,31]
    total_days=0
    for i in range(a-1):
        total_days+=month_days[i]
    total_days+=b
    result=total_days%7
    answer=day[result]
    return answer