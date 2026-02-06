def solution(today, terms, privacies):
    result =[]
    term_dict = {}
    
    for term in terms:
        provision, valid = term.split() # A 6
        term_dict[provision] = int(valid)
    
    for i, p in enumerate(privacies):
        date , provision = p.split()
        year, month, day = map(int, date.split("."))
        month += term_dict[provision]
        
        count = 0
        if month > 12:
            count = month // 12
            year += count
            month %= 12
            if month == 0:
                month = 12
                year -= 1 
                       
        if day == 1 :
            day = 28
            if month == 1:
                month = 12
                year-= 1
            else:
                month -= 1
        else:
            day -= 1    
            
        t_year , t_month , t_day = map(int,today.split("."))
        
        if 2000<= t_year <= 2022 and year < t_year:
            result.append(i+1)
            continue
        if 2000<= t_year <= 2022 and year == t_year and month < t_month:
            result.append(i+1)
            continue
        
        if 2000<= t_year <= 2022 and year == t_year and month == t_month and day < t_day:
            result.append(i+1)
            continue
            
    return result