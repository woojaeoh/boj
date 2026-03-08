class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums) # -6
        avg = total / 2  # mean값
        min_diff = float('inf')
        
        def backtracking(start, curr):
            nonlocal min_diff

            if len(curr) == n//2 :
                min_diff = min(min_diff, abs(sum(curr) - avg))
                return        
            
            for i in range(start, n ):
                curr.append(nums[i])
                backtracking(i+1 , curr)
                curr.pop()
        

        backtracking(0, [])

        return int(2 * abs(min_diff))
            
                        

        