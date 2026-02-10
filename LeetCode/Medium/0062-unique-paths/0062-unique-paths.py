class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dp(x, y):
            if x == 0 or y ==0:
                memo[(x,y)] = 1
                return memo[(x,y)] 
    
            if (x,y) not in memo:
                memo[(x,y)] = dp(x-1, y) + dp(x, y-1)
            
            return memo[(x,y)]


        return dp(m-1, n-1)