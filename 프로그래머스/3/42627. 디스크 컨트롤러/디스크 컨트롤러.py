import heapq
def solution(jobs):
    
    n = len(jobs)
    pq =[]
    jobs = sorted([(requested_at,response_time, i )for i,(requested_at, response_time) in enumerate(jobs)])
    
    time = 0 #현재 진행 시각
    idx = 0
    completed = 0 #완료한 작업 수
    turnaround_time = 0 # 모든 작업들의 turnaround time의 합 
    
    while completed < n : # 모든작업이 종료할 떄까지 # 500
         
            while idx < n and jobs[idx][0] <= time:
                requested_at,response_time, i = jobs[idx]
                heapq.heappush(pq, (response_time, requested_at , i))
                idx += 1
            
            if pq: # 수행할 작업이 있다면
                work_time, requested_at, i = heapq.heappop(pq) # 그 작업을 수행한다. 우선순위에 맞게
                time += work_time #시간은 현재 시간에 소요되는 작업 시간을 더해줌.
                turnaround_time += time - requested_at # 작업이 끝나는 시간  - 처음에 큐에 들어온 시간.
                completed += 1
                
            else: #수행할 작업이 없다면 -> 시간만 + 1
                time = jobs[idx][0]
      
    return turnaround_time // n
            
            
            