class Solution:
    def partition(self, s: str) -> List[List[str]]:

        # 1. 모든 부분집합을 만들어야 한다.
        # 1-1. s를 반복문을 통해 리스트에 집어넣는다. ex) [a, a, b]
        # 1-2.  
        # 2. 
        # 3.   
        
        subset = []

        def backtracking(start, partitions):
            if start == len(s):
                subset.append(partitions[:])
                return

            for i in range(start + 1, len(s) + 1):
                
                tmp = s[start:i]
                if tmp == tmp[::-1]: #palindrome이라면

                    partitions.append(tmp)

                    backtracking(i, partitions)

                    partitions.pop()


        backtracking(0, [])
        return subset