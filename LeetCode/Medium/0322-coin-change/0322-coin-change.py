class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp = [float('inf')]* (amount +1) 
        # dp[0] = 0
             
        # for i in range(amount+1):
        #     for coin in coins:
        #         if i - coin >= 0:
        #             dp[i] = min(dp[i-coin] + 1, dp[i])
        # print(dp[:amount+1])

        
        # return dp[amount] if dp[amount] != float('inf') else -1  

        dp_table  = [float('inf')] * (amount+1)
        dp_table[0] = 0

        for i in range(amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp_table[i] =  min(dp_table[i], dp_table[i-coin]+ 1 )

        
        return dp_table[amount] if dp_table[amount] != float('inf') else -1

