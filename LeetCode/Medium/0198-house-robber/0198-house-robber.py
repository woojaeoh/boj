class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp= [0]* n
        dp[0] = nums[0]

        if len(nums) == 1:
            return nums[0]
            
        dp[1] = nums[1]

        for i in range(2, n):
            for j in range(i-1):
                dp[i] = max(dp[i], dp[j] + nums[i]) 
        print(dp)
        return max(dp)       