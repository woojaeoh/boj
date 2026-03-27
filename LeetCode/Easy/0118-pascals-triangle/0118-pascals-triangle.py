class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # numRows = 5
        pascal = [[1]*(i+1) for i in range(numRows)]
        
        for level in range(1, numRows-1):
            pos = 0
            while pos != level:
                pascal[level+1][pos+1] = pascal[level][pos] + pascal[level][pos+1] 
                pos += 1
                
        return pascal

        print(pascal)

        
        