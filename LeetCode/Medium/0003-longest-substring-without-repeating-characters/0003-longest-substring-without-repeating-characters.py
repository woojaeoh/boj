class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    
        # cur_set = set()
        # longest = -50001
        # count = 0
        # for num in s:
        #     if num not in cur_set:
        #         cur_set.add(num)
        #         count += 1
        #     else:
        #         longest = max(longest , len(cur_set))
        #         cur_set.clear()
        #         cur_set.add(num)
        #         count = 1

        # if len(cur_set)> 0:
        #     longest = max(longest, count)

        # return longest if len(s)!=0 else 0

        cur_set = set()
        longest = 0
        start = 0
        
        for end in range(len(s)):
            
            while s[end] in cur_set:
                longest = max(longest, end-start)
                cur_set.remove(s[start])
                start+=1

            if s[end] not in cur_set:
                cur_set.add(s[end])
                
        

        return longest

            