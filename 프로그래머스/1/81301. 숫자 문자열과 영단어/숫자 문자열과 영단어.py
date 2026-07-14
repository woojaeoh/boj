def solution(s):
    answer = 0
    
    #   s	result
    #   "one4seveneight"	1478
    #   "23four5six7"	234567
    #   "2three45sixseven"	234567
    #   "123"	123
    
    #   문제 이해
    
    #   접근 방식
    #   영어는 key로 사용, 숫자는 그냥 더함
    #   
    
    
    dict = {
        "zero" : 0 ,    
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9
    }
    
    result = ""
    ans = ""
    
    for i in s:
        if ans and ans in dict:
            result += str(dict[ans])
            ans = ""
            
        if i.isalpha():
            ans += i
        elif i.isdigit():    
            result += i
        
    print(ans)
    if ans in dict:
        result += str(dict[ans])
            
            
    return int(result)