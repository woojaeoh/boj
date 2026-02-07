def solution(s):  
    n = len(s) // 2 + 1
    result = float('inf')
  
    for i in range(1, n+1): #자르는 단위
        answer = ""
        prev = ""
        count = 1
        for j in range(0, len(s) , i): #문자열 인덱스
            cur = s[j : j + i]
            
            if prev == cur :
                count += 1
            else:
                if count > 1:
                    answer += str(count)
                
                answer += prev
                prev = cur
                count = 1
                
        if count > 1:
            answer += str(count)
        answer += prev
            
            
                    
        result = min(result, len(answer))
        
    return result
            