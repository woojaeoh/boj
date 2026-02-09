from collections import defaultdict
def solution(id_list, report, k):
    set_report = set(report)
    member = {}
    reported_list = defaultdict(list)
    whoreport = defaultdict(list)
    result =[0] * len(id_list)
    
    for i, p in enumerate(id_list):
        member[p] = i
        reported_list[p] = 0
    
    
    for p in set_report:
        reporter, reported = p.split()
        whoreport[reporter].append(reported)
        reported_list[reported] += 1 
        
    for p in set_report:
        reporter, reported = p.split()
        if reported_list[reported] >= k:
            result[member[reporter]] += 1
            
    
    return result