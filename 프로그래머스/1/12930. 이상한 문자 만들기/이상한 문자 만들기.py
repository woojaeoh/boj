def solution(s):
    
    words = s.split(' ')
    answer = ''
    
    for word in words: 
        for i in range(len(word)):
            if (i+1) % 2 != 0:
                answer += word[i].upper()
            else:
                answer += word[i].lower()
        answer += ' '    
     
    return answer[:-1]