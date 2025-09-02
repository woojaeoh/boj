import sys , heapq


input = sys.stdin.readline
N = int(input())

heap=[]

for _ in range(N):
    k = int(input())
    if k == 0:
        if len(heap) ==0 :
            print(0)
        else:
            value = heapq.heappop(heap)
            print(value)
    else:
        heapq.heappush(heap, k)
            
    