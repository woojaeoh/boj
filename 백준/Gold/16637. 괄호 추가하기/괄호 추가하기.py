import sys

input = sys.stdin.readline

def solution():
    N = int(input())
    expr = input()
    nums = [int(expr[i]) for i in range(0, N, 2)] #[3, 8, 7, 9, 2]
    ops = [expr[i] for i in range(1, N ,2)] # ['+', '*', '-', '*']

    def calc(a, op, b):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
    
    def dfs(idx, value):
        #base case
        if idx == len(ops):
            return value
        
        #괄호 없이 , 현재 값을 계속해서 넘겨줌.
        res = dfs(idx + 1 , calc(value, ops[idx], nums[idx+1]))
                  
        #괄호를 치는 경우.
        if idx < len(ops) - 1: #남은 연산자가 있으면 -> 괄호로 묶음
            next = calc(nums[idx + 1], ops[idx + 1], nums[idx + 2])
            res = max(res, dfs(idx + 2, calc(value, ops[idx], next)))
            
        return res
               
    print(dfs(0, nums[0]))   
  
solution()