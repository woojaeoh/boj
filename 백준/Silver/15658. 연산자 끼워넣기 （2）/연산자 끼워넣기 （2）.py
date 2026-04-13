import sys

input = sys.stdin.readline
N = int(input())

num = list(map(int, input().split()))
op = list(map(int, input().split()))

min_ans = int(1e9)
max_ans = -int(1e9)

def backtrack(idx, total):
    global min_ans , max_ans
    
    if idx == N:
        min_ans = min(min_ans, total)
        max_ans = max(max_ans, total)
        return
       
    if op[0] > 0:
        op[0] -= 1
        backtrack(idx+1 , total + num[idx])
        op[0] += 1 
    
    if op[1] > 0:
        op[1] -= 1
        backtrack(idx+1 , total - num[idx])
        op[1] += 1
    
    if op[2] > 0:
        op[2] -= 1
        backtrack(idx +1, total * num[idx])
        op[2] += 1
     
    if op[3] > 0:
        if num[idx] != 0: 
            op[3] -= 1
            backtrack(idx+1, int(total / num[idx]))
            op[3] += 1

backtrack(1 , num[0])
print(max_ans)
print(min_ans)