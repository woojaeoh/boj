n,k= map(int,input().split())

count=0

coin_types=[]

for _ in range(n):
  coin_types.append(int(input()))

coin_types.sort(reverse=True)

for coin in coin_types:
    if k//coin>=0:
        count+=k//coin
        k%=coin
    

print(count)

