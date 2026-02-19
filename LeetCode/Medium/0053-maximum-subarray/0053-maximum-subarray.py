class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n ==1:
            return nums[0]
        dp =[0] * (n+1)
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(nums[i] + dp[i-1], nums[i])
        print(dp[:])

        return max(dp) 
     