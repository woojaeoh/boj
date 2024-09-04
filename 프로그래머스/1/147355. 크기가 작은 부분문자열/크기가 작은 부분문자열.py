def solution(t, p):
    result = 0
    for i in range(len(t)-len(p)+1):
        if int(p) >= int(t[i:i+len(p)]):
            result+=1
            
    return result