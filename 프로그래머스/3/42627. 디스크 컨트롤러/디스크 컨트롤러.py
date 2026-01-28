import heapq
def solution(jobs):
    
    n = len(jobs)
    jobs = sorted([(requested_at,response_time, i )for i,(requested_at, response_time) in enumerate(jobs)])
    completed = 0
    current_time = 0
    job_idx =0
    turnaround_time = 0
    
    heap = []
    
    while completed < n:
        
        while job_idx < n and jobs[job_idx][0] <= current_time: #현재시점 기준 작업할 수 있는 노드들 가져오기.
            (requested_at, response_time, i ) = jobs[job_idx]
            heapq.heappush(heap,(response_time, requested_at, i))
            job_idx += 1 
            
        if heap:
            response_time, requested_at, _ = heapq.heappop(heap)
            current_time += response_time
            turnaround_time += (current_time - requested_at) 
            completed += 1
        else:
            current_time = jobs[job_idx][0] #힙이 비었다면 , 다음 작업 요청의 시작시간으로 점프
            
    
    return turnaround_time // n