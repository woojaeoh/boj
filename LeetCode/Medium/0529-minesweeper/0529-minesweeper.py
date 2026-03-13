from collections import deque
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # Input: board = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]], click = [1,2]
        m = len(board)
        n = len(board[0])
        graph =[ [0] * n for _ in range(m)]
        q =  deque()

        dx = [-1,-1, -1, 0, 1, 1, 1 , 0]
        dy = [-1, 0, 1, 1, 1, 0, -1, -1]
        for i in range(m):
            for j in range(n):
                if board[i][j] == "M":
                    q.append((i, j))
                    graph[i][j] = -1

        while q:
            r, c  = q.popleft()

            for i in range(8):
                n_r = r + dx[i]
                n_c = c + dy[i]
                
                if 0 <= n_r < m and 0 <= n_c < n:
                    if graph[n_r][n_c] != -1:
                        graph[n_r][n_c] += 1
        
        def bfs(clickr, clickc):

            q.append((clickr, clickc))
            visited = [[False] * n for _ in range(m)]
            visited[clickr][clickc] = True
            
            if graph[clickr][clickc] == -1:
                board[clickr][clickc] = "X"
                return
            elif graph[clickr][clickc] >= 1 :
                board[clickr][clickc] = str(graph[clickr][clickc])
                return 

            while q:
                r, c = q.popleft()

                if graph[r][c] == -1:
                    board[r][c] = "X"
                
                if graph[r][c] == 0:
                    board[r][c] = "B"

                
                for i in range(8):
                    n_r = r + dx[i]
                    n_c = c + dy[i]
                    
                    if 0 <= n_r < m and 0 <= n_c < n :
                        if graph[n_r][n_c] == 0 and not visited[n_r][n_c]:
                            board[n_r][n_c] = "B"
                            visited[n_r][n_c] = True
                            q.append((n_r,n_c))
                        
                        elif graph[n_r][n_c] >= 1 and not visited[n_r][n_c]:
                            board[n_r][n_c] = str(graph[n_r][n_c])
                            visited[n_r][n_c] = True
                        

        bfs(click[0], click[1])
        print(graph)
        return board


