import sys

n = int(sys.stdin.readline())

for _ in range(n):
    stack=[]
    parn = sys.stdin.readline().strip()
    
    for char in parn: 
        if char == "(" :
            stack.append(char)

        elif char == ")":
            if stack :
                stack.pop()
            else:
                stack.append(char)
                break
                
        
    if not stack: #괄호가 없는 경우
        print("YES")
    else: #괄호가 남아 있는 경우
        print("NO")
    

        
        
        
        
