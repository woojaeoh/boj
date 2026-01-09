from itertools import combinations
def solution(relation):
    answer = 0
    m = len(relation) # 인스턴스 수
    n = len(relation[0]) # 컬럼 수
    
    candidate_keys=[]
    
    #이건 그냥 combination 라이브러리쓰는게 훨신 나을것 같긴함.
    #복습할때 combination으로 해결해보기
    
#     def get_combinations(start, depth, max_depth, curr, result_combs):
#         if depth == max_depth:
#             result_combs.append(curr[:])
#             return 
        
#         for i in range(start, n):
#             curr.append(i)
#             get_combinations(i+1, depth+1, max_depth, curr, result_combs)
#             curr.pop()
            
    num_list = [ i for i in range(n)]
    
    for length in range(1, n+1):
        result = []
        
        #get_combinations(0,0,length, [], combinations) #탐색은 그저 조합을 만들기 위한 용도
        result = list(combinations(num_list, length))
        for cols in result:
            minimality = True #최소성 검사용
            row_set = set() 
            
            for key in candidate_keys:
                if set(key).issubset(set(cols)):
                    minimality = False
                    break
            
            if not minimality:
                continue
            
            for r in relation:
                row_str= ""
                for c in cols:
                    row_str += " "+ r[c]
                row_set.add(row_str)
                
            if len(row_set) == m:
                candidate_keys.append(cols)
    
    return len(candidate_keys)
