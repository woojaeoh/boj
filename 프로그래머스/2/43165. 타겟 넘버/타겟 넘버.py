def DFS(idx, numbers, curr , target):
    
    global cnt
    
    if idx == len(numbers) and curr == target:
        cnt += 1
        return
    elif idx == len(numbers):
        return
            
    DFS(idx+1, numbers, curr + numbers[idx], target )
    DFS(idx+1, numbers, curr - numbers[idx], target )
    

def solution(numbers, target):
    
    global cnt  
    cnt =0
    
    DFS(0, numbers, 0 , target)
    
    return cnt