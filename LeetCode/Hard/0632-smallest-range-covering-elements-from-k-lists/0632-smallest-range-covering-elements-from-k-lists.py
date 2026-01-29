import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        pq =[]
        max_val = float('-inf')
        
        for i , num in enumerate(nums):
            heapq.heappush(pq, (num[0], i , 0))
            max_val = max(max_val, num[0])

        answer = [pq[0][0], max_val ] # 초기 -> [0, 5]
        while pq:
            min_val ,list_idx, elem_idx = heapq.heappop(pq)
            
            if len(nums[list_idx]) - 1 == elem_idx:
                break    

            next_val  = nums[list_idx][elem_idx+1]
            heapq.heappush(pq, (next_val, list_idx, elem_idx+1))

            cur_min  = pq[0][0]
            
            if max_val < nums[list_idx][elem_idx+1]:
                max_val = nums[list_idx][elem_idx+1]

            if  max_val - cur_min < answer[1] - answer[0]:
                answer[0] = cur_min
                answer[1] = max_val 
        

        return answer
            
            

        