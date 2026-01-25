# permutation 사용해야 함
def solution(k, dungeons):
    result = 0
    visited= [False] * len(dungeons)

    def backtracking(curr_k, count):
        nonlocal result
        result = max(count, result)
        
        for index, dungeon in enumerate(dungeons):    
            if curr_k >= dungeon[0] and not visited[index]:
                visited[index] = True
                backtracking(curr_k - dungeon[1], count + 1)
                visited[index] = False
                
    backtracking(k, 0)
    return result