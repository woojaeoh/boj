import heapq

n=int(input())
cards=[]

for _ in range(n):
  heapq.heappush(cards,int(input()))

result=0
for _ in range(n-1):
  one=heapq.heappop(cards)
  two=heapq.heappop(cards)
  sum= one+two
  result+=sum
  heapq.heappush(cards,sum)

print(result)
