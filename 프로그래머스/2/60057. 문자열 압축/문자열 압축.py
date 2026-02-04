def solution(s):  
    
    def compress(text, unit):
        
        words = [text[i:i+unit] for i in range(0, len(text), unit)]
        compressed = ""
        prev_word = ""
        count = 0 
        
        for word in words:
            if word == prev_word:
                count += 1
            else:
                if count > 1:
                    compressed += str(count)
                compressed += prev_word
                #새 패턴 시작
                prev_word = word
                count = 1
                
        if count >1: #마지막 부분이 압축 가능한 word일때 , 마지막 문자열 처리를 해줘야 한다.
            compressed += str(count)
            
        compressed += prev_word
        
        return len(compressed)
                
    n = len(s)
    if n ==1:
        return 1
        
    return min(compress(s, unit) for unit in range(1, n // 2 + 1))