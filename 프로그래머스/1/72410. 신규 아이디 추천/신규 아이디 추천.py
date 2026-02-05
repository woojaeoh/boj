def solution(new_id):
    n = len(new_id)
    
    #1단계
    result = new_id.lower()
    
    temp =""
    #2단계
    for c in result:
        if c.isalpha() or c.isdigit() or c == "-" or  c == "_" or c == ".":
            temp += c
    result = temp
    
    #3단계 -> 마침표가 두번 연속된것을 하나의 점으로.
    prev = ""
    ans = ""
    for num in result:
        if num == ".": # 현재 값이 . 이라면
            if prev == ".": # 그리고 이전 값도 . 이라면?
                continue
            
        prev = num
        ans += num
    
    result = ans
    
    #4단계
    if len(result) > 0 and result[0] == '.' :
        result = result[1:]
    if len(result) > 0 and result[-1] == '.' :
        result = result[:-1]
    
    #5단계
    if not result:
        result = "a"
    
    #6단계
    if len(result) >= 16:
        result = result[:15]
        if result[-1] == ".":
            result = result[:14]
            
    #7단계
    while len(result) <= 2:
        result += result[-1]
          
        
    return result