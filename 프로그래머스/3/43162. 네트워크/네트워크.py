from collections import deque

#연결된 노드 방문처리
def dfs(n, computers, visited, start):
    
    if start >= n:
        return 
    
    for i in range(n):
        if computers[start][i] == 1 and not visited[i]:
            visited[i] = True
            dfs(n, computers, visited, i)
    
    

def solution(n, computers):
    answer = 0
    visited = [False] *n
    
    for i in range(n):
        if not visited[i]:
            visited[i]=True
            dfs(n, computers, visited, i)
            answer +=1
    return answer