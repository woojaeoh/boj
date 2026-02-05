from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        memo = defaultdict(list) # 존재하지 않는 키에 대해 접근 할 수 있도록 하는 dict 
        for s in strs:
            key = ''.join(sorted(s)) 
            memo[key].append(s)

        print(memo)
        return list(memo.values())
                
