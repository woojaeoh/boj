class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        maximum = 0
        num_set = set(nums)

        for num in num_set:
            if (num-1) not in num_set:
                count = 1
                current_num = num
                while (current_num +1) in num_set:
                    current_num += 1
                    if current_num in num_set:
                        count += 1
                    else:
                        break
                maximum = max(maximum, count)
        
        return maximum
            