class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        # def Queens(row, board):

        #     if row == n :
        #         res.append(["".join(r) for r in board])
        #         return

        #     for col in range(n):
        #         if ( 
        #             col not in vertical 
        #             and (row-col) not in diagonalleft
        #             and (row+col) not in diagonalright
        #         ):

        #             board[row][col] = "Q"

        #             #set에 저장
        #             vertical.add(col)
        #             diagonalleft.add(row-col)
        #             diagonalright.add(row+col)

        #             #다음 행 재귀 호출
        #             Queens(row+1, board)

        #             board[row][col] = "."
        #             vertical.remove(col)
        #             diagonalleft.remove(row-col)
        #             diagonalright.remove(row+col)



        # res=[] #정답판
        # board=[["."]*n for _ in range(n)] 

        # vertical, diagonalleft, diagonalright =set(),set(),set()

        # Queens(0,board)

        # return res





        
        #n퀸 -> n개의 퀸이 공격x
        answer = []

        def Queens(rows, board):
            #base case
            if rows == n:
                answer.append(["".join(r)for r in board])                
                return

            for cols in range(n):
                if cols not in col_set and (rows-cols) not in left_diagonal and (rows+cols) not in right_diagonal:
                    col_set.add(cols)
                    left_diagonal.add(rows-cols)        
                    right_diagonal.add(rows+cols)
                    board[rows][cols] = 'Q'

                    Queens(rows+1, board)

                    board[rows][cols] = '.'
                    col_set.remove(cols)
                    left_diagonal.remove(rows-cols)        
                    right_diagonal.remove(rows+cols)
                


        board = [["."]*n for _ in range(n)]

        col_set , left_diagonal, right_diagonal = set(), set(), set()
        
        Queens(0, board)
        
        return answer












