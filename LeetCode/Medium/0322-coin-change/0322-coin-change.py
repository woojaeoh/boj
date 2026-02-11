class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def dp(n):
            dp = [0] + [10001] * n
            
            for i in range(1, n+1):
                for coin in coins:
                    if i - coin >= 0:
                        dp[i] = min(dp[i] , dp[i-coin] + 1 )
            
            
            return dp[n] if dp[n] != 10001 else -1
        
        return dp(amount)
        