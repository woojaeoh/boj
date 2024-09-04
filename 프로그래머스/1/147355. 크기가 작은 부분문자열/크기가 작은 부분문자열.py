def solution(t, p):
    result = 0
    length=len(p)
    
    for i in range(len(t)-length+1):
        if int(t[i:i+length]) <= int(p):
            result+=1
            
    return result