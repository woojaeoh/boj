from itertools import permutations

n=int(input())
data=list(map(int,input().split()))

mis=list(permutations(data,n))

max_sum=0

for i in mis:
    sum=0
    for j in range(n-1):
        sum+=abs(i[j]-i[j+1])
    max_sum=max(max_sum,sum)

print(max_sum)
