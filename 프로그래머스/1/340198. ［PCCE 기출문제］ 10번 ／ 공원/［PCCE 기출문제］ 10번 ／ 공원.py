def solution(mats, park):
    answer = 0 
    mats.sort()
    
    #50000 -> ㄱㅊ음
    for dot in mats: # 20 
        for i in range(len(park)): #50
            for j in range(len(park[0])): #50
                result = False
                if park[i][j] == "-1" :
                    result = bfs(i, j, dot, park)
                    if result:
                        answer = dot
    
    if answer == 0:
        return -1
    
    return answer

def bfs(x, y, dot, park):
    
    for i in range(x, x + dot):
        for j in range(y, y + dot):
            if i < len(park) and j < len(park[0]):
                if park[i][j] != "-1":
                    return False
            else:
                return False
            
    return True
                
                
            