import sys
input = sys.stdin.readline
N = int(input())

memo= {
    0:(1,0),
    1:(0,1)
}

def fibo(x):    
    if x not in memo:
        a1, b1= fibo(x-1)
        a2, b2 =fibo(x-2)
        memo[x] = (a1+a2 , b1+b2)
    return memo[x]
    
    
for _ in range(N):
    a,b =fibo(int(input()))
    print(a,b)
    
    
   