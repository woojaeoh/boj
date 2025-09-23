def solution(N, stages):
    
    memo = {}
    total = len(stages) #20만
    result =[0]* 200001
    for stage in stages:
        result[stage] += 1 
    
    for i in range(1, N+1):
        if total >0:
            memo[i] = result[i] / total
        else:
            memo[i] = 0
        total -= result[i]
    
    
    answer = sorted(memo, key =lambda x : memo[x], reverse = True)
            
    
    return answer