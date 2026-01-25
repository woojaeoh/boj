class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        def get_factorial(n):
            if n==0 or n==1:
                return 1

            return n * get_factorial(n-1)
        
        factorial = [get_factorial(i) for i in range(n+1)]
        orders = [0] * n

        k-=1 #인덱스 0부터 시작하므로
        tmp =[i for i in range(n+1)]

        for i in range(n):
            count = k // factorial[n-1-i] + 1

            k = k % factorial[n-1-i]

            orders[i] = str(tmp[count])

            tmp.pop(count)

        return "".join(orders)

        
        