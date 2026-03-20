from collections import defaultdict, Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        need = len(t)
        t_count = defaultdict(list) #인접리스트 형태로 관리
        # 'A' :1 , 'B' :1 , 'C' :1  -> Counter를 import하는것도 좋은 방법
        for char in t:
            if char not in t_count:
                t_count[char] = 1
            else:
                t_count[char] += 1
        
        left, right = 0, 0 
        min_len = float('inf')
        min_start = 0 #갱신이 된다면
        
        while right < m:
            end  = s[right]
            if end in t_count:
                if t_count[end] > 0:
                    need -= 1
                t_count[end] -= 1
                
            right += 1

            # if t_count가 전부 0이라면 -> if A:0 and B:0 and C:0
            # 그떄부터 left를 이동하기 시작
            while need == 0:
                if right - left + 1 < min_len : #더 작은 substr이 있다면 갱신
                    min_len = right - left + 1
                    min_start = left
                
                start = s[left]
                if start in t_count:
                    t_count[start] += 1
                    if t_count[start] > 0:
                        need += 1

                left += 1

        return s[min_start : min_start + min_len] if min_len != float('inf') else ""