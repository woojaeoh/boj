def solution(info, edges):
    # info = [0,0,1,1,1,0,1,0,1,0,1,1]	
    # edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
    # result = 5 
    #sheep = 0, wolf = 1
    
    n = len(info)
    visited = [False] * n
    answer = 0
    
    def backtracking(sheep , wolf):
        
        if sheep > wolf: #base case
            
            nonlocal answer
            
            answer = max(answer, sheep)
    
            for parent, child in edges:
                if visited[parent] and not visited[child]:
                    visited[child] = True
                    
                    if info[child] == 0:
                        backtracking(sheep+1, wolf)
                    else:
                        backtracking(sheep, wolf+1)
                
                    visited[child] = False
    
    visited[0] = True
    backtracking(1, 0)
    
    
    return answer