from collections import defaultdict

def solution(id_list, report, k):
    n = len(id_list)
    memo = defaultdict(list)
    reported_list = defaultdict(list)
    member ={}
    
    for i, id in enumerate(id_list):
        reported_list[id] = 0
        member[id] = i
        
    for rep in set(report):
        a, b = rep.split()
        memo[a] = b #중복 신고 ->자동으로 중복 제거.
        reported_list[b] += 1
    
    answer =[0] * n 
    for rep in set(report):
        reporter, reported = rep.split()
        if reported_list[reported] >= k:
            answer[member[reporter]] +=1
        
    
            
            
    
    return answer