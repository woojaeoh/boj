import sys


n = int(sys.stdin.readline())

stack=[]
answer=[]
number = 1
    
for _ in range(n):
    input = int(sys.stdin.readline())
    while number <= input:
        stack.append(number)
        answer.append("+")
        number += 1
        
    if stack and input == stack[-1]:
        stack.pop()
        answer.append("-")    
        
   
if stack:
    print("NO")
else:
    for char in answer:
        print(char)