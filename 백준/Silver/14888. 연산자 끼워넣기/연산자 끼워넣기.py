import sys

input = sys.stdin.readline
n = int(input())
number = list(map(int, input().split()))

plus, minus, mul, div = map(int, input().split())  # 2 1 1 1

max_num = -10**9 -1
min_num = 10**9 +1

def backtracking(idx, curr ,plus, minus ,mul, div ):
    global max_num, min_num
    
    if n == idx:
        max_num = max(max_num, curr)
        min_num = min(min_num, curr)
        

    if plus > 0:
        backtracking(idx+1, curr + number[idx], plus-1,minus, mul, div )
    
    if div >0:
        if curr < 0:
            backtracking(idx+1, -(-curr//number[idx]), plus, minus, mul, div - 1)
        else:   
            backtracking(idx+1, curr // number[idx], plus, minus, mul, div - 1)
        
    if minus > 0:
        backtracking(idx+1, curr - number[idx], plus, minus -1, mul, div)
        
    if mul > 0:
        backtracking(idx+1, curr * number[idx], plus, minus, mul-1 , div)
        
        
    
    
backtracking(1 ,number[0], plus, minus, mul, div)

print(max_num)
print(min_num)
