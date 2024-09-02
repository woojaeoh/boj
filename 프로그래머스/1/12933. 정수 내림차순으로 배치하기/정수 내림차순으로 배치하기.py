def solution(n):
    number=list(str(n))
    number.sort(reverse=True)
    answer = "".join(number)
    return int(answer)