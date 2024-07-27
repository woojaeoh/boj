def solution(id_list, report, k):
    answer=[0]*len(id_list) #입력받는 사람들의 리스트
    reported={x:0 for x in id_list} #신고한 사람들을 카운트 하기위한
    
    for r in set(report): #중복을 없애주기 위해 set함수 이용
        a,b= r.split()
        reported[b] += 1
        
    for r in set(report):
        a,b= r.split()
        if reported[b]>=k:
            answer[id_list.index(a)] +=1
            
    return answer
    
    return answer