def solution(nums):
    from itertools import combinations
    answer = 0
    for i in combinations(nums,3):    
        cnt=0
        for p in range(1,sum(i)+1):
            if sum(i)%p==0:
                cnt+=1
        
        if cnt==2:
            answer+=1    

        
    return answer