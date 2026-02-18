class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]* (amount +1) 
        dp[0] = 0
        
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1
             
        for i in range(amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i-coin] + 1, dp[i])
        print(dp[:amount+1])

        
        return dp[amount] if dp[amount] != float('inf') else -1  