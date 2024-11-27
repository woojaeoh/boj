def solution(s):
    answer = ''
    numlist=list(map(int,s.split()))
    numlist.sort()
    return str(numlist[0])+" "+str(numlist[-1])