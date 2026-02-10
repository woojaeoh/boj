class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def dp(n):
            memo = [0]  *n 
            max_rob = 0

            memo[0] = nums[0]
            memo[1] = nums[1]

            for i in range(2, n):
                for j in range(i-1):
                    max_rob = max(max_rob, memo[j])
                memo[i] = max_rob + nums[i]
            print(memo)
            return max( memo[n-2] , memo[n-1])

        if len(nums) ==1:
            return nums[0]

        return dp(len(nums))