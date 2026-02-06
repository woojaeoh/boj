class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict ={}

        for i, num in enumerate(nums):
            extra = target - num
            if extra in dict:
                return [ dict[extra], i]
            dict[num] = i
                
        return -1            
            

            


        
            

        
        
       


            
                
