class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        curr_max = nums[0]
        result = [nums[0]]

        for i in range(1, n):
            curr_max = max(curr_max + nums[i], nums[i])
            result.append(curr_max)

        return max(result) if len(result) >= 1 else nums[0]
