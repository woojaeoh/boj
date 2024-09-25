def solution(N, stages):
    answer=[]
    total_players=len(stages)
    #조건 1. 분모 줄이기
    for i in range(1,N+1):
        if total_players !=0:
            stage_count=stages.count(i)
            fail=stage_count/total_players         
            total_players-=stage_count
        
        else:
            fail=0
            
        answer.append((i,fail))
        
    answer=sorted(answer,key=lambda t:t[1],reverse=True)
    #조건 2. 실패율이 큰 순서대로 배열에 집어 넣기.
    answer=[i[0] for i in answer]
    #조건 3. 
    
    return answer