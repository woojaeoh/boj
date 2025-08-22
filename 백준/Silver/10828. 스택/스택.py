import sys

n = int(sys.stdin.readline())
stack = []
for _ in range(n):
    inst = sys.stdin.readline().split()
    cmd = inst[0]

    if cmd == "push":
        if inst[1].isdigit():
            stack.append(inst[1])
    elif cmd == "top":
        if stack:  
            print(stack[len(stack)-1]) 
        else: print(-1)
    elif cmd == "size":
        if stack:
            print(len(stack))
        else: print(0)
    elif cmd == "pop":
        if stack:
            print(stack.pop())
        else: print(-1)
    elif cmd == "empty":
        if not stack:
            print(1)
        else:
            print(0)
 
