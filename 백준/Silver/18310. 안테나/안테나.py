n=int(input())
home=list(map(int,input().split()))
home.sort()

if n%2 ==1:
  print(home[n//2])

else:
  print(home[(n//2)-1])


