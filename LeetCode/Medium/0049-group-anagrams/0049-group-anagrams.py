from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        
        #키를 추가해준다.
        for s in strs:
            key = ''.join(sorted(s))
            dict[key].append(s)


            #print(s)
        return list(dict.values())
    
    
            
                            
