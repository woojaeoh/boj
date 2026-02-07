def solution(new_id):
    
    #1단계
    new_id  = new_id.lower()
    
    #2단계
    temp =""
    for num in new_id:
        if num.isalpha() or num.isdigit() or num in "._-":
            temp += num 
    #3단계
    while ".." in temp:
        temp = temp.replace("..", ".") #replace는 새로운 문자열을 반환 -> 기존 문자열은 바뀌지 않음
    
    #4단계
    temp = temp.strip(".")
    
    #5단계
    if len(temp) == 0:
        temp += "a"
        
    #6단계
    
    if len(temp) >= 16:
        temp= temp[:15]
        if temp[-1] == ".":
            temp = temp.rstrip(".")
    
    while len(temp) <= 2:
        temp += temp[-1]
        
    new_id = temp
    print(temp)
    return new_id