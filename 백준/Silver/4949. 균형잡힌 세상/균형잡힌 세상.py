import sys

while True:
    line = sys.stdin.readline().rstrip()
    if line == ".":
        break

    stack =[]
    is_balanced=True

    for char in line:
        if char == "[" or char  =="(":
            stack.append(char)
        
        elif char ==")":
            if not stack or stack[-1] != "(":
                is_balanced =False
                break
            stack.pop()
                  
        elif char =="]":
            if not stack or stack[-1] != "[":
                is_balanced =False
                break
            stack.pop()
            
    if not stack and is_balanced:
        print("yes")
    else:
        print("no")