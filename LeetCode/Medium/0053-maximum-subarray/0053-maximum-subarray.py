class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        def dp(n):
            dp = [float('-inf')] *10001
            dp[0] =0

            for i in range(1, n+1):
                dp[i] = max(nums[i-1], dp[i-1] + nums[i-1])
        
            return dp

        return max(dp(n)) if n !=1 else nums[0]
