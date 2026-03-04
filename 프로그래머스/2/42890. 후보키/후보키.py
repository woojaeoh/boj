from itertools import combinations
def solution(relation):
    #[["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
    n = len(relation[0])
    m = len(relation)
    
    candidate_keys = [] #후보키로 선정된 것
    
    def get_combinations(start, curr, depth, comb):
        
        #base case
        if len(curr) == depth:
            comb.append(curr[:])
            return 
        
        for i in range(start, n):
            curr.append(i)
            get_combinations(i+1,curr, depth, comb)
            curr.pop()
    
    for cur_depth in range(1, n+1):
        combinations = []
        
        get_combinations(0, [], cur_depth, combinations)
        
        for cols in combinations: 
            row_set = set()
            minimality = True
            
            for keys in candidate_keys:
                if set(keys).issubset(set(cols)):
                    minimality = False
                    break
               
            if not minimality:
                continue
                    
         
            for r in relation:
                row_str = ""          
                for c in cols:
                    row_str += r[c]
                row_set.add(row_str)
                
            if len(row_set) == m:
                candidate_keys.append(cols)
                
                
    return len(candidate_keys)
            
        
        

        
    
