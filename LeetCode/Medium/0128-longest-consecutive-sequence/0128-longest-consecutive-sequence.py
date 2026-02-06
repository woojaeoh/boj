class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dict ={}
        for num in nums:
            dict[num] = True
        
        maximum = 0
        for num in set(nums):
            if num-1 not in dict: #연속된 값 중 맨 첫 값만 시작지점으로 판단.
                count = 1
                next_num = num + 1
                while True: 
                    if next_num in dict: #다음 값이 dict안에 있는지 검사.
                        count += 1
                        next_num += 1
                    else:
                        maximum = max(maximum , count) 
                        break

    
        return maximum
            