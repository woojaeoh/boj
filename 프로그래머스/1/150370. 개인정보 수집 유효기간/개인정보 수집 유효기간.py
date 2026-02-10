def solution(today, terms, privacies):
    dict ={}
    result =[]
    def change_days(year, month , day):
        days = day
        days += year * 336
        days += month * 28
        return days
    
    for term in terms:
        name, month = term.split()
        dict[name] = int(month) * 28
    
    cur_year, cur_month, cur_day = map(int, today.split('.'))
    cur_days = change_days(cur_year, cur_month, cur_day)
    print(cur_days)
    for i, p in enumerate(privacies):
        date, name = p.split()
        year, month , day = map(int, date.split('.'))
        limit_day = change_days(year, month, day)
        end_days = limit_day + dict[name]
        print(end_days)
        if cur_days >= end_days:
            result.append(i+1)
            
    return result