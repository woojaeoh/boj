def solution(today, terms, privacies):
    #today  = "2022.05.19"
    # terms = ["A 6", "B 12", "C 3"]
    # privacies =["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
    
    dict = {}
    
    def change_day(year, month , day):
        real = year*12*28
        real += month*28
        real += day
        
        return real
    
    for term in terms:
        rule, month = term.split() # A 6
        dict[rule] = change_day(0,int(month),0)
    
    t_year, t_month, t_day = map(int, today.split("."))
    today_day =  change_day(t_year, t_month, t_day)    
    
    result = []
    for i, p in enumerate(privacies):
        date, rule = p.split() # 2021.0502 , A
        year , month, day = map(int, date.split(".")) # 2021, 05, 02
        
        real_day = change_day(year, month, day)
        
        if real_day + dict[rule] <= today_day:
            result.append(i+1)
    
    return result