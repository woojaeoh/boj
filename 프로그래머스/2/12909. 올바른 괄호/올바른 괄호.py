def solution(s):
    answer = True
    
    stack = []
    
    for i in s:
        if i == '(':
            stack.append(')')
        elif i == ')':
            if len(stack) !=0 and stack[-1] == i :
                stack.pop()
            elif len(stack) == 0 :
                answer = False
                break
      
    if len(stack) != 0:
        answer=False
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer