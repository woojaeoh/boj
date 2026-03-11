from itertools import combinations
from bisect import bisect_left

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 2 
        total = sum(nums) 
        goal = total / 2  # mean값

        min_diff = 300000001

        def get_partial_sums(arr):
            result = [[] for _ in range(len(arr) + 1)]
            for count in range(len(arr)+1):
                for comb in combinations(arr, count):
                    result[count].append(sum(comb))
            return result
  

        left_sums = get_partial_sums(nums[:n])
        right_sums = get_partial_sums(nums[n:])

        #왼쪽에서 k개선택 , 오른쪽에서 n-k개 선택
        for k in range(n+1):
            left = sorted(left_sums[k])
            right = sorted(right_sums[n-k])
            
            i , j = 0 , len(right)-1

            while i < len(left) and j >= 0:
                s = left[i] + right[j]
                min_diff = min(min_diff, abs(total - 2*s))

                if 2*s > total:
                    j -= 1
                else:
                    i += 1

        return min_diff

            