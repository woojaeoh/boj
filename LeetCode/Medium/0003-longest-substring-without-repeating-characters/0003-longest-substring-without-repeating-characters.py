class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    
        cur_set = set()
        n = len(s)
        start = 0
        longest = 0

        for end in range(n):

            while s[end] in cur_set:
                longest = max(longest, end- start)
                cur_set.remove(s[start])
                start +=1    

            if s[end] not in cur_set:
                cur_set.add(s[end])

        if len(cur_set) >=1 :
            longest = max(longest, len(cur_set))

        return longest 

