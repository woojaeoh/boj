class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # k = len(nums)
        # result= []
        # def backtracking(curr):
            
        #     if len(curr) == k:
        #         result.append(curr[:])
        #         return

        #     for i in nums:
        #         if i not in curr:    
        #             curr.append(i)
        #             backtracking(curr)
        #             curr.pop()
                
        # backtracking([])
        # return result 



        def backtrack(curr):
            if len(curr) == n:
                answer.append(curr[:])
                return

            for i in range(n):
                if nums[i] not in curr:
                    curr.append(nums[i])
                    backtrack(curr)
                    curr.pop()

        n = len(nums)
        answer=[]
        
        backtrack([])
        return answer








